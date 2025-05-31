from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Literal

from ibkr_client import IBKRClient

app = FastAPI()

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
BASE_URL = "https://api.interactivebrokers.com"
ACCOUNT_ID = "your_ibkr_account_id"

ibkr_client = IBKRClient(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, base_url=BASE_URL)

class TradeRequest(BaseModel):
    symbol: str
    action: Literal["buy", "sell"]
    quantity: int

@app.get("/conid")
def get_conid(symbol: str = Query(..., description="Ticker symbol to lookup")):
    try:
        conid = ibkr_client.get_conid(symbol)
        return {"symbol": symbol.upper(), "conid": conid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/trade")
def place_trade(trade: TradeRequest):
    try:
        conid = ibkr_client.get_conid(trade.symbol)
        order_data = {
            "conid": conid,
            "orderType": "MKT",
            "side": trade.action,
            "quantity": trade.quantity,
            "tif": "DAY"
        }
        response = ibkr_client.place_order(ACCOUNT_ID, order_data)
        return {"status": "success", "response": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "ok"}
