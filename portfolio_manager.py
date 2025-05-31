from trade_decision import TradeDecision, Action
from ibkr_client import IBKRClient

class PortfolioManagerAgent:
    def __init__(self, account_id: str):
        self.account_id = account_id
        self.ibkr_client = IBKRClient(
            client_id='your_client_id',
            client_secret='your_client_secret',
            base_url='https://api.interactivebrokers.com'
        )

    def aggregate_decisions(self, agent_outputs):
        decisions = []
        for output in agent_outputs:
            symbol = output.get("symbol")
            signal = output.get("signal")
            quantity = output.get("quantity", 10)
            action_map = {
                "buy": Action.BUY,
                "sell": Action.SELL,
                "hold": Action.HOLD
            }
            action = action_map.get(signal.lower(), Action.HOLD)
            decisions.append(TradeDecision(symbol, action, quantity))
        return decisions

    def execute_decisions(self, decisions):
        for decision in decisions:
            print(f"Processing decision: {decision}")
            if decision.action == Action.HOLD:
                continue
            conid = self.ibkr_client.get_conid(decision.symbol)
            self.place_order(conid, decision)

    def place_order(self, conid, decision: TradeDecision):
        order_data = {
            "conid": conid,
            "orderType": "MKT",
            "side": decision.action.value.lower(),
            "quantity": decision.quantity,
            "tif": "DAY"
        }
        return self.ibkr_client.place_order(self.account_id, order_data)
