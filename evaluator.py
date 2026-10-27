
import ast
import time
from dataclasses import dataclass


@dataclass
class TestResult:
    name: str
    passed: bool
    expected: object
    actual: object
    error: str | None = None
    duration_ms: float = 0.0


# Supported syntax for this local prototype.
# This is NOT a secure sandbox for untrusted code.
ALLOWED_NODES = (
    ast.Module,
    ast.FunctionDef,
    ast.arguments,
    ast.arg,
    ast.Return,
    ast.Assign,
    ast.AugAssign,
    ast.Expr,
    ast.If,
    ast.For,
    ast.Break,
    ast.Continue,
    ast.Pass,
    ast.Name,
    ast.Load,
    ast.Store,
    ast.Constant,
    ast.List,
    ast.Tuple,
    ast.Dict,
    ast.Set,
    ast.Subscript,
    ast.Slice,
    ast.BinOp,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.FloorDiv,
    ast.Mod,
    ast.UnaryOp,
    ast.USub,
    ast.UAdd,
    ast.Not,
    ast.Compare,
    ast.Eq,
    ast.NotEq,
    ast.Lt,
    ast.LtE,
    ast.Gt,
    ast.GtE,
    ast.In,
    ast.NotIn,
    ast.BoolOp,
    ast.And,
    ast.Or,
    ast.Call,
    ast.keyword,
    ast.Attribute,
)

SAFE_BUILTINS = {
    "len": len,
    "range": range,
    "enumerate": enumerate,
    "min": min,
    "max": max,
    "sum": sum,
    "abs": abs,
    "all": all,
    "any": any,
    "sorted": sorted,
}


# Only these object methods are supported by the prototype.
ALLOWED_METHODS = {
    "lower",
    "append",
    "pop",
}


def validate_code(source: str) -> ast.Module:
    """Parse code and reject syntax outside the supported subset."""

    if not source.strip():
        raise ValueError("Please enter your solution before evaluating.")

    if len(source) > 12000:
        raise ValueError(
            "Code is too long (maximum 12,000 characters)."
        )

    tree = ast.parse(source)

    for node in ast.walk(tree):
        if not isinstance(node, ALLOWED_NODES):
            raise ValueError(
                f"Unsupported syntax: {type(node).__name__}"
            )

        if isinstance(node, ast.Name) and node.id.startswith("__"):
            raise ValueError(
                "Names beginning with '__' are not allowed."
            )

        if isinstance(node, ast.Attribute):
            if node.attr not in ALLOWED_METHODS:
                raise ValueError(
                    f"Method or attribute '{node.attr}' is not allowed."
                )

            if not isinstance(node.value, ast.Name):
                raise ValueError(
                    "Method calls must use a simple variable."
                )

        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id not in SAFE_BUILTINS:
                    raise ValueError(
                        f"Function calls to '{node.func.id}' "
                        "are not allowed."
                    )

            elif isinstance(node.func, ast.Attribute):
                if node.func.attr not in ALLOWED_METHODS:
                    raise ValueError(
                        f"Method '{node.func.attr}' is not allowed."
                    )

                if not isinstance(node.func.value, ast.Name):
                    raise ValueError(
                        "Method calls must use a simple variable."
                    )

            else:
                raise ValueError(
                    "Only approved function and method calls are allowed."
                )

    functions = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef)
    ]

    if len(functions) != 1:
        raise ValueError(
            "Submit exactly one function definition."
        )

    if len(tree.body) != 1:
        raise ValueError(
            "Submit only one function definition, "
            "without extra top-level statements."
        )

    return tree


def evaluate_code(
    source: str,
    function_name: str,
    cases: list[dict],
) -> list[TestResult]:
    """
    Evaluate a submitted function against test cases.

    Each case contains:
      name: descriptive test name
      args: positional arguments
      expected: expected return value
    """

    tree = validate_code(source)

    function_names = [
        node.name for node in tree.body
        if isinstance(node, ast.FunctionDef)
    ]

    if function_name not in function_names:
        raise ValueError(
            f"Your code must define '{function_name}(...).'"
        )

    namespace = {"__builtins__": SAFE_BUILTINS}
    compiled = compile(tree, "<submission>", "exec")
    exec(compiled, namespace)

    function = namespace[function_name]
    results = []

    for index, case in enumerate(cases, start=1):
        started = time.perf_counter()

        try:
            actual = function(*case["args"])
            duration = (
                time.perf_counter() - started
            ) * 1000

            expected = case["expected"]

            results.append(
                TestResult(
                    name=case.get("name", f"Test case {index}"),
                    passed=(actual == expected),
                    expected=expected,
                    actual=actual,
                    duration_ms=round(duration, 3),
                )
            )

        except Exception as exc:
            duration = (
                time.perf_counter() - started
            ) * 1000

            results.append(
                TestResult(
                    name=case.get("name", f"Test case {index}"),
                    passed=False,
                    expected=case.get("expected"),
                    actual=None,
                    error=f"{type(exc).__name__}: {exc}",
                    duration_ms=round(duration, 3),
                )
            )

    return results
