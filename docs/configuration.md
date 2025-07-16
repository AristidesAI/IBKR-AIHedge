# Configuration Guide

This guide provides detailed information about configuring the IBKR AI Hedge Fund Integration.

## Table of Contents

- [Environment Variables](#environment-variables)
- [IBKR Connection Settings](#ibkr-connection-settings)
- [Trading Parameters](#trading-parameters)
- [Market Configuration](#market-configuration)
- [AI Model Configuration](#ai-model-configuration)
- [Risk Management Settings](#risk-management-settings)
- [Logging Configuration](#logging-configuration)
- [Advanced Settings](#advanced-settings)
- [Configuration Examples](#configuration-examples)
- [Validation and Testing](#validation-and-testing)

## Environment Variables

The system uses environment variables for configuration. All settings are defined in the `.env` file.

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key for AI models | `sk-...` |
| `FINANCIAL_DATASETS_API_KEY` | Financial data API key | `your-key` |
| `IBKR_HOST` | IBKR connection host | `127.0.0.1` |
| `IBKR_PORT` | IBKR connection port | `7497` |
| `IBKR_CLIENT_ID` | IBKR client identifier | `123` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Anthropic API key | None |
| `GROQ_API_KEY` | Groq API key | None |
| `GOOGLE_API_KEY` | Google API key | None |
| `DEBUG_MODE` | Enable debug mode | `false` |

## IBKR Connection Settings

### Basic Connection

```env
# IBKR Connection Settings
IBKR_HOST=127.0.0.1          # Usually localhost
IBKR_PORT=7497               # Paper: 7497, Live: 7496
IBKR_CLIENT_ID=123           # Unique client identifier
```

### Connection Parameters

#### Host Settings
- **Local Connection**: `127.0.0.1` (recommended)
- **Remote Connection**: IP address of TWS/Gateway server
- **Security**: Only use trusted networks for remote connections

#### Port Configuration
- **Paper Trading**: `7497` (default, recommended for testing)
- **Live Trading**: `7496` (use only after thorough testing)
- **Custom Ports**: Can be configured in TWS/Gateway settings

#### Client ID
- **Purpose**: Identifies your connection to IBKR
- **Range**: 1-10000 (avoid 0)
- **Uniqueness**: Each connection needs a unique ID
- **Recommendation**: Use consistent ID for stable connections

### Advanced Connection Settings

```env
# Connection timeout and retry settings
CONNECTION_TIMEOUT=30        # Seconds to wait for connection
MAX_RETRIES=3               # Maximum connection retry attempts
RETRY_DELAY=5               # Seconds between retry attempts
KEEP_ALIVE=True             # Maintain connection alive
```

## Trading Parameters

### Core Trading Settings

```env
# Trading Settings
INITIAL_CASH=10000.0         # Starting capital
CURRENCY=USD                 # Base currency
MAX_POSITION_SIZE=0.2        # 20% max per position
MAX_DAILY_TRADES=10          # Daily trade limit
STOP_LOSS_PERCENTAGE=0.05    # 5% stop loss
TAKE_PROFIT_PERCENTAGE=0.10  # 10% take profit
```

### Position Sizing

#### Maximum Position Size
- **Conservative**: 0.05-0.10 (5-10% per position)
- **Moderate**: 0.15-0.20 (15-20% per position)
- **Aggressive**: 0.25-0.30 (25-30% per position)

#### Position Calculation
```python
# Position size calculation
position_value = portfolio_value * MAX_POSITION_SIZE
shares = position_value / stock_price
```

### Risk Management

```env
# Risk Management
MAX_PORTFOLIO_VOLATILITY=0.15    # Maximum portfolio volatility
MAX_POSITION_CORRELATION=0.7     # Maximum correlation between positions
MIN_LIQUIDITY=1000000           # Minimum daily volume
MAX_DRAWDOWN=0.10               # Maximum drawdown threshold
```

### Order Configuration

```env
# Order Settings
DEFAULT_ORDER_TYPE=MKT          # Market orders (MKT, LMT, STP)
DEFAULT_TIME_IN_FORCE=DAY       # Order duration (DAY, GTC, IOC)
MIN_TRADE_INTERVAL=60           # Minimum seconds between trades
ORDER_TIMEOUT=300               # Order timeout in seconds
```

## Market Configuration

### Timezone and Schedule

```env
# Market Settings
MARKET_TIMEZONE=US/Eastern      # Market timezone
TRADING_SCHEDULE=09:30          # Daily analysis time
MARKET_HOURS_START=09:30        # Market open time
MARKET_HOURS_END=16:00          # Market close time
```

### Supported Timezones

| Market | Timezone | Trading Hours |
|--------|----------|---------------|
| US | `US/Eastern` | 09:30-16:00 |
| Europe | `Europe/London` | 08:00-16:30 |
| Australia | `Australia/Sydney` | 10:00-16:00 |
| Japan | `Asia/Tokyo` | 09:00-15:00 |
| Canada | `America/Toronto` | 09:30-16:00 |

### Watchlist Configuration

```env
# Watchlist (comma-separated)
WATCHLIST=AAPL,GOOGL,MSFT,AMZN,TSLA,NVDA,META,NFLX,BABA,V
```

#### Watchlist Guidelines
- **Diversification**: Include different sectors
- **Liquidity**: Choose highly liquid stocks
- **Market Cap**: Mix of large, mid, and small-cap stocks
- **Volatility**: Balance stable and volatile stocks
- **Maximum**: Recommend 10-20 stocks for focused analysis

### Currency Support

```env
# Currency Configuration
CURRENCY=USD                    # Base currency
EXCHANGE_RATE_API=true          # Enable currency conversion
CURRENCY_HEDGING=false          # Enable currency hedging
```

#### Supported Currencies
- **USD**: US Dollar
- **EUR**: Euro
- **GBP**: British Pound
- **AUD**: Australian Dollar
- **CAD**: Canadian Dollar
- **JPY**: Japanese Yen
- **CHF**: Swiss Franc
- **SEK**: Swedish Krona

## AI Model Configuration

### Primary Model Settings

```env
# AI Model Configuration
PRIMARY_MODEL=gpt-4o-mini       # Main AI model
BACKUP_MODELS=gpt-3.5-turbo,claude-3-haiku  # Fallback models
MAX_TOKENS=4000                 # Maximum tokens per request
TEMPERATURE=0.1                 # Response randomness (0-1)
```

### Model Selection

#### OpenAI Models
- **gpt-4o-mini**: Fast, cost-effective (recommended)
- **gpt-4-turbo**: More capable, higher cost
- **gpt-3.5-turbo**: Basic functionality, lowest cost

#### Anthropic Models
- **claude-3-haiku**: Fast, efficient
- **claude-3-sonnet**: Balanced performance
- **claude-3-opus**: Highest capability

#### Groq Models
- **llama3-70b**: Fast inference
- **mixtral-8x7b**: Good performance
- **gemma-7b**: Efficient model

### Agent Configuration

```env
# Selected AI agents for analysis
SELECTED_AGENTS=warren_buffett,valuation_analyst,sentiment_analyst,fundamentals_analyst,technical_analyst,risk_management,portfolio_management
```

#### Available Agents
- **warren_buffett**: Value investing approach
- **cathie_wood**: Growth and innovation focus
- **valuation_analyst**: DCF and intrinsic value analysis
- **sentiment_analyst**: News and market sentiment
- **fundamentals_analyst**: Financial metrics and ratios
- **technical_analyst**: Chart patterns and indicators
- **risk_management**: Portfolio risk assessment
- **portfolio_management**: Position sizing and allocation

### AI Performance Settings

```env
# AI Performance
MAX_CONCURRENT_REQUESTS=5       # Concurrent API requests
REQUEST_TIMEOUT=30              # Request timeout in seconds
RATE_LIMIT=60                   # Requests per minute
RETRY_ATTEMPTS=3                # Failed request retries
```

## Risk Management Settings

### Portfolio Risk Controls

```env
# Portfolio Risk Management
MAX_PORTFOLIO_VOLATILITY=0.15   # Maximum portfolio volatility
MAX_SECTOR_ALLOCATION=0.3       # Maximum sector allocation
MIN_DIVERSIFICATION=5           # Minimum number of positions
CORRELATION_THRESHOLD=0.7       # Maximum position correlation
```

### Position Risk Controls

```env
# Position Risk Management
MAX_POSITION_SIZE=0.2           # Maximum position size
MIN_POSITION_SIZE=0.01          # Minimum position size
POSITION_TIMEOUT=86400          # Position timeout in seconds
AUTO_REBALANCE=true             # Enable automatic rebalancing
```

### Stop Loss and Take Profit

```env
# Stop Loss Configuration
STOP_LOSS_PERCENTAGE=0.05       # 5% stop loss
TRAILING_STOP=true              # Enable trailing stops
TRAILING_STOP_PERCENTAGE=0.02   # 2% trailing stop

# Take Profit Configuration
TAKE_PROFIT_PERCENTAGE=0.10     # 10% take profit
PARTIAL_PROFITS=true            # Enable partial profit taking
PROFIT_SCALING=0.5              # Scale out 50% at target
```

## Logging Configuration

### Basic Logging

```env
# Logging Configuration
LOG_LEVEL=INFO                  # DEBUG, INFO, WARNING, ERROR
LOG_FILE=ibkr_hedge_fund.log    # Log file name
MAX_LOG_SIZE=10                 # Maximum log size in MB
LOG_BACKUP_COUNT=5              # Number of backup log files
```

### Advanced Logging

```env
# Advanced Logging
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s
LOG_ROTATION=daily              # Log rotation frequency
LOG_COMPRESSION=true            # Compress old log files
SEPARATE_ERROR_LOG=true         # Separate error log file
```

### Log Levels

- **DEBUG**: Detailed debugging information
- **INFO**: General operational information
- **WARNING**: Warning messages
- **ERROR**: Error conditions
- **CRITICAL**: Critical errors

## Advanced Settings

### Performance Optimization

```env
# Performance Settings
ENABLE_CACHING=true             # Enable data caching
CACHE_TIMEOUT=3600              # Cache timeout in seconds
PARALLEL_PROCESSING=true        # Enable parallel processing
MAX_WORKERS=4                   # Maximum worker threads
```

### Database Configuration

```env
# Database Settings
DATABASE_URL=sqlite:///trading_data.db  # Database connection
ENABLE_DATABASE=true            # Enable database logging
DATABASE_POOL_SIZE=10           # Connection pool size
DATABASE_TIMEOUT=30             # Database timeout
```

### Notification Settings

```env
# Email Notifications
ENABLE_EMAIL_NOTIFICATIONS=false
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
EMAIL_TO=your-email@gmail.com

# Slack Notifications
ENABLE_SLACK_NOTIFICATIONS=false
SLACK_WEBHOOK_URL=your-slack-webhook-url
SLACK_CHANNEL=#trading-alerts
```

## Configuration Examples

### Conservative Trading Setup

```env
# Conservative Configuration
INITIAL_CASH=5000.0
MAX_POSITION_SIZE=0.1
MAX_DAILY_TRADES=3
STOP_LOSS_PERCENTAGE=0.03
TAKE_PROFIT_PERCENTAGE=0.06
WATCHLIST=AAPL,MSFT,JNJ,KO,PG
```

### Aggressive Trading Setup

```env
# Aggressive Configuration
INITIAL_CASH=50000.0
MAX_POSITION_SIZE=0.25
MAX_DAILY_TRADES=20
STOP_LOSS_PERCENTAGE=0.08
TAKE_PROFIT_PERCENTAGE=0.15
WATCHLIST=TSLA,NVDA,AMZN,GOOGL,META,NFLX,BABA,AMD,CRM,ZM
```

### Multi-Market Setup

```env
# Multi-Market Configuration
CURRENCY=USD
MARKET_TIMEZONE=US/Eastern
TRADING_SCHEDULE=09:30,21:00
WATCHLIST=AAPL,MSFT,ASML,TSM,BABA,TM,NESN,SAP
ENABLE_CURRENCY_CONVERSION=true
```

## Validation and Testing

### Configuration Validation

```bash
# Validate configuration
python config.py --validate

# Check specific sections
python config.py --check-ibkr
python config.py --check-api-keys
python config.py --check-trading-params
```

### Test Configuration

```bash
# Test IBKR connection
python config.py --test-ibkr

# Test AI models
python config.py --test-ai

# Test full integration
python config.py --test-all
```

### Configuration Backup

```bash
# Backup current configuration
cp .env .env.backup.$(date +%Y%m%d_%H%M%S)

# Restore from backup
cp .env.backup.YYYYMMDD_HHMMSS .env
```

## Best Practices

### Security
- Never commit `.env` file to version control
- Use strong API keys and rotate them regularly
- Limit API key permissions to minimum required
- Use paper trading for testing

### Performance
- Start with conservative settings
- Monitor system resources
- Adjust concurrent requests based on capabilities
- Use caching for frequently accessed data

### Risk Management
- Always set stop losses
- Diversify across sectors and markets
- Monitor correlations between positions
- Start with small position sizes

### Monitoring
- Enable comprehensive logging
- Set up alerts for errors
- Monitor API usage and costs
- Track performance metrics

## Getting Help

- **Configuration Issues**: Check logs for error messages
- **Validation Errors**: Run configuration validation
- **API Problems**: Test API keys independently
- **Trading Issues**: Verify market hours and permissions
- **Contact**: [@aristidesai](https://x.com/aristidesai)

---

**Remember**: Always test configuration changes in paper trading mode before live trading. 