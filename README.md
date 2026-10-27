# CodeLab — Evaluation Studio

A Python-based coding challenge evaluation platform built with Streamlit. CodeLab provides an interactive workspace where users can solve programming challenges, run test cases, and inspect evaluation results.

## Features

- **Interactive coding workspace** — select a challenge and edit Python starter code.
- **Challenge library** — includes Two Sum, Palindrome Checker, and Valid Parentheses.
- **Automated evaluation** — compare expected outputs with actual outputs.
- **Test reports** — view passed and failed test cases, pass rate, and measured execution time.
- **Error handling** — report supported syntax, validation, and runtime errors.
- **Dark interface** — custom styling with a graphite background, violet accents, and mint highlights.
- **Automated tests** — pytest-based tests for core evaluator behavior.

## Tech Stack

- Python
- Streamlit
- pytest
- Python AST-based code validation

## Project Structure

```text
code-task-evaluation-lab/
├── app.py
├── evaluator.py
├── requirements.txt
├── README.md
└── tests/
    ├── __init__.py
    └── test_evaluator.py
```

## Getting Started

### Prerequisites

- Python installed
- pip package manager

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd code-task-evaluation-lab
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL after publishing the project.

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## Running Automated Tests

Run the test suite from the project directory:

```bash
python -m pytest -v
```

The current test suite covers successful evaluation, incorrect solutions, runtime errors, rejected imports, and missing functions.

## Security Notice

**This project is a local learning prototype, not a secure sandbox for untrusted code.**

AST-based validation and restricted execution globals do not guarantee isolation from malicious Python code. Do not expose the current evaluator to public submissions or run code from untrusted users in a production environment without implementing robust process or container isolation and appropriate resource limits.

## Current Status

- Interactive Streamlit interface implemented.
- Three coding challenges available.
- Local evaluation and test reporting implemented.
- Automated evaluator tests currently pass in the development environment.
- Secure execution for untrusted submissions is not implemented.

## Future Improvements

- Add more programming challenges and edge cases.
- Improve evaluator test coverage.
- Add execution timeouts and resource limits through a suitable isolation layer.
- Add downloadable evaluation reports.
- Improve accessibility and responsive layout.
- Publish a hosted demo after reviewing execution security.

## Author

Developed as a software engineering portfolio project to explore coding challenge evaluation, test-driven development, and Python application design.
