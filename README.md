# board_scraping
Scraping the Billboard Hot 100 Site for data and extract following features

chart date,
song,
artists,
current_rank,
last_week,
peak_pos,
weeks on chart,
This works by submitting requests to the billboard hot 100 website for data 

I have used https://www.billboard.com/charts/pop-songs/2014-10-18 . 

From this, the top 40 songs for the date of 18 October, 2014 are fetched and
populated in a dataframe.

Whats best about this code is that it can also be used on other variations of
billboard websites. I have tried it on https://www.billboard.com/charts/hot-100/2014-08-02

This code can also be run as a function and different urls can be passed to dynamically scrape off data from this website.

Note: If i had submit a request to fetch the data for the date 16 October, 2014 , then since this date
wasnt on the weekly billboard schedule, it would return you the chart for the date of 18 October, 2014 .

Do share your feedback on this site or mrahmed_44@hotmail.com
