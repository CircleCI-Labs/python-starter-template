# Python Starter Template

A standardized Python project template for [Your Organization].

## Overview
This repository provides a solid foundation for new Python projects, enforcing best practices, code quality, and a modern CI/CD workflow using CircleCI.

## Features
- Modern Python packaging (PEP 517/518)
- Pre-commit hooks for linting and formatting
- Unit testing with pytest
- Docker support for containerized builds
- Team-specific CircleCI configuration via `.circleci/team-config.yml`

## Getting Started

### Prerequisites
- Python 3.9+
- [pip](https://pip.pypa.io/en/stable/)
- [Docker](https://www.docker.com/) (optional, for container builds)

### Installation
```bash
python -m venv venv
source venv/bin/activate
# If you get errors about missing pip, run:
python -m ensurepip --upgrade
pip install --upgrade pip setuptools
pip install -r requirements.txt
pip install -r requirements-dev.txt
# Install the package in editable mode (required for running the CLI)
pip install -e .
```

> **Note:** Editable installs (`pip install -e .`) require a `setup.py` file for compatibility with some pip/setuptools versions. This template includes a minimal `setup.py` for this purpose.

### Running the Application
```bash
python -m starter_template hello
python -m starter_template build
```

### Running Tests
To run all tests using pytest:
```bash
pytest
```

You should see output indicating that the sample tests in the `tests/` directory have run and passed.

### Linting & Formatting
```bash
pre-commit run --all-files
```

### Building the Docker Image
```bash
docker build -t starter-template:latest .
```

## CI/CD with CircleCI
This project uses a **centralized CircleCI configuration** managed by the platform team.
- The main pipeline config [`config.yml`](https://github.com/CircleCI-Labs/platform-team-configs/blob/main/config-templates/python/config.yml) is maintained in a separate repo and referenced by all projects.
- This repo contains a [`.circleci/team-config.yml`](.circleci/team-config.yml) file, which you can use to override or extend jobs/workflows for your team's needs.
- For more information, see [Platform Team CI/CD Docs](https://github.com/CircleCI-Labs/platform-team-configs).

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Disclaimer

CircleCI Labs is a collection of solutions developed by members of CircleCI's Field Engineering team through our engagement with various customer needs. This repository is part of that collection.

-   ✅ Created by engineers @ CircleCI
-   ✅ Used by real CircleCI customers
-   ❌ **not** officially supported by CircleCI support

## License
See [LICENSE](LICENSE) for details.

---

> _Replace this text with project-specific details as needed._
