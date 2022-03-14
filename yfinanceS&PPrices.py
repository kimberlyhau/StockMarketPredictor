import pandas as pd
import yfinance as yf
import numpy as np


#Import List of S&P 500 Companies
spData = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

#Store Data Frame with all Corp Information
companyData = spData[0].copy()

#List of All Sectors
sectorList = list(companyData["GICS Sector"].unique())

# #'Industrials', 'Health Care', 'Information Technology','Communication Services','Consumer Staples','Consumer Discretionary', 'Utilities', 
# sectorList = [ 'Financials', 'Materials', 'Real Estate', 'Energy']

#Dictionary to Store Sector and their Tickers
sectorDictionary = {}
#List to make df to store S&P 500 close prices by sector
sectorClosePrices = []

#Dictionary to store market cap
marketCapDict = {}

#For every sector 
for sector in sectorList:

    #Get a list of tickers in that sector, store tickers in the sector dictionary
    TickerList = companyData[companyData["GICS Sector"] == sector]["Symbol"].to_list()
    sectorDictionary[sector] = TickerList

    #convert list to a string to pull all data at once
    stringTickerList = TickerList.copy()
    stringTickerList = ' '.join(stringTickerList)

    #pull ticker info from Yahoo Finance Library
    tickerMaster = yf.Tickers(stringTickerList)
   

    #Lists to store close prices and the market cap fo each company
    closeData = []
    closeData2 = []
    freeFloatByCorp = {}
    totalfreeFloat = 0

    #for every ticker in this sector
    for ticker in TickerList:        
        
        #Pull the historical prices within the given data range, store the close column of the df. Pull company market cap.
        df = tickerMaster.tickers[ticker].history(start="2019-01-01", end="2022-01-31")

        #make sure df is not empty
        if df.empty == False:
            #pull market cap value
            freeFloat = tickerMaster.tickers[ticker].info['floatShares']

            #make sure market cap value is valid
            if freeFloat != None:

                #weight the price by the market capitalization
                updatedDF = df['Close']*(freeFloat)
                
                #store weighted close price and market cap value
                totalfreeFloat += freeFloat
                freeFloatByCorp[ticker] = freeFloat
                closeData += [updatedDF]
                closeData2 += [df['Close']]

    #Create DF    
    closingPrices = pd.concat(closeData, axis = 1)

    
    weights = {}
    count = 0
    total = 0
    for ticker in freeFloatByCorp.keys():
        weights[ticker] = freeFloatByCorp[ticker]/totalfreeFloat
        total += freeFloatByCorp[ticker]/totalfreeFloat
        closingPrices.iloc[:, count] = closingPrices.iloc[:, count]*weights[ticker]
        count += 1
   
    


    closingPrices['Close Prices '+sector] = closingPrices.sum('columns')

    

    #Write to csv
    closingPrices['Close Prices '+sector].to_csv(str(sector)+"SP500Data.txt")




#Create a S&P sector close prices dataframe
spSectorClose = pd.concat(sectorClosePrices, axis = 1)

#store all sectors together
spSectorClose.to_csv("SP500Data.txt")
