import streamlit as st
import streamlit.components.v1 as components
from Modules.getCryptos import *
import numpy as np

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


# --- Displays the Data Frame using Streamlit Library ---
def streamlitFrame(dataFrame):
    st.dataframe(dataFrame, height=800)

# --- Displays a select box to choose one and display the content ---
def selectCrypto(dFrame):
    # Create the select box
    option = st.selectbox(
         'Gráfica:',
        (dFrame.get(["Badge"])), help="Select one of these")

    # Show a widget depending of the value selected in the previous select box
    with st.expander(option, True):
        components.html(f"""
        <script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-1" lcw-coin="{(dFrame.loc[np.where(dFrame["Badge"]==option),"Badge"].values[0])}" lcw-base="USD" lcw-secondary="BTC" lcw-period="d" lcw-color-tx="#ffffff" lcw-color-pr="#58c7c5" lcw-color-bg="#1f2434" lcw-border-w="1" ></div>
        """, height=212)
