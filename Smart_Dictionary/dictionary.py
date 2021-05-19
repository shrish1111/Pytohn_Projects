# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
from difflib import get_close_matches

data = json.load(open("C:\\Users\shris.LAPTOP-V1L17IBF\Documents\Python Real world apps\Smart Dictionary\data.json"))


def Dictionary(word):
    return data[word]

word = input("Enter a word to search: ")
word = word.lower()
if word in data.keys():
    defination = Dictionary(word)
    for i in defination:
        #print("Defination of ",word,"is ",i)
        print(i)
elif len(get_close_matches(word, data.keys()))> 0:
    print("Do you mean",get_close_matches(word, data.keys()),"?")
else:
    print("You entered wrong word, check again")
        


