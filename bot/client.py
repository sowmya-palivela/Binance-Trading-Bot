from binance.client import Client

def create_client(api_key, api_secret):
    # create client in testnet mode
    client = Client(api_key, api_secret, testnet=True)

    # correct futures testnet endpoint
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
