
import pytest

from evaluator import evaluate_code, validate_code


def test_two_sum_passes_all_cases():
    source = """
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
"""
    cases = [
        {
            "name": "Basic pair",
            "args": ([2, 7, 11, 15], 9),
            "expected": [0, 1],
        },
        {
            "name": "Pair in middle",
            "args": ([3, 2, 4], 6),
            "expected": [1, 2],
        },
        {
            "name": "Duplicate values",
            "args": ([3, 3], 6),
            "expected": [0, 1],
        },
    ]

    results = evaluate_code(source, "two_sum", cases)

    assert len(results) == 3
    assert all(result.passed for result in results)


def test_wrong_answer_is_reported():
    source = """
def two_sum(nums, target):
    return [0, 0]
"""
    cases = [
        {
            "name": "Wrong indices",
            "args": ([2, 7], 9),
            "expected": [0, 1],
        }
    ]

    results = evaluate_code(source, "two_sum", cases)

    assert results[0].passed is False
    assert results[0].actual == [0, 0]


def test_runtime_error_is_captured():
    source = """
def two_sum(nums, target):
    return missing_variable
"""
    cases = [
        {
            "name": "Undefined variable",
            "args": ([2, 7], 9),
            "expected": [0, 1],
        }
    ]

    results = evaluate_code(source, "two_sum", cases)

    assert results[0].passed is False
    assert "NameError" in results[0].error


def test_imports_are_rejected():
    source = """
import os
def two_sum(nums, target):
    return []
"""
    with pytest.raises(ValueError):
        validate_code(source)


def test_missing_function_is_rejected():
    source = """
def another_function():
    return 42
"""
    with pytest.raises(ValueError):
        evaluate_code(source, "two_sum", [])
def test_empty_cases_are_rejected():
    import pytest
    from evaluator import evaluate_code

    with pytest.raises(ValueError, match="At least one test case"):
        evaluate_code(
            "def solve(x): return x",
            "solve",
            [],
        )


def test_more_than_50_cases_are_rejected():
    import pytest
    from evaluator import evaluate_code

    cases = [
        {"name": f"Test {i}", "args": [i], "expected": i}
        for i in range(51)
    ]

    with pytest.raises(ValueError, match="maximum of 50"):
        evaluate_code(
            "def solve(x): return x",
            "solve",
            cases,
        )