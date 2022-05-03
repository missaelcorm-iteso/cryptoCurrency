from requests import Request, Session
import streamlit as st

# --- Starts the session ---
def startHeaders():
    # Create the headers using our API key
    YOUR_API_KEY = st.secrets["api_key"]
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': f'{YOUR_API_KEY}'
    }
    # Start the session to the API
    global session
    session = Session()
    session.headers.update(headers)

# --- Gets Crypto and return JSON info ---
def getCrypto(crypto):
    # Define the params
    params = {
        'slug': str(crypto),
        'convert': 'usd'
    }
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    # Get the response of the API, with the Crypto information 
    response = session.get(url, params=params)
    return response
