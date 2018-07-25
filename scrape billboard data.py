# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 22:29:02 2018

scrape off data from the billboard hot 100 site and extract following features

chart date,
song,
artists,
current_rank,
last_week,
peak_pos,
weeks on chart,
"""
#necessary imports
import requests
import pandas as pd

#date on which charts were released for that week in october 2014.
chart_date = '2014-10-18'
#billboard pop songs site url
url='https://www.billboard.com/charts/pop-songs/'

#concatenate both to get the pop songs charts from 18 october, 2014
url = url + chart_date
#submit req.
r=requests.get(url)
#get text
text=r.text

#since i did this with a lot of hit n trial, i downloaded the site locally and did my extraction 
#on the file below
"""
file=open('text.txt','r')
text=file.read()
file.close()
"""

#beautiful soup! 
from bs4 import BeautifulSoup
import math
soup=BeautifulSoup(text)
pretty_soup=soup.prettify()
#on the website, the chart is displayed as rows (duh!), and they all carry the class "chart-list-item"
#so i find all divs with that class
divs = soup.findAll("div", {"class": "chart-list-item"})

#initialize the relevant arrays for setting the data right in dataframe
artists=[]
songs=[]
current_rank=[]
last_week=[]
peak_pos=[]
weeks_on_chart=[]
weeks_on_one=[]

#initialize the relevant classes for scraping the data inside the row divs i got above.
search_song='chart-list-item__title'
search_artist='chart-list-item__artist'
search_current_rank='chart-list-item__position'
search_last_week='chart-list-item__last-week'
search_peak_pos='chart-list-item__weeks-at-one'
search_weeks_on_chart = 'chart-list-item__weeks-on-chart'

#iterate through my rows of divs and find releavnt details pertaining to that row/song.

for a in divs:
    
    songs.append(a.find("div",{"class":search_song}).get_text())
    artists.append(a.find("div",{"class":search_artist}).get_text().replace('\n',''))
    current_rank.append(a.find("div",{"class":search_current_rank}).get_text().replace('\n',''))
    last_week.append(a.find("div",{"class":search_last_week}))
    peak_pos.append(a.find("div",{"class":search_peak_pos}))
    weeks_on_chart.append(a.find("div",{"class":search_weeks_on_chart}))

#the following items had to be set differently through list iteration cuz
#not all of them return a fixed numeric value and some of them return None
#which makes perfect sense since its not necessary for a song to have a last
#week value if this is its debut on the charts! (intuition :-) )
last_week=[int(a.get_text()) if a !=None  else math.nan for a in last_week]
peak_pos=[int(a.get_text()) if a !=None else math.nan for a in peak_pos]
weeks_on_chart=[int(a.get_text()) if a !=None else math.nan for a in weeks_on_chart]

#now for the number one artist!  , has to be dealt separately since its shown on the website
#with a different formatting style 
a=soup.find("div", {"class": "chart-number-one__weeks-at-one"})
weeks_on_one = [(int(a.get_text().replace('\n','')))] + weeks_on_one 

a=soup.find("div", {"class": "chart-number-one__weeks-on-chart"})
weeks_on_chart = [(int(a.get_text().replace('\n','')))] + weeks_on_chart

a=soup.find("div", {"class": "chart-number-one__artist"})
artists = [(a.get_text().replace('\n',''))]+artists
a=soup.find("div", {"class": "chart-number-one__title"})
songs = [(a.get_text().replace('\n',''))] + songs 

#finally append the number one artist to the list and its on its way to be fed into our dataframe
current_rank= [1] + current_rank
peak_pos=[1]+peak_pos
last_week=[math.nan] + last_week
chart_date  = [chart_date]*len(last_week)

#seting the columns of the data frame to the data we got
df=pd.DataFrame({'chart_date':chart_date,
                 'songs':songs,
                 'artists':artists,
                 'current_rank':current_rank,
                'last_week':last_week,
                'peak_pos':peak_pos,
                'weeks_on_chart':weeks_on_chart
                 })
   
"""
save this dataset if you`d like to
call df.csv('data')
"""
