# Statistics Tui Dashboard

This is a terminal-based statistics dashboard that lets you explore data distributions and test hypotheses from the comfort of your command line. Built with pure Python, it features interactive panels and dynamic visualizations to help you quickly grasp key statistical concepts. Whether you're a researcher or student, this tool is designed to make stats more intuitive and fun.

## What makes it unique

Combines distribution fitting and hypothesis tests with a live-updating curses dashboard with panels and sparklines — a niche where few ready-made tools exist.

## Features

- **`statistics_dashboard/app.py`** — Main application entry point
- **`statistics_dashboard/core.py`** — Core functionality for distribution fitting and hypothesis tests
- **`statistics_dashboard/dashboard.py`** — Curses dashboard implementation with panels and sparklines
- **`statistics_dashboard/models.py`** — Data models and structures used throughout the application
- **`statistics_dashboard/tests_test_core.py`** — Unit tests for core functionality
- **`statistics_dashboard/utils.py`** — Utility functions used across the application

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/statistics-dashboard.git
cd statistics-dashboard

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
statistics-dashboard/
├── statistics_dashboard/
│   ├── app.py
│   ├── core.py
│   ├── dashboard.py
│   ├── models.py
│   ├── tests_test_core.py
│   ├── utils.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **statistics** · Archetype: **dashboard** ·
Built autonomously by JARVIS on 2026-10-31. MIT licensed.
