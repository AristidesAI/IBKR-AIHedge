import requests
import json

class IBKRClient:
    def __init__(self, client_id, client_secret, base_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.access_token = self.authenticate()

    def authenticate(self):
        token_url = f"{self.base_url}/v1/api/token"
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(token_url, data=payload)
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            raise Exception("Authentication failed.")

    def get_conid(self, symbol):
        url = f"{self.base_url}/v1/api/iserver/secdef/search"
        headers = {'Authorization': f'Bearer {self.access_token}'}
        params = {"symbol": symbol.upper()}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            results = response.json()
            if results:
                return results[0].get("conid")
            else:
                raise Exception(f"No contract found for symbol: {symbol}")
        else:
            raise Exception(f"Conid lookup failed: {response.status_code} - {response.text}")

    def place_order(self, account_id, order_data):
        url = f"{self.base_url}/v1/api/accounts/{account_id}/orders"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=json.dumps(order_data))
        return response.json()
