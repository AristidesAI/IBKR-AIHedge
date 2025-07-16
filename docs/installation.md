# Installation Guide

This guide provides detailed installation instructions for the IBKR AI Hedge Fund Integration.

## Table of Contents

- [System Requirements](#system-requirements)
- [Python Environment Setup](#python-environment-setup)
- [Interactive Brokers Setup](#interactive-brokers-setup)
- [Project Installation](#project-installation)
- [API Keys Setup](#api-keys-setup)
- [Configuration](#configuration)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## System Requirements

### Operating System Support

- **Windows**: Windows 10/11 (64-bit)
- **macOS**: macOS 10.15 (Catalina) or later
- **Linux**: Ubuntu 18.04+, CentOS 7+, or equivalent

### Hardware Requirements

- **RAM**: Minimum 4GB, recommended 8GB+
- **Storage**: At least 2GB free space
- **Network**: Stable internet connection for real-time data
- **CPU**: Modern multi-core processor recommended

### Software Dependencies

- **Python**: 3.8 or higher
- **pip**: Latest version
- **git**: For repository cloning
- **Interactive Brokers TWS/IB Gateway**: Latest version

## Python Environment Setup

### 1. Install Python

#### Windows
```bash
# Download from python.org or use chocolatey
choco install python

# Verify installation
python --version
pip --version
```

#### macOS
```bash
# Using Homebrew
brew install python

# Or download from python.org
# Verify installation
python3 --version
pip3 --version
```

#### Linux (Ubuntu/Debian)
```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv ibkr_env

# Activate virtual environment
# Windows
ibkr_env\Scripts\activate

# macOS/Linux
source ibkr_env/bin/activate

# Verify activation (should show virtual environment name)
which python
```

### 3. Upgrade pip
```bash
pip install --upgrade pip
```

## Interactive Brokers Setup

### 1. Create IBKR Account

1. Visit [Interactive Brokers](https://www.interactivebrokers.com/)
2. Click "Open Account"
3. Choose account type (Individual/Joint/Corporate)
4. Complete application process
5. Fund your account (minimum varies by region)

### 2. Download TWS or IB Gateway

#### Option A: Trader Workstation (TWS)
- Full trading platform with GUI
- Download from [IBKR TWS](https://www.interactivebrokers.com/en/trading/tws.php)
- Better for beginners and monitoring

#### Option B: IB Gateway
- Lightweight API-only interface
- Download from [IBKR Gateway](https://www.interactivebrokers.com/en/trading/ibgateway-stable.php)
- Better for automated trading

### 3. Configure API Settings

1. **Open TWS/IB Gateway**
2. **Navigate to Configuration**:
   - TWS: File → Global Configuration → API → Settings
   - IB Gateway: Configure → Settings → API
3. **Enable API Access**:
   - ✅ Enable ActiveX and Socket Clients
   - ✅ Allow connections from localhost
   - ❌ Read-Only API (uncheck for trading)
4. **Set Socket Port**:
   - Paper Trading: `7497`
   - Live Trading: `7496`
5. **Add Trusted IPs**: `127.0.0.1`
6. **Click Apply and OK**

### 4. Switch to Paper Trading (Recommended)

1. In TWS: Account → Trade → Paper Trading
2. In IB Gateway: Select "Paper Trading" during login
3. Verify paper trading mode is active

## Project Installation

### 1. Clone Repository

```bash
# Clone the main repository
git clone https://github.com/aristideslintzeris/ibkr-ai-hedge-fund.git
cd ibkr-ai-hedge-fund

# Clone AI-Hedge-Fund dependency
git clone https://github.com/virattt/ai-hedge-fund.git
```

### 2. Install Dependencies

```bash
# Install main dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install -r requirements-dev.txt
```

### 3. Verify Installation

```bash
# Check if key packages are installed
python -c "import ibapi; print('IBKR API installed successfully')"
python -c "import pandas; print('Pandas installed successfully')"
python -c "import openai; print('OpenAI installed successfully')"
```

## API Keys Setup

### 1. OpenAI API Key (Required)

1. Visit [OpenAI API](https://platform.openai.com/api-keys)
2. Create an account or sign in
3. Navigate to "API Keys"
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)

### 2. Financial Datasets API Key (Required)

1. Visit [Financial Datasets](https://financialdatasets.ai/)
2. Create an account
3. Navigate to API section
4. Generate API key
5. Copy the key

### 3. Optional API Keys

#### Anthropic (Claude)
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Create account and get API key

#### Groq
1. Visit [Groq Console](https://console.groq.com/)
2. Create account and get API key

#### Google (Gemini)
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create project and get API key

## Configuration

### 1. Create Environment File

```bash
# Copy template
cp env.template .env

# Edit with your preferred editor
nano .env
# or
vim .env
# or
code .env
```

### 2. Basic Configuration

```env
# IBKR Connection
IBKR_HOST=127.0.0.1
IBKR_PORT=7497
IBKR_CLIENT_ID=123

# Trading Settings
INITIAL_CASH=10000.0
CURRENCY=USD
MAX_POSITION_SIZE=0.2
MAX_DAILY_TRADES=10

# API Keys
OPENAI_API_KEY=sk-your-openai-key-here
FINANCIAL_DATASETS_API_KEY=your-financial-datasets-key
```

### 3. Market-Specific Configuration

Choose your target market and update accordingly:

#### US Market
```env
CURRENCY=USD
MARKET_TIMEZONE=US/Eastern
TRADING_SCHEDULE=09:30
WATCHLIST=AAPL,GOOGL,MSFT,AMZN,TSLA
```

#### European Market
```env
CURRENCY=EUR
MARKET_TIMEZONE=Europe/London
TRADING_SCHEDULE=09:00
WATCHLIST=ASML,SAP,LVMH,NESN,NOVN
```

#### Australian Market
```env
CURRENCY=AUD
MARKET_TIMEZONE=Australia/Sydney
TRADING_SCHEDULE=09:00
WATCHLIST=CBA,BHP,CSL,WBC,ANZ
```

## Verification

### 1. Test Configuration

```bash
# Test configuration file
python config.py

# Should output:
# ✅ Configuration loaded successfully
# ✅ API keys validated
# ✅ Trading parameters set
```

### 2. Test IBKR Connection

```bash
# Test IBKR connection (ensure TWS/Gateway is running)
python -c "
from ibkr_integration import test_connection
test_connection()
"

# Should output:
# ✅ Connected to IBKR successfully
# ✅ Paper trading mode confirmed
# ✅ Account information retrieved
```

### 3. Test AI Integration

```bash
# Test AI models
python -c "
from ibkr_integration import test_ai_models
test_ai_models()
"

# Should output:
# ✅ OpenAI API connection successful
# ✅ AI models responding correctly
# ✅ Financial data API working
```

## Troubleshooting

### Common Installation Issues

#### Python Version Issues
```bash
# If python command doesn't work, try python3
python3 --version
pip3 install -r requirements.txt
```

#### Permission Errors (Linux/macOS)
```bash
# Use --user flag for pip
pip install --user -r requirements.txt

# Or fix permissions
sudo chown -R $USER:$USER ~/.local/lib/python3.*/site-packages
```

#### Virtual Environment Issues
```bash
# If virtual environment doesn't activate
python -m venv --clear ibkr_env
source ibkr_env/bin/activate  # Linux/macOS
ibkr_env\Scripts\activate     # Windows
```

### IBKR Connection Issues

#### Port Already in Use
```bash
# Check what's using the port
netstat -an | grep 7497

# Kill process using port (if needed)
# Linux/macOS
sudo lsof -ti:7497 | xargs kill -9

# Windows
netstat -ano | findstr 7497
taskkill /PID <PID> /F
```

#### API Not Enabled
1. Restart TWS/IB Gateway
2. Re-check API settings
3. Ensure paper trading is selected
4. Try different client ID

### API Key Issues

#### Invalid OpenAI Key
```bash
# Test OpenAI key manually
python -c "
import openai
openai.api_key = 'your-key-here'
print(openai.models.list())
"
```

#### Rate Limiting
- Check API quotas in respective dashboards
- Implement delays between requests
- Consider upgrading API plans

### Dependency Issues

#### Package Conflicts
```bash
# Create fresh virtual environment
deactivate
rm -rf ibkr_env
python -m venv ibkr_env
source ibkr_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### Missing System Dependencies

#### Linux
```bash
sudo apt install build-essential python3-dev
```

#### macOS
```bash
xcode-select --install
```

## Next Steps

After successful installation:

1. **Read the [Configuration Guide](configuration.md)**
2. **Review [Trading Guide](trading.md)**
3. **Start with paper trading**
4. **Monitor logs and performance**
5. **Gradually increase position sizes**

## Getting Help

- **GitHub Issues**: Report installation problems
- **Twitter**: [@aristidesai](https://x.com/aristidesai)
- **Documentation**: Check other guides in `/docs`
- **Community**: GitHub Discussions

---

**Remember**: Always start with paper trading and never risk more than you can afford to lose. 