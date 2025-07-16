# IBKR AI Hedge Fund Integration Setup Guide

This guide walks you through setting up the IBKR AI Hedge Fund integration that connects Interactive Brokers with the AI-Hedge-Fund analysis system for automated trading.

## Overview

The integration combines:
- **Interactive Brokers API** for real-time data and trade execution
- **AI-Hedge-Fund system** for multi-agent financial analysis
- **Automated scheduling** for 24/7 operation
- **Risk management** with position sizing and stop-losses
- **Australian Stock Exchange focus** with $200 AUD starting capital

## Prerequisites

### 1. Interactive Brokers Account
- Sign up for an IBKR account at [Interactive Brokers](https://www.interactivebrokers.com/)
- **Recommended**: Start with a paper trading account for testing
- Download and install **Trader Workstation (TWS)** or **IB Gateway**

### 2. Python Environment
- Python 3.8 or higher
- Access to install packages via pip

### 3. API Keys (Required)
- **OpenAI API Key**: For GPT models
- **Financial Datasets API Key**: For market data
- **Optional**: Anthropic, Groq, DeepSeek, Google API keys for additional models

## Installation Steps

### 1. Clone the AI-Hedge-Fund Repository
```bash
git clone https://github.com/virattt/ai-hedge-fund.git
cd ai-hedge-fund
```

### 2. Install Integration Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Additional Dependencies for Integration
```bash
pip install ibapi pandas schedule python-dotenv colorlog pytz
```

### 4. Configure Environment Variables
```bash
cp env.template .env
```

Edit the `.env` file with your actual API keys and configuration:

```env
# IBKR Connection Settings
IBKR_HOST=127.0.0.1
IBKR_PORT=7497              # Paper trading port (7496 for live)
IBKR_CLIENT_ID=123

# Trading Settings
INITIAL_CASH=200.0
CURRENCY=AUD
MAX_POSITION_SIZE=0.2       # 20% max per position

# API Keys (REQUIRED)
OPENAI_API_KEY=your-openai-api-key
FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key

# Optional additional model providers
ANTHROPIC_API_KEY=your-anthropic-api-key
GROQ_API_KEY=your-groq-api-key
```

## IBKR Setup

### 1. Configure TWS/IB Gateway
1. Open Trader Workstation (TWS) or IB Gateway
2. Go to **File > Global Configuration > API > Settings**
3. Enable **Enable ActiveX and Socket Clients**
4. Set **Socket port** to `7497` (paper trading) or `7496` (live trading)
5. Add `127.0.0.1` to **Trusted IPs**
6. **Disable** "Read-Only API"

### 2. Paper Trading Setup (Recommended)
1. In TWS, go to **File > Global Configuration > API > Settings**
2. Check **Enable ActiveX and Socket Clients**
3. Set port to `7497`
4. Switch to paper trading mode in TWS

### 3. Live Trading Setup (Advanced)
⚠️ **WARNING**: Only use live trading after thorough testing with paper trading

1. Use port `7496` for live trading
2. Ensure sufficient funds in your account
3. Set appropriate risk limits
4. Test thoroughly with small amounts first

## Running the Integration

### 1. Start IBKR TWS/Gateway
Ensure TWS or IB Gateway is running and properly configured.

### 2. Test Configuration
```bash
python config.py
```

This will validate your configuration and show current settings.

### 3. Run the Integration
```bash
python ibkr_integration.py
```

The integration will:
- Connect to IBKR
- Start the scheduling system
- Run daily analysis at 9:00 AM (configurable)
- Execute trades based on AI recommendations
- Log all activities to `ibkr_hedge_fund.log`

## Configuration Options

### Trading Configuration
- **Watchlist**: ASX stocks to analyze (CBA, BHP, CSL, etc.)
- **Selected Agents**: AI agents to use for analysis
- **Risk Management**: Position sizing and stop-losses
- **Scheduling**: Daily analysis time (default: 9:00 AM AEST)

### AI Model Configuration
- **Primary Model**: GPT-4o-mini (default)
- **Backup Models**: Various providers supported
- **Analysis Depth**: Configurable agent selection

### Risk Management
- **Max Position Size**: 20% of portfolio per stock
- **Max Daily Trades**: 10 trades per day
- **Stop Loss**: 5% default
- **Take Profit**: 10% default

## Monitoring

### 1. Log Files
- **Main Log**: `ibkr_hedge_fund.log`
- **Error Tracking**: All errors logged with timestamps
- **Trade History**: All trades logged with details

### 2. Portfolio Tracking
The integration provides real-time portfolio updates:
- Current positions
- Cash balance
- Unrealized P&L
- Performance metrics

### 3. Daily Reports
Automated daily reports include:
- AI analysis results
- Trading decisions
- Portfolio performance
- Risk metrics

## Australian Stock Exchange Focus

### Watchlist (Default)
- **CBA** - Commonwealth Bank
- **BHP** - BHP Group
- **CSL** - CSL Limited
- **WBC** - Westpac Banking Corporation
- **ANZ** - ANZ Banking Group
- **NAB** - National Australia Bank
- **WOW** - Woolworths Group
- **TLS** - Telstra Corporation
- **RIO** - Rio Tinto
- **MQG** - Macquarie Group

### Trading Hours
- **Analysis Time**: 9:00 AM AEST (configurable)
- **Market Hours**: ASX trading hours (10:00 AM - 4:00 PM AEST)
- **Currency**: AUD (Australian Dollars)

## Safety Features

### 1. Risk Management
- Position size limits (20% max per stock)
- Daily trade limits
- Stop-loss protection
- Take-profit targets

### 2. Paper Trading
- Default configuration uses paper trading
- No real money at risk during testing
- Full functionality testing

### 3. Logging and Monitoring
- Comprehensive logging
- Error tracking
- Performance monitoring
- Trade history

## Troubleshooting

### Common Issues

1. **Connection Failed**
   - Check TWS/Gateway is running
   - Verify API settings enabled
   - Check port configuration (7497 for paper, 7496 for live)

2. **API Key Errors**
   - Verify all required API keys in `.env` file
   - Check API key permissions and quotas
   - Ensure keys are properly formatted

3. **Trading Errors**
   - Check account permissions
   - Verify sufficient funds
   - Check market hours

### Debug Mode
Enable debug logging by setting:
```env
LOG_LEVEL=DEBUG
```

## Next Steps

1. **Start with Paper Trading**: Always test with paper trading first
2. **Monitor Performance**: Watch the system for several days
3. **Adjust Configuration**: Tune risk parameters based on performance
4. **Scale Gradually**: If moving to live trading, start with small amounts
5. **Regular Monitoring**: Check logs and performance regularly

## Support

For issues with:
- **AI-Hedge-Fund**: Check the [original repository](https://github.com/virattt/ai-hedge-fund)
- **IBKR API**: Consult [IBKR API documentation](https://interactivebrokers.github.io/tws-api/)
- **This Integration**: Check logs and configuration settings

## Legal Disclaimer

This integration is for educational purposes only. Trading involves risk of loss. Always test thoroughly with paper trading before using real money. The authors are not responsible for any financial losses. 