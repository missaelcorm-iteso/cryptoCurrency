from typing import Any
from webbrowser import get
from requests import Request, Session
import json
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import math
import numpy as np
import os

# --- Separates the number by commas (,), example: 1,234,456 ---
def fValue(number):
    return ("{:,}".format(number))

# --- Rounds Up the number, example 1234.56789 -> 1234.57 ---
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

# --- A test reponse in JSON format ---
def writeCurrencyTest(response):
    st.write(json.loads(response.text)['data'])

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

# --- Writes the info of the Crypto ---
def writeCurrency(response):
    # Load the respone
    responseID = json.dumps(json.loads(response.text)['data'])
    for key in json.loads(responseID):
        responseID = key
    
    # Assign the values to the variable that it corresponds
    name = json.loads(response.text)['data'][responseID]['name']
    symbol = json.loads(response.text)['data'][responseID]['symbol']
    price = json.loads(response.text)['data'][responseID]['quote']['USD']['price']
    _24h = json.loads(response.text)['data'][responseID]['quote']['USD']['percent_change_24h']
    _7d = json.loads(response.text)['data'][responseID]['quote']['USD']['percent_change_7d']
    _Market = json.loads(response.text)['data'][responseID]['quote']['USD']['market_cap']
    _Volume = json.loads(response.text)['data'][responseID]['quote']['USD']['volume_24h']
    _cSupply = json.loads(response.text)['data'][responseID]['total_supply']
    #_last7Days = json.loads(response.text)['data'][responseID]

    #A list with all data
    cryptoData = [name, symbol, price, _24h, _7d, _Market, _Volume, _cSupply]

    return cryptoData

# --- Specifies the rows on the data frame ---
def sortCryptoData(cryptoData):
    # Made a dictionary with the values to make a Data Frame
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

# --- Adds the information from the JSON request to ---
# --- a Data Frame created by Pandas Library       ---
def dataFrame(wCrypto):
    # Define the columns of the Data Frame
    global mainDf
    mainDf = pd.DataFrame(columns = json.loads(sortCryptoData(wEthereum)))

    # Pull all the data into the Data Frame
    for i in range(len(wCrypto)):
        mainDf.loc[i] = json.loads(sortCryptoData(wCrypto[i]))
    return mainDf

# --- Displays the Data Frame using Streamlit Library ---
def streamlitFrame(dataFrame):
    st.dataframe(dataFrame, height=800)

# --- Displays a select box to choose one and display the content ---
def selectCrypto():
    # Create the select box
    option = st.selectbox(
         'Gráfica:',
        (mainDf.get(["Badge"])), help="Select one of these")

    # Show a widget depending of the value selected in the previous select box
    with st.expander(option, True):
        components.html(f"""
        <script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-1" lcw-coin="{(mainDf.loc[np.where(mainDf["Badge"]==option),"Badge"].values[0])}" lcw-base="USD" lcw-secondary="BTC" lcw-period="d" lcw-color-tx="#ffffff" lcw-color-pr="#58c7c5" lcw-color-bg="#1f2434" lcw-border-w="1" ></div>
        """, height=212)

# --- Sest the basics components of the App ---
def appComponents():
    st.set_page_config(
        page_title="Crypto Currency APP",
        page_icon="💲",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "# CryptoCurrency\n"+
            "**CryptoCurrency** is a project WebApp to a University Activity.\n\n"+
            '-Missael Cortés Mendoza\n'+
            '***'
        }
    )

    st.title('💲CryptoCurrency💲')

    components.html('''<script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-5" lcw-base="USD" lcw-color-tx="#999999" lcw-marquee-1="coins" lcw-marquee-2="movers" lcw-marquee-items="30" ></div>''', height=75)
    with st.expander("Coin Converter", False):
        components.html('''<div style="width: 250px; height:335px; background-color: #232937; overflow:hidden; box-sizing: border-box; border: 1px solid #282E3B; border-radius: 4px; text-align: right; line-height:14px; block-size:335px; font-size: 12px; font-feature-settings: normal; text-size-adjust: 100%; box-shadow: inset 0 -20px 0 0 #262B38;margin: 0;width: 250px;padding:1px;padding: 0px; margin: 0px;"><div style="height:315px; padding:0px; margin:0px; width: 100%;"><iframe src="https://widget.coinlib.io/widget?type=converter&theme=dark" width="250" height="310px" scrolling="auto" marginwidth="0" marginheight="0" frameborder="0" border="0" style="border:0;margin:0;padding:0;"></iframe></div><div style="color: #626B7F; line-height: 14px; font-weight: 400; font-size: 11px; box-sizing: border-box; padding: 2px 6px; width: 100%; font-family: Verdana, Tahoma, Arial, sans-serif;"><a href="https://coinlib.io" target="_blank" style="font-weight: 500; color: #626B7F; text-decoration:none; font-size:11px">Cryptocurrency Prices</a>&nbsp;by Coinlib</div></div>''', height=342)

@st.cache
# --- Defines the Cryptos that we'll gonna work ---
def cryptos():
    wCryptos = []

    bitcoin = getCrypto('bitcoin')
    wBitcoin = writeCurrency(bitcoin)
    wCryptos.append(wBitcoin)

    ethereum = getCrypto('ethereum')
    global wEthereum
    wEthereum = writeCurrency(ethereum)
    wCryptos.append(wEthereum)

    tether = getCrypto('tether')
    wTether = writeCurrency(tether)
    wCryptos.append(wTether)

    bnb = getCrypto('bnb')
    wBnb = writeCurrency(bnb)
    wCryptos.append(wBnb)

    xrp = getCrypto('xrp')
    wXrp = writeCurrency(xrp)
    wCryptos.append(wXrp)

    solana = getCrypto('solana')
    wSolana = writeCurrency(solana)
    wCryptos.append(wSolana)

    cardano = getCrypto('cardano')
    wCardano = writeCurrency(cardano)
    wCryptos.append(wCardano)

    dogecoin = getCrypto('dogecoin')
    wDogecoin = writeCurrency(dogecoin)
    wCryptos.append(wDogecoin)

    litecoin = getCrypto('litecoin')
    wLitecoin = writeCurrency(litecoin)
    wCryptos.append(wLitecoin)

    terra = getCrypto('terra')
    wTerra = writeCurrency(terra)
    wCryptos.append(wTerra)

    avalanche = getCrypto('avalanche')
    wAvalanche = writeCurrency(avalanche)
    wCryptos.append(wAvalanche)

    shiba_inu = getCrypto('shiba-inu')
    wShiba_inu = writeCurrency(shiba_inu)
    wCryptos.append(wShiba_inu)

    polygon = getCrypto('polygon')
    wPolygon = writeCurrency(polygon)
    wCryptos.append(wPolygon)

    cronos = getCrypto('cronos')
    wCronos = writeCurrency(cronos)
    wCryptos.append(wCronos)

    cosmos = getCrypto('cosmos')
    wCosmos = writeCurrency(cosmos)
    wCryptos.append(wCosmos)

    tron = getCrypto('tron')
    wTron = writeCurrency(tron)
    wCryptos.append(wTron)

    ftx_token = getCrypto('ftx-token')
    wFtx_token = writeCurrency(ftx_token)
    wCryptos.append(wFtx_token)

    monero = getCrypto('monero')
    wMonero = writeCurrency(monero)
    wCryptos.append(wMonero)

    decentraland = getCrypto('decentraland')
    wDecentraland = writeCurrency(decentraland)
    wCryptos.append(wDecentraland)

    maker = getCrypto('maker')
    wMaker = writeCurrency(maker)
    wCryptos.append(wMaker)

    neo = getCrypto('neo')
    wNeo = writeCurrency(neo)
    wCryptos.append(wNeo)

    return wCryptos

# --- A funtion to exports a Data Frame on a CSV file ---
def exportCSV(dataFrame):
    # Makes a directory called "CSV", if it is not created, then it creates one
    os.makedirs('CSV', exist_ok=True)
    # Makes and export the CSV file
    CSV = dataFrame.to_csv("CSV/out.csv", index=False, header=True)
    return CSV

# --- Downloads the CSV file that we previously made ---
def downloadCSV():
    # Read the CSV
    df = pd.read_csv('CSV/out.csv')
    
    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    
    #Convert the readed CSV on a CSV file
    csv = convert_df(df)

    # Button to download the CSV file
    st.download_button(
        "Download data as CSV",
        csv,
        "out.csv",
        "text/csv",
        key='download-csv'
    )

# --- Main Function ---
def Main():

    # Loads the components
    appComponents()
    startHeaders()
    
    try:
        # Defines the cryptos and get all data from them
        wCryptos = cryptos()

        # Puts the data into a Data Frame
        dFrame = dataFrame(wCryptos)
        # Display the Data Frame
        streamlitFrame(dFrame)

        # Creates a CSV file
        CSV = exportCSV(dFrame)
        # Creates a button to download the CSV file
        downloadCSV()
    
        # Shows the select box and the expander
        selectCrypto()
    except: st.text("Reload Page or delete cookies")

