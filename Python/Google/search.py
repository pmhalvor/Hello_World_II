from googlesearch import search
from bs4 import BeautifulSoup
import requests
import pandas
import os
from read_textfile import file_to_dic, print_table

"""
This program searches Google, and will eventually determine the websites
position on a topic by pulling top 100-500 words and comparing them.

"""
# Get List of search result websites
query = "my topic"
list_of_sites = []

for i in search(query, tld="com", num=10, stop=10):
	list_of_sites.append(i)
	print(i)

for j in range(len(list_of_sites)):
	#Go through all the sites and pull the top 50 words

	# Request URL
	page = requests.get(list_of_sites[j])

	# Fetch webpage
	soup = BeautifulSoup(page.content, "html.parser")
	# print(soup.prettify().encode())

	text_content = []
	f = open('temp.txt', 'a', encoding='utf-8')
	for i in range(0,20): # for some reason this has to be 20
		paragraphs = soup.find_all("p")[i].text
		text_content.append(paragraphs.encode('utf-8'))
		print(paragraphs)
		f.write(paragraphs)
	f.close()

	# Read file and find most used words
	glob_dic = file_to_dic('temp.txt')
	print_table(glob_dic, 50) # Need to instead make function to write to another file
	#
