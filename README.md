# 🔀 GitFlow Portfolio

![CI Pipeline](https://github.com/YOURUSERNAME/gitflow-portfolio/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A demonstration of professional Git workflow, CI/CD automation, and branch strategy.

## 🔧 Tech Stack

- **Git** — branching strategy (main, develop, feature branches)
- **GitHub Actions** — automated CI pipeline on every push
- **Pre-commit hooks** — code quality checks before every commit
- **pytest** — automated testing
- **flake8** — Python linting

## ✨ Features

- ✅ Professional branching strategy (main → develop → feature)
- ✅ CI pipeline runs automatically on every push
- ✅ Pre-commit hook blocks bad commits
- ✅ Automated tests with pytest
- ✅ Python linting with flake8

## 📁 Project Structure

```
gitflow-portfolio/
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI pipeline
├── src/
│   └── app.py            # Main application
├── tests/
│   └── test_app.py       # Automated tests
├── .pre-commit-config.yaml
└── README.md
```

## 🚀 Setup

```bash
git clone https://github.com/YOURUSERNAME/gitflow-portfolio.git
cd gitflow-portfolio
pip install pytest flake8
pytest tests/ -v
```

## 🌿 Branch Strategy

```
main     → production-ready code only
develop  → integration branch
feature/ → individual features
fix/     → bug fixes
```

## 👩‍💻 Author

**Nazneen** — Cloud Engineering Roadmap | Phase 1 Week 4
