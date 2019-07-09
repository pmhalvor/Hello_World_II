#Import libraries
import requests
from bs4 import BeautifulSoup
import pandas
from collections import OrderedDict

"""
This file pulls the player statistics from the 2018 world cup

"""

#Fetch Player ID's
player_ids = pandas.read_csv("player_ids.csv")
ids = player_ids["Ids"]

#Base url
base = "https://www.fifa.com/worldcup/_libraries/players/player/"
tail = "/_player-statistics.html"
player_list = []

c = 2
#iterate through all players, scraping their data
for id_num in ids:
    print("id line:",c)
    c+=1
    if id_num == 306194:
        continue

    #create dictionary
    d = OrderedDict()

    #Fetch current url
    page = requests.get(base + str(id_num) + tail)
    soup = BeautifulSoup(page.content,"html.parser")

    #Scraping the data
    all_profile = soup.find_all("div", {"class":"fi-p__profile-number__number"})
    if len(all_profile)<1:
        d['Matches played'] = "N/A"
        d['Minutes played'] = "N/A"
        d['Dist. covered'] ="N/A"
        d['Dist. covered (w/ ball)'] = "N/A"
        d['Dist. covered (w/o ball)'] = "N/A"
        d['Goals scored'] = "N/A"
        d['Pen. scored'] = "N/A"
        d['Goals (left ft)'] = "N/A"
        d['Goals (right ft)'] = "N/A"
        d['Goals (head)'] = "N/A"
        d['Goals (heel)'] = "N/A"
        d['Attempts'] = "N/A"
        d['Attempts (on target)'] = "N/A"
        d['Attempts (off target)'] = "N/A"
        d['Shots blocked'] = "N/A"
        d['Attempts (against woodwork)'] = "N/A"
        d['Free kicks'] = "N/A"
        d['Attempts (inside)'] = "N/A"
        d['Attempts (outside)'] = "N/A"
        d['Attempts (on target, inside)'] = "N/A"
        d['Attempts (on target, outside)'] = "N/A"
        d['Assists'] = "N/A"
        d['Total passes'] = "N/A"
        d['Passes complete'] = "N/A"
        d['Passes complete (short)'] = "N/A"
        d['Passes complete (medium)'] = "N/A"
        d['Passes complete (long)'] = "N/A"
        d['Crosses attemped'] = "N/A"
        d['Crosses complete'] = "N/A"
        d['Delivery into box'] = "N/A"
        d['Dribbles into box'] = "N/A"
        d['Corners'] = "N/A"
        d['Throws'] = "N/A"
        d['Tackles'] = "N/A"
        d['Tackles won'] = "N/A"
        d['Lost balls'] = "N/A"
        d['Tackles suffered'] = "N/A"
        d['Recovered balls'] = "N/A"
        d['Clearences'] = "N/A"
        d['Blocks'] = "N/A"
        d['Saves'] = "N/A"
        d['Save rate'] = "N/A"
        d['Goal kicks (complete)'] = "N/A"
        d['Red card'] = "N/A"
        d['Yellow card'] = "N/A"
        d['Fouls'] = "N/A"
        d['Fouls (penalty)'] = "N/A"
        d['Fouls sufferd'] = "N/A"
        d['Offsides'] = "N/A"

        #Update .csv file with blank info
        player_list.append(d)
        df = pandas.DataFrame(player_list)
        df.to_csv('player_stats_1.csv', index = False)
        print("\n Success")
        continue

    d['Matches played'] = all_profile[0].text.replace("\n","").strip()
    d['Minutes played'] = all_profile[1].text.replace("\n","").strip()
    d['Dist. covered'] = all_profile[2].text.replace("\n","").strip()
    d['Dist. covered (w/ ball)'] = all_profile[3].text.replace("\n","").strip()
    d['Dist. covered (w/o ball)'] = all_profile[4].text.replace("\n","").strip()
    d['Goals scored'] = all_profile[5].text.replace("\n","").strip()
    d['Pen. scored'] = all_profile[6].text.replace("\n","").strip()
    d['Goals (left ft)'] = all_profile[7].text.replace("\n","").strip()
    d['Goals (right ft)'] = all_profile[8].text.replace("\n","").strip()
    d['Goals (head)'] = all_profile[9].text.replace("\n","").strip()
    d['Goals (heel)'] = all_profile[10].text.replace("\n","").strip()
    d['Attempts'] = all_profile[11].text.replace("\n","").strip()
    d['Attempts (on target)'] = all_profile[12].text.replace("\n","").strip()
    d['Attempts (off target)'] = all_profile[13].text.replace("\n","").strip()
    d['Shots blocked'] = all_profile[14].text.replace("\n","").strip()
    d['Attempts (against woodwork)'] = all_profile[15].text.replace("\n","").strip()
    d['Free kicks'] = all_profile[16].text.replace("\n","").strip()
    d['Attempts (inside)'] = all_profile[17].text.replace("\n","").strip()
    d['Attempts (outside)'] = all_profile[18].text.replace("\n","").strip()
    d['Attempts (on target, inside)'] = all_profile[19].text.replace("\n","").strip()
    d['Attempts (on target, outside)'] = all_profile[20].text.replace("\n","").strip()
    d['Assists'] = all_profile[21].text.replace("\n","").strip()
    d['Total passes'] = all_profile[22].text.replace("\n","").strip()
    d['Passes complete'] = all_profile[23].text.replace("\n","").strip()
    d['Passes complete (short)'] = all_profile[24].text.replace("\n","").strip()
    d['Passes complete (medium)'] = all_profile[25].text.replace("\n","").strip()
    d['Passes complete (long)'] = all_profile[26].text.replace("\n","").strip()
    d['Crosses attemped'] = all_profile[27].text.replace("\n","").strip()
    d['Crosses complete'] = all_profile[28].text.replace("\n","").strip()
    d['Delivery into box'] = all_profile[29].text.replace("\n","").strip()
    d['Dribbles into box'] = all_profile[30].text.replace("\n","").strip()
    d['Corners'] = all_profile[31].text.replace("\n","").strip()
    d['Throws'] = all_profile[32].text.replace("\n","").strip()
    d['Tackles'] = all_profile[33].text.replace("\n","").strip()
    d['Tackles won'] = all_profile[34].text.replace("\n","").strip()
    d['Lost balls'] = all_profile[35].text.replace("\n","").strip()
    d['Tackles suffered'] = all_profile[36].text.replace("\n","").strip()
    d['Recovered balls'] = all_profile[37].text.replace("\n","").strip()
    d['Clearences'] = all_profile[38].text.replace("\n","").strip()
    d['Blocks'] = all_profile[39].text.replace("\n","").strip()
    d['Saves'] = all_profile[40].text.replace("\n","").strip()
    d['Save rate'] = all_profile[41].text.replace("\n","").strip()
    d['Goal kicks (complete)'] = all_profile[42].text.replace("\n","").strip()
    d['Red card'] = all_profile[43].text.replace("\n","").strip()
    d['Yellow card'] = all_profile[44].text.replace("\n","").strip()
    d['Fouls'] = all_profile[45].text.replace("\n","").strip()
    d['Fouls (penalty)'] = all_profile[46].text.replace("\n","").strip()
    d['Fouls sufferd'] = all_profile[47].text.replace("\n","").strip()
    d['Offsides'] = all_profile[48].text.replace("\n","").strip()

    #Appending dictionary to list
    player_list.append(d)

    #a Comma Seperated Variables file takes in dictionary entries, where entries with the same key with be added to the end of the column. It now makes sense why we have to use the OrderedDictionary. If we didnt, the hieghts would all be sorted shorted to tallest, same with ages, goals, ect. The ordered dic keeps everythin in the order we scrapped it up in, and adds everything to the next row in the column. This shit is dope!

    #Data Frame to store our ids
    df = pandas.DataFrame(player_list)
    df.to_csv('player_stats_1.csv', index = False)
    print("\n Success")
