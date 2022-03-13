
import pandas as pd
from bs4 import BeautifulSoup
import json
import requests
from urllib.request import urlopen
import requests


# websites= ["https://www.msn.com/en-ca/news/", "https://www.cnn.com/","https://www.nytimes.com/", "https://www.foxnews.com/","https://news.google.com/topstories?hl=en-CA&gl=CA&ceid=CA:en/"]



def cnn():

    #archive dates
    dates = ['2020-1.html',
            '2020-2.html',
            '2020-3.html',
            '2020-4.html',
            '2020-5.html',
            '2020-6.html',
            '2020-7.html',
            '2020-8.html',
            '2020-9.html',
            '2020-10.html',
            '2020-11.html',
            '2020-12.html',
            '2021-1.html',
            '2021-2.html',
            '2021-3.html',
            '2021-4.html',
            '2021-5.html',
            '2021-6.html',
            '2021-7.html',
            '2021-8.html',
            '2021-9.html',
            '2021-10.html',
            '2021-11.html',
            '2021-12.html',
            '2022-1.html']

    #baseUrl for cnn
    baseUrl = 'https://www.cnn.com/article/sitemap-'

    #masterDf 
    masterDf = []
    
    #Need to pull the data for each date
    for d in dates: 
        #create new url
        current = baseUrl+d

        print (current)
    
        #pull contents, and scrape website with beautiful soup
        response = urlopen(current)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')

        #lists to make dataframe and store information
        url = []
        headline = []
        text = []
        dateList = []
        currentUrl = []

        #for every link on the webpage
        for link in soup.find_all('a'):
            #get link
            next = link.get('href')

            #check if the link is valid
            if next != None:
                if "https://www.cnn.com/" in next:
                    
                    #Open the new link, scrape with bs
                    
                    try:
                        tempResposnse = urlopen(next)
                        tempcontent = tempResposnse.read().decode("utf-8")
                        tempsoup = BeautifulSoup(tempcontent, 'html.parser')
                        

                        #check different tags to get the date article was published. 

                        try:    
                            date =  (tempsoup.findAll('meta', itemprop="datePublished")[0])
                            date = (date.get('content'))
                        except:
                            pass
                    
                        
                        try:
                            if date == None or date == []:
                                key = True
                        except:
                            key = False
                            date = ''

                        if key == True:
                            date =  (tempsoup.find('script', type="application/ld+json")) #["datePublished"])
                            date = json.loads(date.text)

                            try: 
                                date = date['datePublished']      
                            except :
                                try:
                                    date = date['uploadDate']
                                except:
                                    date = ''
                                
                        #store: date, url, headline, base url, article text
                        dateList += [date]
                        url += [next]
                        headline+= [tempsoup.title.string]
                        currentUrl += [current]
                        text += [tempsoup.get_text()]
                    except:
                        pass

        #Make dictionary of data, turn into df, save file, add to master list. 
        df = {'url':url, 'date':dateList, 'headline':headline,'text':text,'currentUrl':currentUrl}
        df = pd.DataFrame(df)
        df.to_csv(d+"CNN.txt")

        masterDf.append(df)
        print (df)

    #combine all CNN data, write to text file
    masterDf = pd.concate(masterDf, axis = 1)
    masterDf.to_csv("masterCNN.txt")

if __name__ == "__main__":
    cnn()