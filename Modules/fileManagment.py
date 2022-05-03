import streamlit as st
import pandas as pd
import os

# --- A funtion to exports a Data Frame on a CSV file ---
def exportCSV(dataFrame):
    # Makes a directory called "CSV", if it is not created, then it creates one
    os.makedirs('CSV', exist_ok=True)
    # Makes and export the CSV file
    CSV = dataFrame.to_csv("CSV/CryptoTable.csv", index=False, header=True)
    return CSV

# --- Downloads the CSV file that we previously made ---
def downloadCSV():
    # Read the CSV
    df = pd.read_csv('CSV/CryptoTable.csv')
    
    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    
    #Convert the readed CSV on a CSV file
    csv = convert_df(df)

    # Button to download the CSV file
    st.download_button(
        "Download data as CSV",
        csv,
        "CryptoTable.csv",
        "text/csv",
        key='download-csv'
    )
