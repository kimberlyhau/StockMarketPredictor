# StockMarketPredictor
ECE324 Project: Using Sentiment Analysis of COVID-19 Headlines to Predict Stock Market Prices and Trends

# Project Description

This project aims to determine if stock prices can be predicted or if trends can be identified in different sectors of the US stock market due to the spread of COVID-19 information through news headlines. To classify the sentiment of headlines from popular American news sites, sentiment analysis, a machine learning method that has become increasing popular and is used to classify general position on subjective information, will be used. Then, a neural network will be used to evaluate the relationship between COVID-19 in the US and the US stock market. To represent the US stock market, the S&P 500 sector indices from January 1st, 2019, to January 31st, 2022, will be used. Headline selection will correspond to these dates. Using machine learning methodology will allow for pre-emptive and objective predictions of the stock market based on the pulse of the population via news. 


# Table of Contents
###### BERTSentimentAnalysis.py - BERT model for sentiment analysis of headlines, as well as text preprocessing 
###### scrapping.py - contains various attempts to use web scrapping to gather headline data.
###### nyTimesHeadlinesAPI.py - contains code for gathering NY Times article data using an API key, as well as organizing the data into a Pandas dataframe.
###### cnnHeadlines.py  - code for gathering CNN article data from the CNN archives.
###### cnnHeadlinesMultiThread.py - code for gathering CNN article data from CNN archives using multi threading. 
###### sectorPricesS&P.py - code for gathering S&P market closing prices.
###### yfinanceS&PPrices.py  - code for gathering S&P market closing prices using yfinance library.
###### requirements.txt - list of required python libraries and versions to run these programs. 
