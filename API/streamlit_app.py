from cryptoModule import *

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

st.title('💲CryptoCurrency💲')

components.html('''<script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-5" lcw-base="USD" lcw-color-tx="#999999" lcw-marquee-1="coins" lcw-marquee-2="movers" lcw-marquee-items="30" ></div>''', height=75)

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

selectCrypto()


#st.write(type(mainDf.loc[np.where(mainDf["Badge"]==option),"Badge"].values[0]))

#writeCurrencyTest(bitcoin)

#sortCryptoData(cryptoData)
