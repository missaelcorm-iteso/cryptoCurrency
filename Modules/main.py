from Modules.getCryptos import *
from Modules.appComponents import *
from Modules.fileManagment import *
from Modules.apiSession import *

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
        selectCrypto(dFrame)
    except: st.text("Reload Page or delete cookies")
