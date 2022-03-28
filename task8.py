import json
import requests
import os
# from task1 import scrape_top_list
with open ("my_task_1.json","r+") as file:
    a=json.load(file)
# data=scrape_top_list()
def scrape_movie_details ():

    for i in a:
        # print(i)
        path="/home/admin123/Desktop/web_scraping/movies.txt"+i["Movie_name"]+".text"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Desktop/web_scraping/movies.txt"+i["Movie_name"]+".text","w")
            url=requests.get(i["URL"])
            create1=create.write(url.text)
            create.close()

scrape_movie_details()
