#Import libraries
import requests
from bs4 import BeautifulSoup
import pandas
from collections import OrderedDict

#Fetch Player ID's
player_ids = pandas.read_csv("player_ids.csv")
ids = player_ids["Ids"]

#Base url
base_url = "https://www.fifa.com/worldcup/players/player/"
tail_url = "/profile.html"
player_list = []

c = 0
#iterate through all urls with correct ids to get data
for id_number in ids:
    c+=1
    print(c, id_number)
    if id_number == 270895:
        continue
    if id_number == 329076:
        continue

    #create dict to store
    d = OrderedDict()

    #Fetch url
    page = requests.get(base_url + str(id_number) + tail_url)
    soup = BeautifulSoup(page.content,"html.parser")

    #Scraping data
    # Here text removes the other coding, while replace gets rid of the new lines and strip clear the excess whitespaces
    d['Name'] = soup.find("div", {"class": "fi-p__name"}).text.replace("\n","").strip()
    d['Country'] = soup.find("div", {"class": "fi-p__country"}).text.replace("\n","").strip()
    d['Role'] = soup.find("div", {"class":"fi-p__role"}).text.replace("\n","").strip()
    d['Age'] = soup.find("div", {"class": "fi-p__profile-number__number"}).text.replace("\n","").strip()
    d['Height'] = soup.find_all("div", {"class": "fi-p__profile-number__number"})[1].text.replace("\n","").strip()
    d['Int_caps'] = soup.find_all("div", {"class": "fi-p__profile-number__number"})[2].text.replace("\n","").strip()
    d['Int_goal'] = soup.find_all("div", {"class": "fi-p__profile-number__number"})[3].text.replace("\n","").strip()

#Appending dictionary to list
# #Im not really sure how this works. But I think it'll create a .csv file with columns of each item in the dictionary. I just don't understand why I append d to player_list.
    player_list.append(d)
# print(player_list)

#a Cloumn seperated variables file takes in dictionary entries, where entries with the same key with be added to the end of the column. It now makes sense why we have to use the OrderedDictionary. If we didnt, the hieghts would all be sorted shorted to tallest, same with ages, goals, ect. The ordered dic keeps everythin in the order we scrapped it up in, and adds everything to the next row in the column. This shit is dope!

#Data Frame to store our ids
df = pandas.DataFrame(player_list)
df.to_csv('player_info.csv', index = False)
print("\n Success")


#____________thisPartIsAlreadyFinished_____________
#Request URL
# page = requests.get("https://www.fifa.com/worldcup/players.html")
# page = requests.get("https://www.fifa.com/worldcup/players/player/201200/profile.html")
# page = requests.get("https://www.fifa.com/worldcup/players/_libraries/byposition/[id]/_players-list")

#Fetch webpage
# soup = BeautifulSoup(page.content,"html.parser")
# print(soup.prettify().encode())

# #List to store data
# id_list = []
#
# #Iterating through all the players
# for ids in range(0,736):
#     section = soup.find_all("a", "fi-p--link")[ids]
#     id_list.append(section['data-player-id'])
#
# #Data Frame to store our ids
# df = pandas.DataFrame({
# "Ids":id_list
# })
# df.to_csv('player_ids.csv', index = False)
# print(df, "\n Success")
# ______ILeftItInHereForAReferenceForLater__________


"""

# Printing the data I have
# for var in list(vars()):
#     if var[:6] == "player":
#         print(var + " : " + str(vars()[var]))
"""
