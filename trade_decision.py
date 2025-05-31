from enum import Enum

class Action(Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

class TradeDecision:
    def __init__(self, symbol: str, action: Action, quantity: int):
        self.symbol = symbol
        self.action = action
        self.quantity = quantity

    def __repr__(self):
        return f"<TradeDecision {self.action} {self.quantity} of {self.symbol}>"
