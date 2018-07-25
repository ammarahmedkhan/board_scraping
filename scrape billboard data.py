# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 22:29:02 2018

@author: DELL inspiron
"""

import requests
import pandas as pd

chart_date = '2014-10-18'
url='https://www.billboard.com/charts/pop-songs/'
url = url + chart_date
r=requests.get(url)
text=r.text


"""
file=open('text.txt','r')
text=file.read()
file.close()
"""
from bs4 import BeautifulSoup
import math
soup=BeautifulSoup(text)
pretty_soup=soup.prettify()
divs = soup.findAll("div", {"class": "chart-list-item"})

artists=[]
songs=[]
current_rank=[]
last_week=[]
peak_pos=[]
weeks_on_chart=[]
weeks_on_one=[]
search_song='chart-list-item__title'
search_artist='chart-list-item__artist'
search_current_rank='chart-list-item__position'
search_last_week='chart-list-item__last-week'
search_peak_pos='chart-list-item__weeks-at-one'
search_weeks_on_chart = 'chart-list-item__weeks-on-chart'



for a in divs:
    
    songs.append(a.find("div",{"class":search_song}).get_text())
    artists.append(a.find("div",{"class":search_artist}).get_text().replace('\n',''))
    current_rank.append(a.find("div",{"class":search_current_rank}).get_text().replace('\n',''))
    last_week.append(a.find("div",{"class":search_last_week}))
    peak_pos.append(a.find("div",{"class":search_peak_pos}))
    weeks_on_chart.append(a.find("div",{"class":search_weeks_on_chart}))
last_week=[int(a.get_text()) if a !=None  else math.nan for a in last_week]
peak_pos=[int(a.get_text()) if a !=None else math.nan for a in peak_pos]
weeks_on_chart=[int(a.get_text()) if a !=None else math.nan for a in weeks_on_chart]


a=soup.find("div", {"class": "chart-number-one__weeks-at-one"})
weeks_on_one = [(int(a.get_text().replace('\n','')))] + weeks_on_one 

a=soup.find("div", {"class": "chart-number-one__weeks-on-chart"})
weeks_on_chart = [(int(a.get_text().replace('\n','')))] + weeks_on_chart

a=soup.find("div", {"class": "chart-number-one__artist"})
artists = [(a.get_text().replace('\n',''))]+artists
a=soup.find("div", {"class": "chart-number-one__title"})
songs = [(a.get_text().replace('\n',''))] + songs 

current_rank= [1] + current_rank
peak_pos=[1]+peak_pos
last_week=[math.nan] + last_week
chart_date  = [chart_date]*len(last_week)


df=pd.DataFrame({'chart_date':chart_date,
                 'songs':songs,
                 'artists':artists,
                 'current_rank':current_rank,
                'last_week':last_week,
                'peak_pos':peak_pos,
                'weeks_on_chart':weeks_on_chart
                 })
    
"""
call df.csv('data')
"""