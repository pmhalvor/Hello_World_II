#Import libraries
import requests
from bs4 import BeautifulSoup
import pandas

"""
This file scraps the player ids from every player in the 2018 world cup,
and stores info in file player_ids.csv
"""

# Request URL
page = requests.get("https://www.fifa.com/worldcup/players/_libraries/byposition/[id]/_players-list")

#Fetch webpage
soup = BeautifulSoup(page.content,"html.parser")
# print(soup.prettify().encode())

#List to store data
id_list = []

#Iterating through all the players
for ids in range(0,736):
    section = soup.find_all("a", "fi-p--link")[ids]
    id_list.append(section['data-player-id'])

#Data Frame to store our ids
df = pandas.DataFrame({
"Ids":id_list
})
df.to_csv('player_ids.csv', index = False)
print(df, "\n Success")
