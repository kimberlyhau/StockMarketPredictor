from json.tool import main
import requests
from bs4 import BeautifulSoup
from datetime import date
# from GoogleNews import GoogleNews
# from newspaper import Article
# from newspaper import Config
import pandas as pd
import nltk
#import pyjq
import datetime
import time
from dateutil.rrule import rrule, MONTHLY
import csv
import json
import io

def cnn():
    today = date.today()
    d = today.strftime("%m-%d-%y")
    cnn_url="https://edition.cnn.com/world/live-news/coronavirus-pandemic-{}-intl/index.html".format(d)
    html = requests.get(cnn_url)
    bsobj = BeautifulSoup(html.content,'lxml')
    for link in bsobj.findAll("h2"):
        print("Headline : {}".format(link.text))

def google():
    """
    googlenews = GoogleNews(lang='en', period='1d')
    googlenews.search("machien learning")
    results = googlenews.results(sort = True)
    for result in results:
        print('\n\nTITLE:', result['title'], '\nDESC:', result['desc'], '\nURL: ', result['link'])
    """
    #config will allow us to access the specified url for which we are #not authorized. Sometimes we may get 403 client error while parsing #the link to download the article.
    nltk.download('punkt')

    #user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    #config = Config()
    #config.browser_user_agent = user_agent
    
    googlenews=GoogleNews(start='05/01/2020',end='05/31/2020')
    googlenews.search('Coronavirus')
    result=googlenews.result()
    df=pd.DataFrame(result)
    print(df.head())
    for i in range(2,20):
        googlenews.getpage(i)
        result=googlenews.result()
        df=pd.DataFrame(result)

    list=[]
    for ind in df.index:
        dict={}
        article = Article(df['link'][ind])#,config=config)
        article.download()
        article.parse()
        article.nlp()
        dict['Date']=df['date'][ind]
        dict['Title']=article.title
        dict['Article']=article.text
        dict['Summary']=article.summary
        list.append(dict)
    news_df=pd.DataFrame(list)
    news_df.head()
    #news_df.to_excel("articles.xlsx")
    

def bbc():
    
    url='https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    for x in headlines:
        print(x.text.strip())

# This one
def nytimes():
    all_output =[]
    start_dt = datetime.date(2019,1,1)
    end_dt = datetime.date(2019,1,31)
    key = "DjHJJ7AGTOpRARxYh5WEUNIK7ekHC7Ep"
    # NY Times archive pulls by the month
    #For one month - replace {year} and {month}
    """
    url = "https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key="+key
    r = requests.get(url)
    json_data = r.json() #stores json data in dictionary
    """
    #For 6 months - stored in all_output as a list of lists. To save to output file, do run command > output.log
    for month in range(1,2):
        url = "https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key="+key
        r = requests.get(url)
        json_data = r.json()

        df = pd.json_normalize(json_data['response']['docs'])
        df = df[['pub_date', 'headline.main','keywords','news_desk']]
        df['source'] = ['nytimes']*len(df)
        print (df)
        
    # print(all_output)
    """
    dates = [(dt.year, dt.month) for dt in rrule (MONTHLY, dtstart = start_dt, until = end_dt)]
    all_output =[]
    for year, month in dates:
        time.sleep(20)
        print(year, month)
        url = "https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key="+key
        r = requests.get(url)
        json_data = r.json()
        
        #length =  pyjq.all('.response .docs | length', json_data)[0]
        #jq_query = f'.response .docs [] | ((the_snippet: .snippet, the_headline: .headline .main, the_date: .pub_date))'
        #output = pyjq.all(jq_query, json_data)
        
        all_output.append([f'{year}{month:02}', json_data])
    return all_output
    """
    """
    ui="https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=yourkey"
    u="https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key=yourkey"
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=covid&api-key="+key
    url2 = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=new+york+times&page=2&sort=oldest&api-key="+key
    url3 = "https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=romney&facet_field=day_of_week&facet=true&begin_date=20120101&end_date=20120101&api-key="+key
    # /articlesearch.json?q={query}&fq={filter}
    r = requests.get(url)
    json_data = r.json()
    print(json_data)
    num_docs = pyjq.all('.response .docs | length', json_data)[0]
    jq_query = f'.response .docs [] | ((the_snippet: .snippet, the_headline: .headline .main, the_date: .pub_date))'
    output = pyjq.all(jq_query, json_data)
    """


if __name__ == "__main__":
    nytimes()