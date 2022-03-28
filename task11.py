import json
with open("my_task_5.json","r")as file:
    movies_genre=json.load(file)
    # print(movies_genre)
def analyse_movies_genre():
    dict={}
    for i in movies_genre:
        if "Genre" in i:
            j=i["Genre"]
            # print(k)
        for i in j:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
    with open("my_task_11.json","w")as file:
        json.dump(dict,file,indent=4)
analyse_movies_genre()