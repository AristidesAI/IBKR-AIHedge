#!/usr/bin/env python3
"""
Configuration module for IBKR AI Hedge Fund Integration
"""

import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class IBKRConfig:
    """Configuration for IBKR connection and trading"""
    
    # IBKR Connection Settings
    host: str = os.getenv("IBKR_HOST", "127.0.0.1")
    port: int = int(os.getenv("IBKR_PORT", "7497"))  # Paper trading port (7496 for live)
    client_id: int = int(os.getenv("IBKR_CLIENT_ID", "123"))
    
    # Trading Settings
    initial_cash: float = float(os.getenv("INITIAL_CASH", "200.0"))  # $200 AUD as specified
    currency: str = os.getenv("CURRENCY", "AUD")
    max_position_size: float = float(os.getenv("MAX_POSITION_SIZE", "0.2"))  # 20% max per position
    
    # Scheduling
    analysis_schedule: str = os.getenv("ANALYSIS_SCHEDULE", "09:00")  # Daily analysis time
    timezone: str = os.getenv("TIMEZONE", "Australia/Sydney")
    
    # AI Model Configuration
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    model_provider: str = os.getenv("MODEL_PROVIDER", "OpenAI")
    
    # Risk Management
    max_daily_trades: int = int(os.getenv("MAX_DAILY_TRADES", "10"))
    max_position_value: float = float(os.getenv("MAX_POSITION_VALUE", "40.0"))  # $40 AUD max per position
    
    # Logging
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_file: str = os.getenv("LOG_FILE", "ibkr_hedge_fund.log")

@dataclass
class TradingConfig:
    """Trading-specific configuration"""
    
    # Australian Stock Exchange watchlist
    watchlist: Optional[List[str]] = None
    
    # Agent selection
    selected_agents: Optional[List[str]] = None
    
    # Risk parameters
    stop_loss_pct: float = 0.05  # 5% stop loss
    take_profit_pct: float = 0.10  # 10% take profit
    
    def __post_init__(self):
        if self.watchlist is None:
            self.watchlist = [
                "CBA",  # Commonwealth Bank
                "BHP",  # BHP Group
                "CSL",  # CSL Limited
                "WBC",  # Westpac Banking Corporation
                "ANZ",  # ANZ Banking Group
                "NAB",  # National Australia Bank
                "WOW",  # Woolworths Group
                "TLS",  # Telstra Corporation
                "RIO",  # Rio Tinto
                "MQG",  # Macquarie Group
                "TCL",  # Transurban Group
                "WDS",  # Woodside Energy
                "FMG",  # Fortescue Metals Group
                "STO",  # Santos Limited
                "QAN"   # Qantas Airways
            ]
        
        if self.selected_agents is None:
            self.selected_agents = [
                "warren_buffett",
                "valuation_analyst",
                "sentiment_analyst",
                "fundamentals_analyst",
                "technical_analyst"
            ]

def get_config() -> IBKRConfig:
    """Get the IBKR configuration"""
    return IBKRConfig()

def get_trading_config() -> TradingConfig:
    """Get the trading configuration"""
    return TradingConfig()

def validate_config(config: IBKRConfig) -> bool:
    """Validate the configuration"""
    if config.initial_cash <= 0:
        print("Error: Initial cash must be positive")
        return False
    
    if config.max_position_size <= 0 or config.max_position_size > 1:
        print("Error: Max position size must be between 0 and 1")
        return False
    
    if config.port not in [7496, 7497]:
        print("Warning: Port should be 7496 (live) or 7497 (paper)")
    
    return True

def setup_environment():
    """Setup environment variables and validate configuration"""
    config = get_config()
    
    if not validate_config(config):
        raise ValueError("Invalid configuration")
    
    # Set up required environment variables for AI-Hedge-Fund
    required_env_vars = [
        'OPENAI_API_KEY',
        'FINANCIAL_DATASETS_API_KEY'
    ]
    
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    if missing_vars:
        print(f"Warning: Missing environment variables: {', '.join(missing_vars)}")
        print("Some AI agents may not function properly without these keys")
    
    return config

if __name__ == "__main__":
    # Test configuration
    config = setup_environment()
    trading_config = get_trading_config()
    
    print("IBKR Configuration:")
    print(f"  Host: {config.host}:{config.port}")
    print(f"  Initial Cash: ${config.initial_cash} {config.currency}")
    print(f"  Max Position Size: {config.max_position_size * 100}%")
    print(f"  Analysis Schedule: {config.analysis_schedule}")
    
    print("\nTrading Configuration:")
    print(f"  Watchlist: {len(trading_config.watchlist) if trading_config.watchlist else 0} stocks")
    print(f"  Selected Agents: {', '.join(trading_config.selected_agents) if trading_config.selected_agents else 'None'}")
    print(f"  Stop Loss: {trading_config.stop_loss_pct * 100}%")
    print(f"  Take Profit: {trading_config.take_profit_pct * 100}%") 