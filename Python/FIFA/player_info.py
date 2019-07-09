#Import libraries
import requests
from bs4 import BeautifulSoup
import pandas
from collections import OrderedDict

"""
This file scraps each players basic info like age, height and nationality

"""

#Fetch Player ID's
player_ids = pandas.read_csv("player_ids.csv")
ids = player_ids["Ids"]

#Base url
base_url = "https://www.fifa.com/worldcup/players/player/"
tail_url = "/profile.html"
player_list = []

#iterate through all urls with correct ids to get data
c = 0
for id_number in ids:
    c+=1
    print(c, id_number)
    # if id_number == 270895:
    #     continue
    # if id_number == 329076:
    #     continue

    #create dict to store
    d = OrderedDict()

    #Fetch url
    page = requests.get(base_url + str(id_number) + tail_url)
    soup = BeautifulSoup(page.content,"html.parser")

    #Scraping data
    if len(soup.find("div", {"class": "fi-p__name"}))<1:
        continue
    # Here text removes the other coding, while replace gets rid of the new lines and strip clear the excess whitespaces
    d['Name'] = soup.find("div", {"class": "fi-p__name"}).text.replace("\n","").strip()
    d['Country'] = soup.find("div", {"class": "fi-p__country"}).text.replace("\n","").strip()
    d['Role'] = soup.find("div", {"class":"fi-p__role"}).text.replace("\n","").strip()
    d['Age'] = soup.find("div", {"class": "fi-p__profile-number__number"}).text.replace("\n","").strip()
    d['Height'] = soup.find_all("div", {"class": "fi-p__profile-number__number"})[1].text.replace("\n","").strip()
    d['Int_caps'] = soup.find_all("div", {"class": "fi-p__profile-number__number"})[2].text.replace("\n","").strip()
    d['Int_goal'] = soup.find_all("div", {"class": "fi-p__profile-number__number"})[3].text.replace("\n","").strip()

#Appending dictionary to list
player_list.append(d)

#Data Frame to store our ids
df = pandas.DataFrame(player_list)
df.to_csv('player_info.csv', index = False)
print("\n Success")
