from operator import index
from urllib import response
from webbrowser import get
from pip import main
from requests import Request, Session
import json
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import math
import numpy as np

def fValue(number):
    return ("{:,}".format(number))

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def writeCurrencyTest(response):
    st.write(json.loads(response.text)['data'])

# --- Start the session ---
def startHeaders():
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '4c2644ea-d9ac-4143-8dae-71df1b333b62'
    }
    global session
    session = Session()
    session.headers.update(headers)

# --- Get Crypto and return JSON info ---
def getCrypto(crypto):
    params = {
        'slug': str(crypto),
        'convert': 'usd'
    }
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    response = session.get(url, params=params)
    return response

# --- Writes the info of the Crypto ---
def writeCurrency(response):
    responseID = json.dumps(json.loads(response.text)['data'])
    for key in json.loads(responseID):
        responseID = key
    
    name = json.loads(response.text)['data'][responseID]['name']
    symbol = json.loads(response.text)['data'][responseID]['symbol']
    price = json.loads(response.text)['data'][responseID]['quote']['USD']['price']
    _24h = json.loads(response.text)['data'][responseID]['quote']['USD']['percent_change_24h']
    _7d = json.loads(response.text)['data'][responseID]['quote']['USD']['percent_change_7d']
    _Market = json.loads(response.text)['data'][responseID]['quote']['USD']['market_cap']
    _Volume = json.loads(response.text)['data'][responseID]['quote']['USD']['volume_24h']
    _cSupply = json.loads(response.text)['data'][responseID]['total_supply']
    #_last7Days = json.loads(response.text)['data'][responseID]

    cryptoData = [name, symbol, price, _24h, _7d, _Market, _Volume, _cSupply]

    return cryptoData

def sortCryptoData(cryptoData):
    newRow = json.dumps({
        'Name': f"{cryptoData[0]} ({cryptoData[1]})",
        'Price': fValue(round_up(cryptoData[2], 2)),
        '24h %': fValue(round_up(cryptoData[3], 2)),
        '7d %': fValue(round_up(cryptoData[4], 2)),
        'Market Cap': fValue(round_up(cryptoData[5], 2)),
        'Volume(24h)': fValue(round_up(cryptoData[6], 2)),
        'Circulating Supply': fValue(float(cryptoData[7])),
        'Badge': cryptoData[1]
        #'Last 7 Days': []
    })
    return newRow

startHeaders()
cryptosJSON = {
        'Name',
        'Price',
        '24h %',
        '7d %',
        'Market Cap',
        'Volume(24h)',
        'Circulating Supply',
        #'Last 7 Days'
    }

def dataFrame(wCrypto):
    global mainDf
    mainDf = pd.DataFrame(columns=json.loads(sortCryptoData(wEthereum)))

    for i in range(len(wCrypto)):
        mainDf.loc[i] = json.loads(sortCryptoData(wCrypto[i]))
    st.dataframe(mainDf)

st.set_page_config(
     page_title="Crypto Currency APP",
     page_icon="💲",
     layout="centered",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

def selectCrypto(cryptos):
    option = st.selectbox(
         'Gráfica:',
        (mainDf.get(["Badge"])), help="Select one of these")

    with st.expander(option, True):
        components.html(f"""
        <script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-1" lcw-coin="{(mainDf.loc[np.where(mainDf["Badge"]==option),"Badge"].values[0])}" lcw-base="USD" lcw-secondary="BTC" lcw-period="d" lcw-color-tx="#ffffff" lcw-color-pr="#58c7c5" lcw-color-bg="#1f2434" lcw-border-w="1" ></div>
        """, height=212)

st.title('💲CryptoCurrency💲')

components.html('''<script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-5" lcw-base="USD" lcw-color-tx="#999999" lcw-marquee-1="coins" lcw-marquee-2="movers" lcw-marquee-items="30" ></div>''', height=75)

bitcoin = getCrypto('bitcoin')
wBitcoin = writeCurrency(bitcoin)

ethereum = getCrypto('ethereum')
wEthereum = writeCurrency(ethereum)

tether = getCrypto('tether')
wTether = writeCurrency(tether)

bnb = getCrypto('bnb')
wBnb = writeCurrency(bnb)

xrp = getCrypto('xrp')
wXrp = writeCurrency(xrp)

solana = getCrypto('solana')
wSolana = writeCurrency(solana)

cardano = getCrypto('cardano')
wCardano = writeCurrency(cardano)

dogecoin = getCrypto('dogecoin')
wDogecoin = writeCurrency(dogecoin)

litecoin = getCrypto('litecoin')
wLitecoin = writeCurrency(litecoin)

wCryptos = [wBitcoin, wEthereum, wTether, wXrp, wSolana, wCardano, wDogecoin, wLitecoin]

dataFrame(wCryptos)

selectCrypto(wCryptos)


components.html("""""")



#st.write(type(mainDf.loc[np.where(mainDf["Badge"]==option),"Badge"].values[0]))

#writeCurrencyTest(bitcoin)

#sortCryptoData(cryptoData)
