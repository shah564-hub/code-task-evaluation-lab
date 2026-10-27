import html
from datetime import datetime

import streamlit as st
from evaluator import evaluate_code


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CodeLab | Evaluation Studio",
    page_icon="⌘",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PREMIUM DARK DESIGN SYSTEM
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #0b0d12;
        --panel: #12151d;
        --line: #272d3a;
        --muted: #929bad;
        --text: #f0f2f8;
        --violet: #a78bfa;
        --mint: #6ee7b7;
    }

    .stApp {
        background: var(--bg);
        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stSidebar"] {
        background: #0e1118;
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, p, label {
        color: var(--text);
    }

    h1 {
        letter-spacing: -1.8px;
        font-weight: 800;
    }

    h2, h3 {
        letter-spacing: -0.5px;
    }

    p, label {
        line-height: 1.6;
    }

    .brand {
        font-size: 23px;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .brand span {
        color: var(--violet);
    }

    .eyebrow {
        color: var(--mint);
        font-family: 'DM Mono', monospace;
        text-transform: uppercase;
        font-size: 11px;
        letter-spacing: 2px;
    }

    .hero {
        background:
            radial-gradient(ellipse at 95% 0%, #302454 0%, transparent 42%),
            linear-gradient(135deg, #171a26, #10131a 65%);
        border: 1px solid #343047;
        border-radius: 20px;
        padding: 28px 30px;
        margin-bottom: 22px;
    }

    .hero h1 {
        font-size: clamp(30px, 4vw, 43px);
        margin: 10px 0 8px;
    }

    .hero p {
        color: #aeb6c8;
        max-width: 700px;
    }

    .panel {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
    }

    .metric {
        background: linear-gradient(145deg, #171b25, #11141b);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 18px;
        min-height: 110px;
    }

    .metric-label {
        color: #b9c3d8;
        font-size: 12px;
        margin-bottom: 12px;
    }

    .metric-value {
        color: var(--text);
        font-size: 27px;
        font-weight: 800;
    }

    .metric-note {
        color: #b0bacd;
        font-size: 11px;
        margin-top: 5px;
    }

    .pill {
        display: inline-block;
        border: 1px solid #3a3157;
        background: #211b34;
        color: #c4b5fd;
        border-radius: 999px;
        padding: 5px 10px;
        font-size: 11px;
        font-family: 'DM Mono', monospace;
    }

    .pill-mint {
        border-color: #205342;
        background: #102a23;
        color: var(--mint);
    }

    .section-title {
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .section-subtitle {
        color: #aab5ca;
        font-size: 12px;
        margin-bottom: 18px;
    }

    /* Challenge selector */

    div[data-testid="stSelectbox"] label {
        color: #f0f2f8 !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
        background-color: #171b26 !important;
        border: 1px solid #454d60 !important;
        border-radius: 10px !important;
        opacity: 1 !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="select"] div[class*="singleValue"],
    div[data-testid="stSelectbox"] [data-baseweb="select"] div[class*="valueContainer"] {
        color: #f0f2f8 !important;
        opacity: 1 !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="select"] input {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        opacity: 1 !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="select"] svg {
        fill: #e5e7eb !important;
        color: #e5e7eb !important;
    }

    div[data-baseweb="popover"] ul,
    ul[data-baseweb="menu"] {
        background-color: #171b26 !important;
    }

    div[data-baseweb="popover"] li,
    li[data-baseweb="option"] {
        background-color: #171b26 !important;
        color: #f0f2f8 !important;
        opacity: 1 !important;
    }

    div[data-baseweb="popover"] li:hover,
    li[data-baseweb="option"]:hover {
        background-color: #302747 !important;
        color: #ffffff !important;
    }

    /* Buttons */

    div.stButton > button {
        background: linear-gradient(135deg, #a78bfa, #8b5cf6);
        color: #100d1c;
        border: none;
        border-radius: 10px;
        font-weight: 800;
        min-height: 43px;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        color: #08070c;
        box-shadow: 0 0 24px #8b5cf644;
        transform: translateY(-1px);
    }

    /* Code editor */

    div[data-testid="stTextArea"] textarea {
        background: #0b0e14 !important;
        color: #e5edfc !important;
        border: 1px solid #454d60;
        border-radius: 10px;
        font-family: 'DM Mono', monospace;
        font-size: 13px;
        opacity: 1 !important;
    }

    div[data-testid="stExpander"] {
        background: #10131a;
        border: 1px solid var(--line);
        border-radius: 12px;
    }

    /* Result output panels */

    .output-value {
        box-sizing: border-box;
        width: 100%;
        min-height: 48px;
        display: flex;
        align-items: center;
        padding: 12px 14px;
        background: #171b26;
        border: 1px solid #30384a;
        border-radius: 10px;
        color: #a7f3d0;
        font-family: 'DM Mono', monospace;
        font-size: 13px;
        white-space: pre-wrap;
        overflow-wrap: anywhere;
    }

    .result-label {
        color: #929bad;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .result-note {
        color: #aeb6c8;
        font-size: 12px;
        margin-top: 12px;
    }

    .status-card {
        border-radius: 15px;
        padding: 18px 20px;
        margin: 8px 0 18px;
    }

    hr {
        border-color: var(--line);
    }

    footer {
        visibility: hidden;
    }
    /* Fix light backgrounds in expandable panels */
div[data-testid="stExpander"] {
    background-color: #10131a !important;
    border: 1px solid #303746 !important;
    border-radius: 12px !important;
}

div[data-testid="stExpander"] details,
div[data-testid="stExpander"] summary {
    background-color: #10131a !important;
    color: #f0f2f8 !important;
}

div[data-testid="stExpander"] summary span,
div[data-testid="stExpander"] summary p {
    color: #f0f2f8 !important;
}

div[data-testid="stCode"],
div[data-testid="stCode"] pre,
div[data-testid="stCode"] code {
    background-color: #171b26 !important;
    color: #e5edfc !important;
}
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# CHALLENGE DATA
# ============================================================

CHALLENGES = {
    "Two Sum": {
        "function_name": "two_sum",
        "difficulty": "EASY",
        "category": "Arrays & Hashing",
        "description": (
            "Given a list of integers and a target, return the indices "
            "of two numbers that add up to the target."
        ),
        "starter": (
            "def two_sum(nums, target):\n"
            "    # Return the indices of two values that sum to target.\n"
            "    pass\n"
        ),
        "cases": [
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
            {
                "name": "No matching pair",
                "args": ([1, 2, 3], 10),
                "expected": [],
            },
        ],
        "examples": [
            ("[2, 7, 11, 15], 9", "[0, 1]"),
            ("[3, 2, 4], 6", "[1, 2]"),
            ("[3, 3], 6", "[0, 1]"),
        ],
    },

    "Palindrome Checker": {
        "function_name": "is_palindrome",
        "difficulty": "EASY",
        "category": "Strings",
        "description": (
            "Return True if a string reads the same forwards and "
            "backwards, ignoring letter case."
        ),
        "starter": (
            "def is_palindrome(text):\n"
            "    # Ignore letter case when comparing.\n"
            "    pass\n"
        ),
        "cases": [
            {
                "name": "Mixed-case palindrome",
                "args": ("Level",),
                "expected": True,
            },
            {
                "name": "Not a palindrome",
                "args": ("Python",),
                "expected": False,
            },
            {
                "name": "Capitalized palindrome",
                "args": ("Madam",),
                "expected": True,
            },
            {
                "name": "Empty string",
                "args": ("",),
                "expected": True,
            },
        ],
        "examples": [
            ("'Level'", "True"),
            ("'Python'", "False"),
            ("'Madam'", "True"),
        ],
    },

    "Valid Parentheses": {
        "function_name": "is_valid",
        "difficulty": "MEDIUM",
        "category": "Stacks",
        "description": (
            "Determine whether every opening bracket has a matching "
            "closing bracket in the correct order."
        ),
        "starter": (
            "def is_valid(text):\n"
            "    # Check (), [] and {} in the correct order.\n"
            "    pass\n"
        ),
        "cases": [
            {
                "name": "Multiple bracket types",
                "args": ("()[]{}",),
                "expected": True,
            },
            {
                "name": "Incorrect order",
                "args": ("([)]",),
                "expected": False,
            },
            {
                "name": "Nested brackets",
                "args": ("{[]}",),
                "expected": True,
            },
            {
                "name": "Unclosed bracket",
                "args": ("((",),
                "expected": False,
            },
            {
                "name": "Empty string",
                "args": ("",),
                "expected": True,
            },
        ],
        "examples": [
            ("'()[]{}'", "True"),
            ("'([)]'", "False"),
            ("'{[]}'", "True"),
        ],
    },
}


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:
    st.markdown(
        '<div class="brand">code<span>lab</span>'
        '<sup style="font-size:10px;color:#929bad"> / EVAL</sup></div>',
        unsafe_allow_html=True,
    )

    st.caption("AI CODE EVALUATION WORKSPACE")
    st.divider()

    page = st.radio(
        "WORKSPACE",
        [
            "Evaluation Studio",
            "Challenge Library",
            "About this project",
        ],
    )

    st.divider()
    st.markdown("**WORKSPACE STATUS**")

    st.markdown(
        '<span class="pill pill-mint">● UI ONLINE</span> '
        '<span class="pill">LOCAL PROTOTYPE</span>',
        unsafe_allow_html=True,
    )

    st.write("")
    st.caption("Local development build")
    st.caption("Python · Streamlit · pytest")


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    '<div class="eyebrow">DEVELOPER TOOLS / CODE QUALITY</div>',
    unsafe_allow_html=True,
)


# ============================================================
# EVALUATION STUDIO
# ============================================================

if page == "Evaluation Studio":

    st.markdown(
        """
        <div class="hero">
            <span class="pill">EVALUATION STUDIO · V0.3</span>
            <h1>Test your logic.<br>Trust your results.</h1>
            <p>
                A workspace for coding challenges, test design,
                edge-case analysis, and transparent code evaluation.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Summary cards
    metrics = [
        ("CHALLENGES", "03", "Available challenges"),
        ("TEST ENGINE", "Connected", "Local prototype"),
        ("LANGUAGE", "Python", "Current language"),
        ("BUILD", "0.3.0", "Development version"),
    ]

    columns = st.columns(4)

    for col, (label, value, note) in zip(columns, metrics):
        with col:
            st.markdown(
                f"""
                <div class="metric">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-note">{note}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")

    left, right = st.columns([1.45, 1], gap="large")

    # --------------------------------------------------------
    # LEFT COLUMN: CHALLENGE AND EDITOR
    # --------------------------------------------------------

    with left:
        st.markdown(
            '<div class="section-title">01 / Choose a challenge</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Select a task to load its prompt and starter code.'
            '</div>',
            unsafe_allow_html=True,
        )

        challenge_name = st.selectbox(
            "Coding challenge",
            list(CHALLENGES.keys()),
            label_visibility="collapsed",
            key="challenge_selector",
        )

        challenge = CHALLENGES[challenge_name]

        st.markdown(
            f'<span class="pill">{challenge["difficulty"]}</span> '
            f'<span class="pill">{challenge["category"]}</span>',
            unsafe_allow_html=True,
        )

        st.write("")
        st.markdown("**Problem statement**")
        st.write(challenge["description"])

        with st.expander("View example cases", expanded=False):
            for index, (inputs, output) in enumerate(
                challenge["examples"],
                start=1,
            ):
                st.code(
                    f"Case {index}\nInput:  {inputs}\nOutput: {output}",
                    language="text",
                )

        st.markdown(
            '<div class="section-title">02 / Solution editor</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Python starter code · editing is enabled'
            '</div>',
            unsafe_allow_html=True,
        )

        code = st.text_area(
            "Your Python solution",
            value=challenge["starter"],
            height=270,
            label_visibility="collapsed",
            key=f"editor_{challenge_name}",
        )

        st.caption(
            "Your code is evaluated locally. This prototype is not "
            "a secure sandbox for untrusted submissions."
        )

        run_clicked = st.button(
            "▶ Run Evaluation",
            use_container_width=True,
        )

    # --------------------------------------------------------
    # RIGHT COLUMN: STATUS AND RESULTS
    # --------------------------------------------------------

    with right:
        st.markdown(
            '<div class="section-title">Evaluation overview</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Local execution and challenge-specific test reporting.'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="panel">
                <div class="eyebrow">CURRENT SESSION</div>
                <h3 style="margin-top:12px">Evaluation engine ready</h3>
                <p style="color:#b0bacd;font-size:13px">
                    Run your solution to see test results, pass rate,
                    errors, and measured function timing.
                </p>
                <hr>
                <div style="display:flex;justify-content:space-between;
                            gap:12px;margin:12px 0">
                    <span style="color:#b0bacd">Execution engine</span>
                    <span style="color:#6ee7b7">Connected · local</span>
                </div>
                <div style="display:flex;justify-content:space-between;
                            gap:12px;margin:12px 0">
                    <span style="color:#b0bacd">Sandbox isolation</span>
                    <span style="color:#fbbf24">Not configured</span>
                </div>
                <div style="display:flex;justify-content:space-between;
                            gap:12px;margin:12px 0">
                    <span style="color:#b0bacd">Supported challenges</span>
                    <span style="color:#6ee7b7">3</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Run the selected challenge's own test cases
        if run_clicked:
            try:
                results = evaluate_code(
                    source=code,
                    function_name=challenge["function_name"],
                    cases=challenge["cases"],
                )

                passed = sum(
                    result.passed for result in results
                )
                failed = len(results) - passed

                rate = (
                    passed / len(results) * 100
                    if results
                    else 0
                )

                duration = sum(
                    result.duration_ms for result in results
                )

                # Evaluation status banner
                status_title = (
                    "All tests passed"
                    if failed == 0
                    else "Some tests failed"
                )

                status_detail = (
                    "Your solution passed every available test case."
                    if failed == 0
                    else f"{failed} test case(s) need attention."
                )

                status_bg = (
                    "#102a23" if failed == 0 else "#2a171d"
                )
                status_border = (
                    "#205342" if failed == 0 else "#71313d"
                )
                status_accent = (
                    "#6ee7b7" if failed == 0 else "#fda4af"
                )

                st.markdown(
                    f"""
                    <div class="status-card"
                         style="background:{status_bg};
                                border:1px solid {status_border}">
                        <div style="color:{status_accent};
                                    font-family:'DM Mono',monospace;
                                    font-size:10px;
                                    letter-spacing:2px;
                                    font-weight:700">
                            EVALUATION STATUS
                        </div>
                        <div style="color:#f0f2f8;
                                    font-size:21px;
                                    font-weight:800;
                                    margin:8px 0">
                            {status_title}
                        </div>
                        <div style="color:#c4ccda;font-size:12px">
                            {status_detail}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # Summary metrics
                st.markdown("### Evaluation Results")

                a, b, c = st.columns(3)
                a.metric("Passed", passed)
                b.metric("Failed", failed)
                c.metric("Pass rate", f"{rate:.0f}%")

                st.progress(rate / 100)

                st.caption(
                    f"{len(results)} test cases · "
                    f"{duration:.3f} ms combined measured function time"
                )

                # Individual test case details
                st.markdown("### Test case details")

                for result in results:
                    icon = "✅" if result.passed else "❌"

                    with st.expander(
                        f"{icon} {result.name}",
                        expanded=not result.passed,
                    ):
                        expected_text = html.escape(
                            repr(result.expected)
                        )
                        actual_text = html.escape(
                            repr(result.actual)
                        )

                        left_result, right_result = st.columns(2)

                        with left_result:
                            st.markdown(
                                '<div class="result-label">'
                                'EXPECTED OUTPUT</div>',
                                unsafe_allow_html=True,
                            )

                            st.markdown(
                                f'<div class="output-value">'
                                f'{expected_text}</div>',
                                unsafe_allow_html=True,
                            )

                        with right_result:
                            st.markdown(
                                '<div class="result-label">'
                                'ACTUAL OUTPUT</div>',
                                unsafe_allow_html=True,
                            )

                            st.markdown(
                                f'<div class="output-value">'
                                f'{actual_text}</div>',
                                unsafe_allow_html=True,
                            )

                        if result.error:
                            st.error(result.error)

                        elif result.passed:
                            st.markdown(
                                '<div class="result-note">'
                                '✓ Output matches the expected result.'
                                '</div>',
                                unsafe_allow_html=True,
                            )

                        else:
                            st.warning(
                                "This test did not match the expected "
                                "result. Review the output and your solution."
                            )

                if failed == 0:
                    st.success("All test cases passed!")
                else:
                    st.error(
                        f"{failed} test case(s) failed. "
                        "Review the failing cases above."
                    )

            except (SyntaxError, ValueError, TypeError) as exc:
                st.error(
                    f"Could not evaluate submission: {exc}"
                )

            except Exception as exc:
                st.error(
                    f"Unexpected evaluation error: "
                    f"{type(exc).__name__}: {exc}"
                )

        # Evaluation principles
        st.markdown(
            '<div class="section-title">Evaluation principles</div>',
            unsafe_allow_html=True,
        )

        principles = [
            (
                "Correctness",
                "Compare expected and actual outputs.",
            ),
            (
                "Edge cases",
                "Test empty, boundary, and unusual inputs.",
            ),
            (
                "Transparency",
                "Report passed tests and failures.",
            ),
            (
                "Safety",
                "Do not run untrusted code without isolation.",
            ),
        ]

        for title, detail in principles:
            st.markdown(
                f'<div style="padding:12px 0;'
                f'border-bottom:1px solid #272d3a">'
                f'<div style="font-weight:600">{title}</div>'
                f'<div style="color:#b0bacd;font-size:12px">'
                f'{detail}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )


# ============================================================
# CHALLENGE LIBRARY
# ============================================================

elif page == "Challenge Library":
    st.markdown("# Challenge Library")

    st.caption(
        "Browse the coding challenges available in this prototype."
    )

    for name, item in CHALLENGES.items():
        with st.container(border=True):
            st.markdown(f"### {name}")

            st.markdown(
                f'<span class="pill">{item["difficulty"]}</span> '
                f'<span class="pill">{item["category"]}</span>',
                unsafe_allow_html=True,
            )

            st.write(item["description"])

            st.caption(
                f'{len(item["cases"])} automated test cases'
            )

            with st.expander("Preview test cases"):
                for case in item["cases"]:
                    st.markdown(f"**{case['name']}**")
                    st.code(
                        f"Input: {case['args']}\n"
                        f"Expected: {case['expected']}",
                        language="text",
                    )


# ============================================================
# ABOUT
# ============================================================

else:
    st.markdown("# About CodeLab")

    st.write(
        "CodeLab is a portfolio project exploring automated code "
        "evaluation, test design, and transparent reporting. The local "
        "prototype evaluates submitted functions against test cases "
        "for three Python challenges. It is not a secure environment "
        "for untrusted submissions."
    )

    st.markdown("### Current architecture")

    st.code(
        "Streamlit UI\n"
        "    ↓\n"
        "Local evaluation function\n"
        "    ↓\n"
        "Challenge-specific test cases\n"
        "    ↓\n"
        "Test results + error report\n\n"
        "Next improvement: isolated execution worker",
        language="text",
    )

    st.markdown("### Current capabilities")

    st.markdown(
        """
        - Three coding challenges with separate test cases
        - Editable Python solution area
        - Expected-versus-actual output comparison
        - Pass/fail reporting and measured function timing
        - Challenge library and example-case previews
        """
    )

    st.warning(
        "Security note: AST validation is not a security sandbox. "
        "A production evaluator needs proper process isolation and "
        "resource limits before accepting untrusted code."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    '<div style="display:flex;justify-content:space-between;'
    'gap:12px;flex-wrap:wrap;color:#929bad;font-size:11px">'
    '<span>CODELAB / EVALUATION STUDIO</span>'
    '<span>Built as a learning project · '
    + datetime.now().strftime("%d %b %Y")
    + "</span></div>",
    unsafe_allow_html=True,
)