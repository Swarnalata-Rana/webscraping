from bs4 import BeautifulSoup
import json
import requests
from task5 import get_movie_list_details
from task12 import scrape_movie_cast
def scrape_movie_details(url):
    list=[]
    a=get_movie_list_details(url)
    b=scrape_movie_cast(url)
    list.append(a)
    # print(list)
    list.append(b)
    with open("my_task_13.json","w")as file:
        json.dump(list,file,indent=4)
    return list

scrape_movie_details("https://www.rottentomatoes.com/m/toy_story_4")