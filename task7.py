import json
import requests
from bs4 import BeautifulSoup
with open("my_task_5.json","r")as file:
    a=json.load(file)
    # print(a)
def analyse_movies_director():
    dict={}
    for i in a:
        # print(i)
        if "director" in i:
            directors=i["director"]
            # print(director)
            for i in directors:
                if i not in dict:
                    dict[i]=1
                else:
                    dict[i]+=1
    with open ("my_task_7.json", "w+") as file:
        json.dump(dict,file, indent=4)
    # return list
analyse_movies_director()
    