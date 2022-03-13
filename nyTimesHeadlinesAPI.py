
import requests
from bs4 import BeautifulSoup
import datetime 
import pandas as pd
from urllib.request import urlopen


def nytimes():

    #store outout
    all_output =[]

    #date range of interest
    start_dt = datetime.date(2019,1,1)
    end_dt = datetime.date(2019,3,31)

    #api key
    key = "DjHJJ7AGTOpRARxYh5WEUNIK7ekHC7Ep"
    

    #pull data for each month
    for month in range(1,2):

        #open url, store as json file
        url = "https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key="+key
        r = requests.get(url)
        json_data = r.json()

        #convert json to dataframe, keep only required data
        df = pd.json_normalize(json_data['response']['docs'])
        df = df[['pub_date', 'headline.main','keywords','news_desk','web_url']]
        df['source'] = ['nytimes']*len(df)

        #Add df to master list
        all_output += [df]
    
    #combine all the pulled data
    allDf = pd.concat(all_output, axis = 0).reset_index(drop = True)

    #for every url in the dataframe
    allDf['text'] = [' ']*len(allDf)
    for i in range(0,len(allDf)):

        #check if link is valid. If valid, pull text and save in dataframe
        try:
            response = urlopen(allDf.iloc[i]['web_url'])
            content = response.read()
            soup = BeautifulSoup(content, 'html.parser')
            allDf.loc[i, 'text'] = soup.get_text()
        except: 
            pass
  
 
    #Save Data to text      
    allDf.to_csv("nyTimes.txt")
  


if __name__ == "__main__":
    nytimes()