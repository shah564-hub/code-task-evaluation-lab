# CodeLab — Evaluation Studio

An interactive Python coding challenge platform built with Streamlit. Write solutions, run predefined test cases, inspect expected and actual outputs, and review evaluation results through a modern developer-focused interface.

🚀 **[Live Demo — Try CodeLab](https://code-task-evaluation-lab-6bsuvdb7ytq6kkneeyanz3.streamlit.app/)**

## Overview

CodeLab — Evaluation Studio is a portfolio project exploring how coding assessment tools can evaluate programming solutions and communicate results clearly.

The application combines an interactive coding workspace with a Python evaluation engine and a collection of algorithm challenges.

## Features

- **Interactive coding workspace** — edit Python solutions directly in the app.
- **Automated evaluation** — run supported solutions against predefined test cases.
- **Test result reporting** — inspect passed and failed cases.
- **Expected vs. actual output** — compare results for individual tests.
- **Performance timing** — display measured function execution time.
- **Challenge library** — explore algorithm challenges.
- **Dark developer-focused UI** — a polished interface built with Streamlit.
- **Automated tests** — verify evaluator behavior using pytest.

## Challenges

The current challenge library includes:

- Two Sum
- Palindrome Checker
- Valid Parentheses

Evaluation support depends on the current implementation of each challenge.

## Tech Stack

- Python
- Streamlit
- pytest
- Abstract Syntax Tree (AST) validation
- Git and GitHub

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shah564-hub/code-task-evaluation-lab.git
cd code-task-evaluation-lab
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL shown in your terminal, usually `http://localhost:8501`.

## Run Tests

Run the automated test suite with:

```bash
python -m pytest -v
```

## Project Structure

```text
code-task-evaluation-lab/
├── app.py
├── evaluator.py
├── requirements.txt
├── README.md
└── tests/
    ├── __init__.py
    ├── test_app.py
    └── test_evaluator.py
```

## Security Note

This project is a learning prototype. AST validation and restricted built-ins do not constitute a secure sandbox. Executing arbitrary or untrusted Python code can still be dangerous.

Do not expose the current evaluator to public submissions without proper process isolation, resource limits, timeouts, and other security controls.

## Future Improvements

- Expand automated evaluation support across all challenges.
- Add submission history and evaluation summaries.
- Improve test coverage and error reporting.
- Add isolated execution for untrusted code.
- Deploy a publicly accessible demo.

## Author

**Shahida**

Built as a portfolio project to explore Python evaluation logic, automated testing, and interactive developer tools.
