"""
Created on Sat Nov 10 21:40:28 2018

@author: github.com/pmhalvor

Python version 3.6.1

This file is for analysing a text file and catagorizing the top used words,
 most often used words.  It shall later be implimented into a later project
 the reads webpages.

-count how many times the word has come up.

-sort results to most to least

"""

#coding: utf-8
import string


caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
all = caps+lower
# print(all)
conjunctions=['and', 'or', 'with', 'but', 'while', 'a', 'for', 'in', 'the', 'have', 'of', 'to', 'are', 'on', 'is', 'as', 'so', 'was']
konjunksjoner=['i', 'som', 'og', 'er', 'til', 'med', 'det', 'var', 'men', 'mens', 'at', 'en', 'for']

def caps_to_lower(wrd):
    for letter in wrd:
        if letter in caps:
            l_itr = caps.find(letter)
            wrd = wrd.replace(letter,lower[l_itr])
        if letter in all:
            pass
        else:
            # print(letter)
            wrd = wrd.replace(letter,'_')
    return wrd

def file_to_dic(fname):
    infile = open(fname, 'r', encoding='utf-8')
    dic = {}
    alf = {}
    cntr = 0
    for line in infile:
        line_words = line.split()
        for word in line_words:
            for pun in string.punctuation:
                if pun in word:
                    word = word.replace(pun,'')
            # word = caps_to_lower(word)
            if len(word)>0:
                cntr+=1
                try:
                    current = dic[word]
                    dic[word] = current+1
                except:
                    dic.update({word:1})

    sorted_by_value = sorted(dic.items(), key=lambda para: para[1], reverse=True)
    infile.close()     #Be sure to always close files
    return sorted_by_value

# glob_dic = file_to_dic("tekst.txt")

def print_table(sl, n):
    cntr =0
    print('Word        Amount')
    for ele in sl:
        #if ele[0] in conjunctions:
        if ele[0] in konjunksjoner:
            continue
        print('{:12s}|{:d}'.format(ele[0], ele[1]))
        cntr+=1
        if cntr==n:
            return

# print_table(glob_dic, 50)
