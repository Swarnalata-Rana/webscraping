import json
from task1 import scrape_top_list
from task4 import movies_detailes
with open("my_task_1.json","r")as file:
    data=json.load(file)
movies=scrape_top_list()
# print(movies)
def get_movie_list_details():
    list=[]
    for i in data:
        a=i["URL"]
        b=movies_detailes(a)
        list.append(b)
        # print(list)
    with open ("my_task_5.json", "w+") as f:
        json.dump(list,f, indent=4)
    return list
get_movie_list_details()