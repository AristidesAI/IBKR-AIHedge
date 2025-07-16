#!/usr/bin/env python3
"""
IBKR AI Hedge Fund Integration

This module integrates the AI-Hedge-Fund system with Interactive Brokers (IBKR) API
to execute real trades based on AI analysis from multiple agents.

Features:
- Real-time data fetching from IBKR
- AI-powered analysis using multiple agents
- Risk management and position sizing
- Automated trade execution
- 24/7 operation with scheduled analysis
- Portfolio monitoring and reporting
"""

import asyncio
import logging
import os
import sys
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

import pandas as pd
import schedule
from dataclasses import dataclass, asdict
from decimal import Decimal

# IBKR API imports
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
from ibapi.common import TickerId, OrderId
from ibapi.ticktype import TickType

# Import AI-Hedge-Fund components
sys.path.append('src')
from agents.warren_buffett import warren_buffett_agent
from agents.cathie_wood import cathie_wood_agent
from agents.ben_graham import ben_graham_agent
from agents.stanley_druckenmiller import stanley_druckenmiller_agent
from agents.valuation import valuation_analyst_agent
from agents.sentiment import sentiment_analyst_agent
from agents.fundamentals import fundamentals_analyst_agent
from agents.technicals import technical_analyst_agent
from agents.risk_manager import risk_management_agent
from agents.portfolio_manager import portfolio_management_agent
from utils.analysts import ANALYST_CONFIG
from graph.state import AgentState
from data.models import AgentStateData, Portfolio, TickerAnalysis
from utils.progress import AgentProgress
from utils.display import print_trading_output
from main import create_workflow, run_hedge_fund

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ibkr_hedge_fund.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class IBKRConfig:
    """Configuration for IBKR connection"""
    host: str = "127.0.0.1"
    port: int = 7497  # Paper trading port (7496 for live)
    client_id: int = 123
    initial_cash: float = 200.0  # $200 AUD as specified
    currency: str = "AUD"
    max_position_size: float = 0.2  # 20% max per position
    analysis_schedule: str = "09:00"  # Daily analysis time
    timezone: str = "Australia/Sydney"

@dataclass
class Position:
    """Represents a position in the portfolio"""
    symbol: str
    quantity: int
    avg_cost: float
    market_value: float
    unrealized_pnl: float
    
@dataclass
class Trade:
    """Represents a trade execution"""
    symbol: str
    action: str
    quantity: int
    price: float
    timestamp: datetime
    order_id: int
    
class IBKRClient(EWrapper, EClient):
    """
    IBKR API client that handles connection, data requests, and trade execution
    """
    
    def __init__(self, config: IBKRConfig):
        EClient.__init__(self, self)
        self.config = config
        self.connected = False
        self.positions: Dict[str, Position] = {}
        self.portfolio_value = 0.0
        self.cash_balance = config.initial_cash
        self.pending_orders: Dict[int, Order] = {}
        self.market_data: Dict[str, Dict[str, float]] = {}
        self.contracts: Dict[str, Contract] = {}
        self.next_order_id = 1
        self.data_ready = threading.Event()
        
    def connect_to_ibkr(self) -> bool:
        """Connect to IBKR TWS or Gateway"""
        try:
            self.connect(self.config.host, self.config.port, self.config.client_id)
            
            # Wait for connection
            timeout = 10
            while not self.connected and timeout > 0:
                time.sleep(1)
                timeout -= 1
                
            if self.connected:
                logger.info("Successfully connected to IBKR")
                self.reqAccountUpdates(True, "")
                return True
            else:
                logger.error("Failed to connect to IBKR")
                return False
                
        except Exception as e:
            logger.error(f"Connection error: {e}")
            return False
    
    def nextValidId(self, orderId: int):
        """Callback for next valid order ID"""
        self.next_order_id = orderId
        self.connected = True
        logger.info(f"Connected. Next valid order ID: {orderId}")
    
    def error(self, reqId: TickerId, errorCode: int, errorString: str):
        """Handle errors from IBKR"""
        if errorCode in [2104, 2106, 2158]:  # Informational messages
            logger.info(f"Info {errorCode}: {errorString}")
        else:
            logger.error(f"Error {errorCode}: {errorString}")
    
    def get_stock_contract(self, symbol: str) -> Contract:
        """Create a stock contract for the given symbol"""
        if symbol not in self.contracts:
            contract = Contract()
            contract.symbol = symbol
            contract.secType = "STK"
            contract.exchange = "ASX"  # Australian Stock Exchange
            contract.currency = self.config.currency
            self.contracts[symbol] = contract
        return self.contracts[symbol]
    
    def request_market_data(self, symbols: List[str]) -> Dict[str, Dict[str, float]]:
        """Request real-time market data for symbols"""
        logger.info(f"Requesting market data for: {symbols}")
        
        for i, symbol in enumerate(symbols):
            contract = self.get_stock_contract(symbol)
            self.reqMktData(i, contract, "", False, False, [])
            self.market_data[symbol] = {}
        
        # Wait for data to be received
        self.data_ready.wait(timeout=30)
        return self.market_data
    
    def tickPrice(self, reqId: TickerId, tickType: TickType, price: float, attrib):
        """Handle tick price updates"""
        symbols = list(self.market_data.keys())
        if reqId < len(symbols):
            symbol = symbols[reqId]
            
            if tickType == TickType.BID:
                self.market_data[symbol]['bid'] = price
            elif tickType == TickType.ASK:
                self.market_data[symbol]['ask'] = price
            elif tickType == TickType.LAST:
                self.market_data[symbol]['last'] = price
            elif tickType == TickType.CLOSE:
                self.market_data[symbol]['close'] = price
                
        # Check if we have enough data
        if all('last' in data for data in self.market_data.values()):
            self.data_ready.set()
    
    def place_order(self, symbol: str, action: str, quantity: int, order_type: str = "MKT") -> int:
        """Place an order with IBKR"""
        contract = self.get_stock_contract(symbol)
        order = Order()
        order.action = action.upper()
        order.totalQuantity = quantity
        order.orderType = order_type
        
        order_id = self.next_order_id
        self.next_order_id += 1
        
        self.placeOrder(order_id, contract, order)
        self.pending_orders[order_id] = order
        
        logger.info(f"Placed {action} order for {quantity} shares of {symbol} (Order ID: {order_id})")
        return order_id
    
    def orderStatus(self, orderId: OrderId, status: str, filled: float, remaining: float, 
                   avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, 
                   clientId: int, whyHeld: str, mktCapPrice: float):
        """Handle order status updates"""
        logger.info(f"Order {orderId} status: {status}, filled: {filled}, remaining: {remaining}")
        
        if status == "Filled":
            if orderId in self.pending_orders:
                order = self.pending_orders[orderId]
                logger.info(f"Order {orderId} filled at {avgFillPrice}")
                del self.pending_orders[orderId]
    
    def updatePortfolio(self, contract: Contract, position: float, marketPrice: float, 
                       marketValue: float, averageCost: float, unrealizedPNL: float, 
                       realizedPNL: float, accountName: str):
        """Update portfolio positions"""
        symbol = contract.symbol
        if position != 0:
            self.positions[symbol] = Position(
                symbol=symbol,
                quantity=int(position),
                avg_cost=averageCost,
                market_value=marketValue,
                unrealized_pnl=unrealizedPNL
            )
        elif symbol in self.positions:
            del self.positions[symbol]
    
    def updateAccountValue(self, key: str, val: str, currency: str, accountName: str):
        """Update account values"""
        if key == "CashBalance" and currency == self.config.currency:
            self.cash_balance = float(val)
        elif key == "NetLiquidation" and currency == self.config.currency:
            self.portfolio_value = float(val)

class IBKRDataAdapter:
    """
    Adapter to convert IBKR data to the format expected by AI-Hedge-Fund agents
    """
    
    def __init__(self, ibkr_client: IBKRClient):
        self.ibkr_client = ibkr_client
    
    def get_price_data(self, symbol: str, start_date: str, end_date: str) -> List[Dict]:
        """Convert IBKR market data to price data format"""
        market_data = self.ibkr_client.market_data.get(symbol, {})
        
        # For real-time data, create a single price point
        if 'last' in market_data:
            return [{
                'time': datetime.now().isoformat(),
                'open': market_data.get('last', 0),
                'high': market_data.get('last', 0),
                'low': market_data.get('last', 0),
                'close': market_data.get('last', 0),
                'volume': 0  # Real-time tick data doesn't include volume
            }]
        return []
    
    def get_financial_metrics(self, symbol: str) -> List[Dict]:
        """Get financial metrics from IBKR (placeholder - would need fundamental data)"""
        # This would require IBKR fundamental data subscription
        # For now, return empty list - agents will handle gracefully
        return []
    
    def get_market_cap(self, symbol: str) -> Optional[float]:
        """Get market cap (placeholder)"""
        return None

class AIHedgeFundIntegration:
    """
    Main integration class that connects IBKR with AI-Hedge-Fund analysis
    """
    
    def __init__(self, config: IBKRConfig):
        self.config = config
        self.ibkr_client = IBKRClient(config)
        self.data_adapter = IBKRDataAdapter(self.ibkr_client)
        self.progress = AgentProgress()
        self.running = False
        self.trades_log: List[Trade] = []
        
        # Watchlist of stocks to analyze
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
            "MQG"   # Macquarie Group
        ]
    
    def start(self):
        """Start the integration"""
        logger.info("Starting IBKR AI Hedge Fund Integration")
        
        # Connect to IBKR
        if not self.ibkr_client.connect_to_ibkr():
            logger.error("Failed to connect to IBKR. Exiting.")
            return False
        
        # Start the client processing thread
        api_thread = threading.Thread(target=self.ibkr_client.run, daemon=True)
        api_thread.start()
        
        # Schedule daily analysis
        schedule.every().day.at(self.config.analysis_schedule).do(self.run_analysis)
        
        # Start the scheduler
        self.running = True
        self.schedule_thread = threading.Thread(target=self.run_scheduler, daemon=True)
        self.schedule_thread.start()
        
        logger.info("Integration started successfully")
        return True
    
    def stop(self):
        """Stop the integration"""
        logger.info("Stopping IBKR AI Hedge Fund Integration")
        self.running = False
        self.ibkr_client.disconnect()
    
    def run_scheduler(self):
        """Run the scheduled tasks"""
        while self.running:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    def run_analysis(self):
        """Run the AI analysis and execute trades"""
        logger.info("Starting daily analysis")
        
        try:
            # Get market data for watchlist
            market_data = self.ibkr_client.request_market_data(self.watchlist)
            
            # Filter out symbols with no data
            available_symbols = [symbol for symbol in self.watchlist 
                               if symbol in market_data and 'last' in market_data[symbol]]
            
            if not available_symbols:
                logger.warning("No market data available for analysis")
                return
            
            # Run AI analysis
            analysis_results = self.run_ai_analysis(available_symbols)
            
            # Execute trades based on analysis
            self.execute_trades(analysis_results)
            
            # Log portfolio status
            self.log_portfolio_status()
            
        except Exception as e:
            logger.error(f"Error during analysis: {e}")
    
    def run_ai_analysis(self, symbols: List[str]) -> Dict:
        """Run the AI-Hedge-Fund analysis on the given symbols"""
        logger.info(f"Running AI analysis on {len(symbols)} symbols")
        
        # Create initial portfolio state
        portfolio = self.create_portfolio_state()
        
        # Prepare agent state
        agent_state = AgentState(
            messages=[],
            data={
                "tickers": symbols,
                "portfolio": portfolio,
                "start_date": (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
                "end_date": datetime.now().strftime('%Y-%m-%d')
            },
            metadata={
                "show_reasoning": True,
                "model_name": "gpt-4o-mini",
                "model_provider": "OpenAI"
            }
        )
        
        # Create workflow with selected agents
        selected_agents = [
            "warren_buffett",
            "valuation_analyst",
            "sentiment_analyst",
            "fundamentals_analyst",
            "technical_analyst"
        ]
        
        # Use the existing AI-Hedge-Fund workflow
        workflow = create_workflow(selected_agents)
        
        # Run the analysis
        self.progress.start()
        try:
            result = workflow.invoke(agent_state)
            return result
        finally:
            self.progress.stop()
    
    def create_portfolio_state(self) -> Dict:
        """Create portfolio state from current IBKR positions"""
        portfolio = {
            "cash": self.ibkr_client.cash_balance,
            "margin_requirement": 0.0,
            "margin_used": 0.0,
            "positions": {},
            "realized_gains": {}
        }
        
        # Add current positions
        for symbol, position in self.ibkr_client.positions.items():
            portfolio["positions"][symbol] = {
                "long": max(0, position.quantity),
                "short": max(0, -position.quantity),
                "long_cost_basis": position.avg_cost if position.quantity > 0 else 0,
                "short_cost_basis": position.avg_cost if position.quantity < 0 else 0,
                "short_margin_used": 0.0
            }
            
            portfolio["realized_gains"][symbol] = {
                "long": 0.0,
                "short": 0.0
            }
        
        return portfolio
    
    def execute_trades(self, analysis_results: Dict):
        """Execute trades based on AI analysis results"""
        logger.info("Executing trades based on AI analysis")
        
        # Parse the analysis results
        decisions = analysis_results.get("data", {}).get("decisions", {})
        
        if not decisions:
            logger.warning("No trading decisions found in analysis results")
            return
        
        # Execute each decision
        for symbol, decision in decisions.items():
            try:
                self.execute_single_trade(symbol, decision)
            except Exception as e:
                logger.error(f"Error executing trade for {symbol}: {e}")
    
    def execute_single_trade(self, symbol: str, decision: Dict):
        """Execute a single trade based on AI decision"""
        action = decision.get("action", "hold")
        quantity = decision.get("quantity", 0)
        confidence = decision.get("confidence", 0)
        reasoning = decision.get("reasoning", "")
        
        logger.info(f"Trade decision for {symbol}: {action} {quantity} shares (confidence: {confidence}%)")
        logger.info(f"Reasoning: {reasoning}")
        
        if action == "hold" or quantity == 0:
            logger.info(f"Holding position for {symbol}")
            return
        
        # Map AI actions to IBKR actions
        ibkr_action = {
            "buy": "BUY",
            "sell": "SELL",
            "short": "SELL",
            "cover": "BUY"
        }.get(action.lower())
        
        if not ibkr_action:
            logger.warning(f"Unknown action: {action}")
            return
        
        # Execute the trade
        order_id = self.ibkr_client.place_order(symbol, ibkr_action, quantity)
        
        # Log the trade
        trade = Trade(
            symbol=symbol,
            action=action,
            quantity=quantity,
            price=self.ibkr_client.market_data.get(symbol, {}).get('last', 0),
            timestamp=datetime.now(),
            order_id=order_id
        )
        
        self.trades_log.append(trade)
        logger.info(f"Trade executed: {trade}")
    
    def log_portfolio_status(self):
        """Log current portfolio status"""
        logger.info("=== Portfolio Status ===")
        logger.info(f"Cash Balance: ${self.ibkr_client.cash_balance:.2f} {self.config.currency}")
        logger.info(f"Portfolio Value: ${self.ibkr_client.portfolio_value:.2f} {self.config.currency}")
        
        if self.ibkr_client.positions:
            logger.info("Positions:")
            for symbol, position in self.ibkr_client.positions.items():
                logger.info(f"  {symbol}: {position.quantity} shares @ ${position.avg_cost:.2f}, "
                          f"Value: ${position.market_value:.2f}, "
                          f"P&L: ${position.unrealized_pnl:.2f}")
        else:
            logger.info("No positions held")
        
        logger.info("========================")
    
    def get_performance_report(self) -> Dict:
        """Generate performance report"""
        initial_value = self.config.initial_cash
        current_value = self.ibkr_client.portfolio_value
        total_return = ((current_value - initial_value) / initial_value) * 100
        
        return {
            "initial_cash": initial_value,
            "current_value": current_value,
            "total_return_pct": total_return,
            "total_trades": len(self.trades_log),
            "current_positions": len(self.ibkr_client.positions),
            "cash_balance": self.ibkr_client.cash_balance
        }

def main():
    """Main function to run the integration"""
    # Configuration
    config = IBKRConfig(
        host="127.0.0.1",
        port=7497,  # Paper trading port
        client_id=123,
        initial_cash=200.0,  # $200 AUD as specified
        currency="AUD",
        analysis_schedule="09:00"  # 9 AM daily analysis
    )
    
    # Create and start integration
    integration = AIHedgeFundIntegration(config)
    
    try:
        if integration.start():
            logger.info("Integration running. Press Ctrl+C to stop.")
            
            # Keep the main thread alive
            while True:
                time.sleep(60)
                
                # Log periodic status
                report = integration.get_performance_report()
                if len(integration.trades_log) > 0:
                    logger.info(f"Performance: {report['total_return_pct']:.2f}% return, "
                              f"{report['total_trades']} trades executed")
                
    except KeyboardInterrupt:
        logger.info("Received shutdown signal")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        integration.stop()
        logger.info("Integration stopped")

if __name__ == "__main__":
    main() 