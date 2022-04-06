from cryptoModule import *

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

selectCrypto()


#st.write(type(mainDf.loc[np.where(mainDf["Badge"]==option),"Badge"].values[0]))

#writeCurrencyTest(bitcoin)

#sortCryptoData(cryptoData)
