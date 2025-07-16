# IBKR AI Hedge Fund Integration

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-black)](https://black.readthedocs.io/)
[![Twitter](https://img.shields.io/badge/Twitter-@aristidesai-1DA1F2)](https://x.com/aristidesai)

An automated trading integration that connects Interactive Brokers with AI-powered financial analysis for intelligent trading decisions.

> **Created by**: [@aristides lintzeris](https://x.com/aristidesai) | **Follow for updates and trading insights**

## 🚀 Features

- **Real-time Data Processing**: Connect to Interactive Brokers API for live market data
- **AI-Powered Analysis**: Leverage multiple AI models for comprehensive market analysis
- **Automated Trading**: Execute trades based on AI recommendations with built-in risk management
- **Multi-Market Support**: Configure for any stock exchange or market worldwide
- **Risk Management**: Position sizing, stop-losses, and daily trade limits
- **Paper Trading Support**: Test strategies safely before live trading
- **Comprehensive Logging**: Track all activities and performance metrics

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Risk Management](#risk-management)
- [Monitoring](#monitoring)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Contact](#contact)
- [Disclaimer](#disclaimer)

## ⚡ Quick Start

Get up and running in 5 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/aristideslintzeris/ibkr-ai-hedge-fund.git
cd ibkr-ai-hedge-fund

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp env.template .env
# Edit .env with your API keys and settings

# 4. Start paper trading
python ibkr_integration.py
```

## 🔧 Prerequisites

### Interactive Brokers Account
- Sign up at [Interactive Brokers](https://www.interactivebrokers.com/)
- Download and install **Trader Workstation (TWS)** or **IB Gateway**
- **Recommended**: Start with paper trading for testing

### Python Environment
- Python 3.8 or higher
- pip package manager

### API Keys (Required)
- **OpenAI API Key**: For GPT models
- **Financial Datasets API Key**: For market data
- **Optional**: Additional model providers (Anthropic, Groq, DeepSeek, Google)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/aristideslintzeris/ibkr-ai-hedge-fund.git
cd ibkr-ai-hedge-fund
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Clone AI-Hedge-Fund Repository
```bash
git clone https://github.com/virattt/ai-hedge-fund.git
```

### 4. Configure Environment
```bash
cp env.template .env
```

## ⚙️ Configuration

### Environment Variables

Edit your `.env` file with the following configurations:

```env
# IBKR Connection Settings
IBKR_HOST=127.0.0.1
IBKR_PORT=7497              # 7497 for paper trading, 7496 for live
IBKR_CLIENT_ID=123

# Trading Settings
INITIAL_CASH=10000.0        # Starting capital (adjust to your preference)
CURRENCY=USD                # USD, EUR, GBP, AUD, CAD, etc.
MAX_POSITION_SIZE=0.2       # Maximum 20% per position
MAX_DAILY_TRADES=10         # Maximum trades per day
STOP_LOSS_PERCENTAGE=0.05   # 5% stop loss
TAKE_PROFIT_PERCENTAGE=0.10 # 10% take profit

# Market Settings
MARKET_TIMEZONE=US/Eastern  # Your market timezone
TRADING_SCHEDULE=09:30      # Daily analysis time (24-hour format)

# Watchlist (comma-separated stock symbols)
WATCHLIST=AAPL,GOOGL,MSFT,AMZN,TSLA,NVDA,META,NFLX,BABA,V

# AI Model Configuration
PRIMARY_MODEL=gpt-4o-mini
BACKUP_MODELS=gpt-3.5-turbo,claude-3-haiku

# API Keys (REQUIRED)
OPENAI_API_KEY=your-openai-api-key
FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key

# Optional AI Model Providers
ANTHROPIC_API_KEY=your-anthropic-api-key
GROQ_API_KEY=your-groq-api-key
DEEPSEEK_API_KEY=your-deepseek-api-key
GOOGLE_API_KEY=your-google-api-key

# Logging
LOG_LEVEL=INFO              # DEBUG, INFO, WARNING, ERROR
LOG_FILE=ibkr_hedge_fund.log
```

### Market-Specific Examples

<details>
<summary>🇺🇸 US Market Configuration</summary>

```env
CURRENCY=USD
MARKET_TIMEZONE=US/Eastern
TRADING_SCHEDULE=09:30
WATCHLIST=AAPL,GOOGL,MSFT,AMZN,TSLA,NVDA,META,NFLX,JPM,JNJ
```
</details>

<details>
<summary>🇪🇺 European Market Configuration</summary>

```env
CURRENCY=EUR
MARKET_TIMEZONE=Europe/London
TRADING_SCHEDULE=09:00
WATCHLIST=ASML,SAP,LVMH,NESN,NOVN,ROG,OR,SAN,INGA,PHIA
```
</details>

<details>
<summary>🇦🇺 Australian Market Configuration</summary>

```env
CURRENCY=AUD
MARKET_TIMEZONE=Australia/Sydney
TRADING_SCHEDULE=09:00
WATCHLIST=CBA,BHP,CSL,WBC,ANZ,NAB,WOW,TLS,RIO,MQG
```
</details>

<details>
<summary>🇯🇵 Japanese Market Configuration</summary>

```env
CURRENCY=JPY
MARKET_TIMEZONE=Asia/Tokyo
TRADING_SCHEDULE=09:00
WATCHLIST=7203,6758,6861,8411,9984,4661,6098,9432,8001,8031
```
</details>

### IBKR Configuration

1. **Open TWS/IB Gateway**
2. **Navigate to API Settings**:
   - File → Global Configuration → API → Settings
3. **Enable API**:
   - ✅ Enable ActiveX and Socket Clients
   - ✅ Read-Only API (uncheck for trading)
4. **Set Port**:
   - Paper Trading: `7497`
   - Live Trading: `7496`
5. **Add Trusted IPs**: `127.0.0.1`

## 🚀 Usage

### Quick Start

1. **Validate Configuration**:
```bash
python config.py
```

2. **Start Paper Trading**:
```bash
python ibkr_integration.py
```

3. **Monitor Logs**:
```bash
tail -f ibkr_hedge_fund.log
```

### Advanced Usage

#### Custom Watchlist
```python
# In your .env file
WATCHLIST=AAPL,GOOGL,MSFT,AMZN,TSLA

# Or modify in config.py
WATCHLIST = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
```

#### Scheduling Options
```python
# Daily at 9:30 AM
TRADING_SCHEDULE=09:30

# Multiple times per day (comma-separated)
TRADING_SCHEDULE=09:30,14:00,16:00

# Weekly on specific days
TRADING_SCHEDULE=Monday:09:30,Wednesday:09:30,Friday:09:30
```

#### Risk Management Profiles

<details>
<summary>Conservative Profile</summary>

```env
MAX_POSITION_SIZE=0.1       # 10% max per position
MAX_DAILY_TRADES=5
STOP_LOSS_PERCENTAGE=0.03   # 3% stop loss
TAKE_PROFIT_PERCENTAGE=0.06 # 6% take profit
```
</details>

<details>
<summary>Moderate Profile</summary>

```env
MAX_POSITION_SIZE=0.15      # 15% max per position
MAX_DAILY_TRADES=8
STOP_LOSS_PERCENTAGE=0.05   # 5% stop loss
TAKE_PROFIT_PERCENTAGE=0.10 # 10% take profit
```
</details>

<details>
<summary>Aggressive Profile</summary>

```env
MAX_POSITION_SIZE=0.25      # 25% max per position
MAX_DAILY_TRADES=15
STOP_LOSS_PERCENTAGE=0.08   # 8% stop loss
TAKE_PROFIT_PERCENTAGE=0.15 # 15% take profit
```
</details>

## 🛡️ Risk Management

### Built-in Safety Features

- **Position Sizing**: Automatic position size calculation based on portfolio percentage
- **Stop Losses**: Configurable stop-loss orders for all positions
- **Daily Limits**: Maximum number of trades per day
- **Portfolio Limits**: Maximum allocation per security
- **Paper Trading**: Safe testing environment

### Risk Monitoring

```python
# Check current risk metrics
python -c "from ibkr_integration import get_portfolio_metrics; print(get_portfolio_metrics())"
```

## 📊 Monitoring

### Real-time Monitoring

The integration provides comprehensive monitoring through:

- **Log Files**: Detailed activity logging
- **Portfolio Tracking**: Real-time position updates
- **Performance Metrics**: P&L tracking and analytics
- **Error Handling**: Automatic error recovery and logging

### Dashboard (Optional)

Create a simple monitoring dashboard:

```bash
python dashboard.py
```

## 📚 Documentation

Comprehensive documentation is available in the `/docs` folder:

- **[Installation Guide](docs/installation.md)**: Detailed setup instructions
- **[Configuration Guide](docs/configuration.md)**: Complete configuration reference
- **[API Reference](docs/api.md)**: Code documentation and examples
- **[Trading Guide](docs/trading.md)**: Trading strategies and best practices
- **[Troubleshooting](docs/troubleshooting.md)**: Common issues and solutions

## 🔧 Troubleshooting

### Common Issues

<details>
<summary>Connection Errors</summary>

**Issue**: Cannot connect to IBKR
```
Error: Connection failed to 127.0.0.1:7497
```

**Solution**:
1. Ensure TWS/IB Gateway is running
2. Check API settings are enabled
3. Verify correct port (7497 for paper, 7496 for live)
4. Confirm 127.0.0.1 is in trusted IPs
</details>

<details>
<summary>API Key Errors</summary>

**Issue**: Invalid API key
```
Error: OpenAI API key is invalid
```

**Solution**:
1. Verify API key in `.env` file
2. Check API key permissions
3. Confirm sufficient quota/credits
4. Test API key independently
</details>

<details>
<summary>Trading Errors</summary>

**Issue**: Order rejected
```
Error: Order rejected - insufficient funds
```

**Solution**:
1. Check account balance
2. Verify market hours
3. Confirm security permissions
4. Review position limits
</details>

### Debug Mode

Enable detailed logging:
```env
LOG_LEVEL=DEBUG
```

### Test Configuration

Run diagnostic tests:
```bash
python -m pytest tests/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📞 Contact

- **Creator**: [@aristidesai](https://x.com/aristidesai)

For project updates, trading insights, and AI developments, follow [@aristidesai](https://x.com/aristidesai) on Twitter.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

**Important**: This software is for educational purposes only. Trading involves substantial risk of loss. Always test thoroughly with paper trading before using real money. The authors and contributors are not responsible for any financial losses.

**Key Points**:
- Start with paper trading
- Test thoroughly before live trading
- Never risk more than you can afford to lose
- Understand the risks involved
- Consult with financial professionals

## 🆘 Support
Contact me on twitter for support - [@aristidesai](https://x.com/aristidesai) 
- **IBKR API**: [Official Documentation](https://interactivebrokers.github.io/tws-api/)

## 🙏 Acknowledgments

- [AI-Hedge-Fund](https://github.com/virattt/ai-hedge-fund) for the original AI analysis system
- [Interactive Brokers](https://www.interactivebrokers.com/) for the trading platform
- Contributors and the open-source community

---

Made with ❤️ by [@aristidesai](https://x.com/aristidesai) and the community 
