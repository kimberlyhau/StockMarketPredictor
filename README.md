# StockMarketPredictor
ECE324 Project: Using Sentiment Analysis of COVID-19 Headlines to Predict Stock Market Prices and Trends

# Project Description

  This project aims to determine if stock prices can be predicted or if trends can be identified in different sectors of the US stock market due to the spread of COVID-19 information through news headlines. To classify the sentiment of headlines from popular American news sites, sentiment analysis, a machine learning method that has become increasing popular and is used to classify general position on subjective information, will be used. Then, a neural network will be used to evaluate the relationship between COVID-19 in the US and the US stock market. To represent the US stock market, the S&P 500 sector indices from January 1st, 2019, to January 31st, 2022, will be used. Headline selection will correspond to these dates. Using machine learning methodology will allow for pre-emptive and objective predictions of the stock market based on the pulse of the population via news. 

# Table of Contents

###### 1. yfinanceS&PPrices.py: Code for gathering S&P market closing prices using yfinance library.
###### 2. sectorPricesS&P.py: Final code for gathering S&P market closing prices.
###### 3. scrapping.py: Contains various attempts to use web scrapping to gather headline data.
###### 4. nyTimesHeadlinesAPI.py: Contains code for gathering NY Times article data using an API key, as well as organizing the data into a Pandas dataframe.
###### 5. cnnHeadlines.py: Code for gathering CNN article data from the CNN archives.
###### 6. cnnHeadlinesMultiThread.py: Code for gathering CNN article data from CNN archives using multi threading. 
###### 7. BERTSentimentAnalysis.py: BERT model for sentiment analysis of headlines, as well as text pre-processing. 
###### 8. requirements.txt: List of required python libraries and versions to run these programs. 
###### 9. output.log.zip: Test raw NY Times output file. Unable to send file due to size over email. Uploded data to share. 
###### 10. VaderModel_SentimentAnalysis.ipynb: Vader Model for sentiment analysis of CNN headlines, as well as text pre-processing.
###### 11. NYTimes_VaderModel_SentimentAnalysis.ipynb: Vader Model for sentiment analysis of NY Times headlines, as well as text pre-processing.
###### 12. LSTMPredictor.ipynb: Template for LSTM model, first iteration of neural network used for stock predictions.
###### 13. LSTM_Predictor.ipynb: Second attempt of LSTM model for stock prediction. 
###### 14. Final_LSTM_Model_Predictor.ipynb: Final version of the LSTM model used for stock prediction. Contains training loop and final results. 
