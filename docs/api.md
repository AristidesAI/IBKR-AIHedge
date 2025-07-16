# API Reference

This document provides comprehensive API reference for the IBKR AI Hedge Fund Integration.

## Table of Contents

- [Core Classes](#core-classes)
- [Configuration Management](#configuration-management)
- [Trading Functions](#trading-functions)
- [AI Integration](#ai-integration)
- [Data Management](#data-management)
- [Risk Management](#risk-management)
- [Monitoring and Logging](#monitoring-and-logging)
- [Utilities](#utilities)
- [Error Handling](#error-handling)
- [Examples](#examples)

## Core Classes

### IBKRIntegration

Main integration class that orchestrates all components.

```python
class IBKRIntegration:
    def __init__(self, config_path: str = ".env"):
        """
        Initialize the IBKR integration.
        
        Args:
            config_path: Path to configuration file
        """
        
    def connect(self) -> bool:
        """
        Connect to Interactive Brokers.
        
        Returns:
            bool: True if connection successful
        """
        
    def disconnect(self) -> None:
        """Disconnect from Interactive Brokers."""
        
    def start_trading(self) -> None:
        """Start the automated trading process."""
        
    def stop_trading(self) -> None:
        """Stop the automated trading process."""
        
    def get_portfolio(self) -> Dict[str, Any]:
        """
        Get current portfolio information.
        
        Returns:
            Dict containing portfolio data
        """
        
    def get_positions(self) -> List[Dict[str, Any]]:
        """
        Get current positions.
        
        Returns:
            List of position dictionaries
        """
```

### AIAnalyzer

Handles AI model interactions and analysis.

```python
class AIAnalyzer:
    def __init__(self, config: Config):
        """
        Initialize AI analyzer.
        
        Args:
            config: Configuration object
        """
        
    def analyze_stock(self, symbol: str) -> Dict[str, Any]:
        """
        Analyze a single stock using AI agents.
        
        Args:
            symbol: Stock symbol to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        
    def get_trading_recommendations(self, watchlist: List[str]) -> List[Dict[str, Any]]:
        """
        Get trading recommendations for watchlist.
        
        Args:
            watchlist: List of stock symbols
            
        Returns:
            List of recommendation dictionaries
        """
        
    def run_agents(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run selected AI agents on market data.
        
        Args:
            data: Market data dictionary
            
        Returns:
            Agent analysis results
        """
```

### RiskManager

Manages trading risk and position sizing.

```python
class RiskManager:
    def __init__(self, config: Config):
        """
        Initialize risk manager.
        
        Args:
            config: Configuration object
        """
        
    def validate_trade(self, trade: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Validate a proposed trade.
        
        Args:
            trade: Trade dictionary
            
        Returns:
            Tuple of (is_valid, reason)
        """
        
    def calculate_position_size(self, symbol: str, price: float, portfolio_value: float) -> int:
        """
        Calculate optimal position size.
        
        Args:
            symbol: Stock symbol
            price: Current stock price
            portfolio_value: Total portfolio value
            
        Returns:
            Number of shares to trade
        """
        
    def check_portfolio_risk(self, portfolio: Dict[str, Any]) -> Dict[str, Any]:
        """
        Check overall portfolio risk metrics.
        
        Args:
            portfolio: Current portfolio
            
        Returns:
            Risk metrics dictionary
        """
```

## Configuration Management

### Config

Configuration management class.

```python
class Config:
    def __init__(self, config_path: str = ".env"):
        """
        Initialize configuration.
        
        Args:
            config_path: Path to configuration file
        """
        
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        
    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value.
        
        Args:
            key: Configuration key
            value: Value to set
        """
        
    def validate(self) -> Tuple[bool, List[str]]:
        """
        Validate configuration.
        
        Returns:
            Tuple of (is_valid, error_messages)
        """
        
    def get_trading_params(self) -> Dict[str, Any]:
        """
        Get trading parameters.
        
        Returns:
            Dictionary of trading parameters
        """
        
    def get_ai_config(self) -> Dict[str, Any]:
        """
        Get AI configuration.
        
        Returns:
            Dictionary of AI configuration
        """
```

## Trading Functions

### place_order

```python
def place_order(
    symbol: str,
    action: str,
    quantity: int,
    order_type: str = "MKT",
    price: float = None,
    stop_price: float = None
) -> Dict[str, Any]:
    """
    Place a trading order.
    
    Args:
        symbol: Stock symbol
        action: "BUY" or "SELL"
        quantity: Number of shares
        order_type: Order type ("MKT", "LMT", "STP")
        price: Limit price (for limit orders)
        stop_price: Stop price (for stop orders)
        
    Returns:
        Dictionary containing order information
    """
```

### cancel_order

```python
def cancel_order(order_id: int) -> bool:
    """
    Cancel an existing order.
    
    Args:
        order_id: Order ID to cancel
        
    Returns:
        True if successful
    """
```

### get_market_data

```python
def get_market_data(symbols: List[str]) -> Dict[str, Dict[str, Any]]:
    """
    Get real-time market data.
    
    Args:
        symbols: List of stock symbols
        
    Returns:
        Dictionary of market data by symbol
    """
```

### get_historical_data

```python
def get_historical_data(
    symbol: str,
    duration: str = "1 D",
    bar_size: str = "1 min",
    what_to_show: str = "TRADES"
) -> pd.DataFrame:
    """
    Get historical market data.
    
    Args:
        symbol: Stock symbol
        duration: Data duration
        bar_size: Bar size
        what_to_show: Data type
        
    Returns:
        DataFrame containing historical data
    """
```

## AI Integration

### OpenAI Integration

```python
class OpenAIProvider:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        """
        Initialize OpenAI provider.
        
        Args:
            api_key: OpenAI API key
            model: Model name to use
        """
        
    def generate_analysis(self, prompt: str, context: Dict[str, Any]) -> str:
        """
        Generate AI analysis.
        
        Args:
            prompt: Analysis prompt
            context: Market context data
            
        Returns:
            AI analysis text
        """
        
    def get_trading_decision(self, analysis: str) -> Dict[str, Any]:
        """
        Get trading decision from analysis.
        
        Args:
            analysis: AI analysis text
            
        Returns:
            Trading decision dictionary
        """
```

### Agent System

```python
class TradingAgent:
    def __init__(self, name: str, description: str, provider: AIProvider):
        """
        Initialize trading agent.
        
        Args:
            name: Agent name
            description: Agent description
            provider: AI provider instance
        """
        
    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze market data.
        
        Args:
            data: Market data
            
        Returns:
            Analysis results
        """
        
    def get_recommendation(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get trading recommendation.
        
        Args:
            analysis: Analysis results
            
        Returns:
            Trading recommendation
        """
```

## Data Management

### DataManager

```python
class DataManager:
    def __init__(self, config: Config):
        """
        Initialize data manager.
        
        Args:
            config: Configuration object
        """
        
    def store_trade(self, trade: Dict[str, Any]) -> None:
        """
        Store trade data.
        
        Args:
            trade: Trade information
        """
        
    def store_analysis(self, analysis: Dict[str, Any]) -> None:
        """
        Store analysis results.
        
        Args:
            analysis: Analysis results
        """
        
    def get_trade_history(self, start_date: str = None, end_date: str = None) -> List[Dict[str, Any]]:
        """
        Get trade history.
        
        Args:
            start_date: Start date filter
            end_date: End date filter
            
        Returns:
            List of trade records
        """
        
    def get_performance_metrics(self) -> Dict[str, Any]:
        """
        Get performance metrics.
        
        Returns:
            Performance metrics dictionary
        """
```

## Risk Management

### Position Sizing

```python
def calculate_kelly_criterion(
    win_rate: float,
    avg_win: float,
    avg_loss: float
) -> float:
    """
    Calculate Kelly criterion for position sizing.
    
    Args:
        win_rate: Winning percentage
        avg_win: Average winning amount
        avg_loss: Average losing amount
        
    Returns:
        Kelly criterion percentage
    """
```

### Risk Metrics

```python
def calculate_var(returns: List[float], confidence: float = 0.95) -> float:
    """
    Calculate Value at Risk.
    
    Args:
        returns: List of returns
        confidence: Confidence level
        
    Returns:
        VaR value
    """
    
def calculate_sharpe_ratio(returns: List[float], risk_free_rate: float = 0.02) -> float:
    """
    Calculate Sharpe ratio.
    
    Args:
        returns: List of returns
        risk_free_rate: Risk-free rate
        
    Returns:
        Sharpe ratio
    """
    
def calculate_max_drawdown(portfolio_values: List[float]) -> float:
    """
    Calculate maximum drawdown.
    
    Args:
        portfolio_values: List of portfolio values
        
    Returns:
        Maximum drawdown percentage
    """
```

## Monitoring and Logging

### Logger

```python
class TradingLogger:
    def __init__(self, config: Config):
        """
        Initialize trading logger.
        
        Args:
            config: Configuration object
        """
        
    def log_trade(self, trade: Dict[str, Any]) -> None:
        """
        Log trade information.
        
        Args:
            trade: Trade data
        """
        
    def log_analysis(self, analysis: Dict[str, Any]) -> None:
        """
        Log analysis results.
        
        Args:
            analysis: Analysis results
        """
        
    def log_error(self, error: Exception, context: Dict[str, Any] = None) -> None:
        """
        Log error information.
        
        Args:
            error: Exception object
            context: Additional context
        """
        
    def get_logs(self, level: str = "INFO", limit: int = 100) -> List[Dict[str, Any]]:
        """
        Get log entries.
        
        Args:
            level: Log level filter
            limit: Maximum number of entries
            
        Returns:
            List of log entries
        """
```

### Performance Monitor

```python
class PerformanceMonitor:
    def __init__(self, config: Config):
        """
        Initialize performance monitor.
        
        Args:
            config: Configuration object
        """
        
    def track_trade(self, trade: Dict[str, Any]) -> None:
        """
        Track trade performance.
        
        Args:
            trade: Trade information
        """
        
    def get_daily_performance(self) -> Dict[str, Any]:
        """
        Get daily performance metrics.
        
        Returns:
            Daily performance data
        """
        
    def get_portfolio_metrics(self) -> Dict[str, Any]:
        """
        Get portfolio performance metrics.
        
        Returns:
            Portfolio metrics
        """
        
    def generate_report(self) -> str:
        """
        Generate performance report.
        
        Returns:
            Performance report text
        """
```

## Utilities

### Market Data Utilities

```python
def validate_symbol(symbol: str) -> bool:
    """
    Validate stock symbol format.
    
    Args:
        symbol: Stock symbol
        
    Returns:
        True if valid
    """
    
def is_market_open(timezone: str = "US/Eastern") -> bool:
    """
    Check if market is currently open.
    
    Args:
        timezone: Market timezone
        
    Returns:
        True if market is open
    """
    
def get_next_trading_day(date: datetime = None) -> datetime:
    """
    Get next trading day.
    
    Args:
        date: Reference date
        
    Returns:
        Next trading day
    """
```

### Data Processing

```python
def normalize_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize market data.
    
    Args:
        data: Market data DataFrame
        
    Returns:
        Normalized DataFrame
    """
    
def calculate_indicators(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate technical indicators.
    
    Args:
        data: OHLCV data
        
    Returns:
        DataFrame with indicators
    """
```

## Error Handling

### Exception Classes

```python
class IBKRConnectionError(Exception):
    """Raised when IBKR connection fails."""
    pass

class InvalidConfigurationError(Exception):
    """Raised when configuration is invalid."""
    pass

class TradingError(Exception):
    """Raised when trading operation fails."""
    pass

class AIAnalysisError(Exception):
    """Raised when AI analysis fails."""
    pass

class RiskViolationError(Exception):
    """Raised when risk limits are violated."""
    pass
```

### Error Handling Decorators

```python
def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
    """
    Decorator to retry function on failure.
    
    Args:
        max_retries: Maximum retry attempts
        delay: Delay between retries
    """
    
def log_errors(logger: TradingLogger):
    """
    Decorator to log function errors.
    
    Args:
        logger: Logger instance
    """
```

## Examples

### Basic Usage

```python
# Initialize integration
integration = IBKRIntegration()

# Connect to IBKR
if integration.connect():
    print("Connected successfully!")
    
    # Get portfolio
    portfolio = integration.get_portfolio()
    print(f"Portfolio value: {portfolio['total_value']}")
    
    # Start trading
    integration.start_trading()
    
    # Stop trading (when done)
    integration.stop_trading()
    
    # Disconnect
    integration.disconnect()
```

### Manual Trading

```python
# Place a market order
order = place_order(
    symbol="AAPL",
    action="BUY",
    quantity=100,
    order_type="MKT"
)

# Place a limit order
limit_order = place_order(
    symbol="GOOGL",
    action="SELL",
    quantity=50,
    order_type="LMT",
    price=150.00
)

# Cancel an order
cancel_order(order['order_id'])
```

### AI Analysis

```python
# Initialize AI analyzer
analyzer = AIAnalyzer(config)

# Analyze a stock
analysis = analyzer.analyze_stock("AAPL")
print(f"Analysis: {analysis}")

# Get recommendations for watchlist
recommendations = analyzer.get_trading_recommendations(["AAPL", "GOOGL", "MSFT"])
for rec in recommendations:
    print(f"{rec['symbol']}: {rec['action']} - {rec['confidence']}")
```

### Risk Management

```python
# Initialize risk manager
risk_manager = RiskManager(config)

# Validate a trade
trade = {
    'symbol': 'AAPL',
    'action': 'BUY',
    'quantity': 100,
    'price': 150.00
}

is_valid, reason = risk_manager.validate_trade(trade)
if is_valid:
    print("Trade approved")
else:
    print(f"Trade rejected: {reason}")

# Calculate position size
position_size = risk_manager.calculate_position_size("AAPL", 150.00, 10000.00)
print(f"Recommended position size: {position_size} shares")
```

### Performance Monitoring

```python
# Initialize performance monitor
monitor = PerformanceMonitor(config)

# Get daily performance
daily_perf = monitor.get_daily_performance()
print(f"Daily P&L: {daily_perf['pnl']}")

# Get portfolio metrics
metrics = monitor.get_portfolio_metrics()
print(f"Sharpe Ratio: {metrics['sharpe_ratio']}")
print(f"Max Drawdown: {metrics['max_drawdown']}")

# Generate report
report = monitor.generate_report()
print(report)
```

## Testing

### Unit Tests

```python
import unittest
from unittest.mock import Mock, patch

class TestIBKRIntegration(unittest.TestCase):
    def setUp(self):
        self.config = Mock()
        self.integration = IBKRIntegration()
        
    def test_connection(self):
        with patch('ibkr_integration.IBApi') as mock_api:
            result = self.integration.connect()
            self.assertTrue(result)
            
    def test_place_order(self):
        order = place_order("AAPL", "BUY", 100)
        self.assertIsNotNone(order['order_id'])
        
if __name__ == '__main__':
    unittest.main()
```

### Integration Tests

```python
def test_full_trading_cycle():
    """Test complete trading cycle."""
    integration = IBKRIntegration()
    
    # Connect
    assert integration.connect()
    
    # Get market data
    data = get_market_data(["AAPL"])
    assert "AAPL" in data
    
    # Place order
    order = place_order("AAPL", "BUY", 1)
    assert order['status'] == 'submitted'
    
    # Check position
    positions = integration.get_positions()
    assert len(positions) > 0
    
    # Clean up
    integration.disconnect()
```

## Best Practices

1. **Error Handling**: Always wrap API calls in try-except blocks
2. **Logging**: Log all trading activities for audit trail
3. **Validation**: Validate all inputs before processing
4. **Testing**: Write comprehensive tests for all components
5. **Documentation**: Document all custom functions and classes
6. **Performance**: Monitor API rate limits and response times
7. **Security**: Never log sensitive information like API keys

---

For more examples and detailed usage, see the [Trading Guide](trading.md) and [Configuration Guide](configuration.md). 