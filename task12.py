
from bs4 import BeautifulSoup
import json
import requests
url="https://www.rottentomatoes.com/m/toy_story_4"
def scrape_movie_cast(url):
    a=requests.get(url)
    soup=BeautifulSoup(a.text,"html.parser")
    main_div=soup.find("div",class_="castSection")
    div=main_div.find_all("div",class_="cast-item media inlineBlock")
    div1=main_div.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    # print(div1)
    list=[]
    for i in div:
        dict1={}
        cast=i.find("a")["href"][11:]
        dict1["Name"]=cast
        list.append(dict1)
        # print(list)
    for i in div1:
        print(i)
        dict2={}
        cast=i.find("a")["href"][11:]
        dict2["Name"]=cast
        list.append(dict2)
        # print(list)
    with open("my_task_12.json","w+")as file:
        json.dump(list,file,indent=4)
    # return 
scrape_movie_cast(url)