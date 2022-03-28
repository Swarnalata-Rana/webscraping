import os
import json
import random
import time
file= open("my_task_1.json","r+")
a=json.load(file)
file.close()
# b=random.randint(1,3)
def data():
    # b=random.randint(1,3)
    for i in a:
        b=random.randint(1,3)
        path="/home/admin123/Desktop/task9/task9"+i["Movie_name"]+".json"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Desktop/web_scraping/movies.txt"+i["Movie_name"]+".text","w")
            data_file=open(path,"w+")
            json.dump(i,data_file,indent=4)
        time.sleep(b)
data()
        

