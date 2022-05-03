from typing import Any
from webbrowser import get
import json
import streamlit as st
import pandas as pd
from Modules.apiSession import *
from Modules.formatNumbers import *

# --- A test reponse in JSON format ---
def writeCurrencyTest(response):
    st.write(json.loads(response.text)['data'])


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
    mainDf = pd.DataFrame(columns = ['Name', 'Price', '24h %', '7d %', 'Market Cap', 'Volume(24h)', 'Circulating Supply', 'Badge'])

    # Pull all the data into the Data Frame
    for i in range(len(wCrypto)):
        mainDf.loc[i] = json.loads(sortCryptoData(wCrypto[i]))
    return mainDf

@st.cache
# --- Defines the Cryptos that we'll gonna work ---
def cryptos():
    wCryptos = []

    bitcoin = getCrypto('bitcoin')
    wBitcoin = writeCurrency(bitcoin)
    wCryptos.append(wBitcoin)

    ethereum = getCrypto('ethereum')
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
