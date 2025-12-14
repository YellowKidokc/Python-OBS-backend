# Contributing to Theophysics Manager

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🚀 Quick Start

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/theophysics-manager.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Run tests: `python -m pytest`
6. Commit: `git commit -m "Add: your feature description"`
7. Push: `git push origin feature/your-feature-name`
8. Open a Pull Request

## 📋 Code Guidelines

### Python Style
- Follow PEP 8
- Use type hints
- Document functions with docstrings
- Keep functions focused and under 50 lines when possible

### Commit Messages
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- Reference issues when applicable: `Fix #123: description`

### Code Structure
```python
def function_name(param: str) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
    """
    # Implementation
    pass
```

## 🧪 Testing

- Write tests for new features
- Ensure existing tests pass
- Test on multiple platforms if possible

## 📝 Documentation

- Update docs/ for new features
- Add docstrings to all public functions
- Update README.md if adding user-facing features

## 🐛 Bug Reports

When filing a bug report, include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs

## 💡 Feature Requests

For feature requests, describe:
- The problem it solves
- Proposed solution
- Alternative solutions considered
- Who benefits from this feature

## 🔍 Pull Request Process

1. **Update documentation** for any changed functionality
2. **Add tests** for new features
3. **Follow code style** guidelines
4. **Keep PRs focused** - one feature per PR when possible
5. **Respond to feedback** from reviewers

### PR Checklist

- [ ] Code follows project style
- [ ] Tests added and passing
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No linter errors

## 🏗️ Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/theophysics-manager.git
cd theophysics-manager

# Install in development mode
python scripts/install.py

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linter
flake8 .
```

## 🎯 Areas to Contribute

### High Priority
- Additional AI provider integrations
- Performance optimizations
- Test coverage improvements
- Documentation improvements

### Good First Issues
- Bug fixes
- Documentation updates
- UI improvements
- New entity extraction patterns

### Advanced
- New engine modules
- Database optimizations
- Graph visualization features
- API development

## 📬 Contact

- Open an issue for bugs/features
- Email: [project-email]
- Discord: [server-link]

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Theophysics Manager! 🚀

