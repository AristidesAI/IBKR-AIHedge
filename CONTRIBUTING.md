# Contributing to IBKR AI Hedge Fund Integration

We welcome contributions to the IBKR AI Hedge Fund Integration project! This guide will help you get started with contributing to our project.

## 🤝 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Interactive Brokers account (paper trading recommended for testing)
- Required API keys (OpenAI, Financial Datasets)

### Setting Up Development Environment

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/ibkr-ai-hedge-fund.git
   cd ibkr-ai-hedge-fund
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Configure environment**
   ```bash
   cp env.template .env
   # Edit .env with your configuration
   ```

## 📋 How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Clear description** of the issue
- **Steps to reproduce** the problem
- **Expected behavior** vs actual behavior
- **Environment details** (Python version, OS, etc.)
- **Log files** if applicable
- **Screenshots** if helpful

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Clear description** of the enhancement
- **Use case** - why would this be useful?
- **Possible implementation** approach
- **Examples** of how it would work

### Pull Requests

1. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes**
   - Follow the coding standards
   - Add tests for new functionality
   - Update documentation as needed
   - Ensure all tests pass

3. **Commit your changes**
   ```bash
   git commit -m "feat: add amazing feature"
   ```

4. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```

5. **Open a Pull Request**
   - Provide a clear title and description
   - Reference any related issues
   - Include screenshots if applicable

## 🎯 Development Guidelines

### Code Style

We use [Black](https://black.readthedocs.io/) for code formatting and [flake8](https://flake8.pycqa.org/) for linting.

```bash
# Format code
black .

# Check linting
flake8 .

# Type checking
mypy .
```

### Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Build process or auxiliary tool changes

Examples:
```
feat: add support for European markets
fix: resolve connection timeout issue
docs: update installation instructions
```

### Testing

- Write tests for new functionality
- Ensure existing tests still pass
- Test with paper trading before live trading
- Include unit tests and integration tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_integration.py

# Run with coverage
python -m pytest --cov=src
```

### Documentation

- Update docstrings for new functions/classes
- Update README.md if needed
- Add examples for new features
- Keep documentation clear and concise

## 📁 Project Structure

```
ibkr-ai-hedge-fund/
├── src/
│   ├── __init__.py
│   ├── ibkr_integration.py
│   ├── config.py
│   ├── models/
│   ├── utils/
│   └── tests/
├── docs/
├── scripts/
├── requirements.txt
├── requirements-dev.txt
├── .env.template
├── .gitignore
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

## 🔧 Areas for Contribution

### High Priority

- **Market Support**: Add support for additional stock exchanges
- **Risk Management**: Enhance risk management algorithms
- **Performance**: Optimize API calls and data processing
- **Documentation**: Improve setup guides and examples

### Medium Priority

- **UI/Dashboard**: Web-based monitoring interface
- **Backtesting**: Enhanced backtesting capabilities
- **Notifications**: Email/SMS/Slack notifications
- **Database**: Better data storage and retrieval

### Good for Beginners

- **Code Quality**: Add type hints, improve docstrings
- **Testing**: Write unit tests for existing functions
- **Documentation**: Fix typos, add examples
- **Logging**: Improve logging messages

## 🧪 Testing Guidelines

### Test Categories

1. **Unit Tests**: Test individual functions/classes
2. **Integration Tests**: Test IBKR API integration
3. **End-to-End Tests**: Test complete workflows
4. **Paper Trading Tests**: Test with real market data

### Test Structure

```python
def test_function_name():
    # Arrange
    setup_test_data()
    
    # Act
    result = function_under_test()
    
    # Assert
    assert result == expected_result
```

### Mock External Dependencies

```python
@patch('src.ibkr_integration.IBApi')
def test_connection(mock_ibapi):
    # Test logic here
    pass
```

## 📊 Performance Considerations

- **API Rate Limits**: Respect IBKR API rate limits
- **Memory Usage**: Optimize data structures for large datasets
- **Concurrent Processing**: Use async/await for I/O operations
- **Caching**: Cache frequently accessed data

## 🛡️ Security Guidelines

- **API Keys**: Never commit API keys to version control
- **Sensitive Data**: Use environment variables for configuration
- **Trading Safety**: Always test with paper trading first
- **Code Review**: All PRs require code review

## 🐛 Debugging Tips

### Common Issues

1. **Connection Problems**
   - Check TWS/IB Gateway is running
   - Verify API settings
   - Check firewall settings

2. **API Errors**
   - Verify API keys are correct
   - Check API quotas/limits
   - Review error logs

3. **Trading Issues**
   - Confirm paper trading mode
   - Check account permissions
   - Verify market hours

### Debug Tools

```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Use pdb for debugging
import pdb; pdb.set_trace()

# Profile performance
import cProfile
cProfile.run('main_function()')
```

## 📚 Resources

### Documentation

- [Interactive Brokers API](https://interactivebrokers.github.io/tws-api/)
- [AI-Hedge-Fund](https://github.com/virattt/ai-hedge-fund)
- [Python Best Practices](https://docs.python.org/3/tutorial/)

### Tools

- [Black](https://black.readthedocs.io/) - Code formatting
- [flake8](https://flake8.pycqa.org/) - Linting
- [mypy](https://mypy.readthedocs.io/) - Type checking
- [pytest](https://docs.pytest.org/) - Testing

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Hall of Fame (for significant contributions)

## 📞 Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Documentation**: Check existing documentation first

## 📝 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to IBKR AI Hedge Fund Integration! 🚀 