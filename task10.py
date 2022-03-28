import json
with open("my_task_5.json","r+")as file:
    language_director=json.load(file)
def analyse_language_and_directors():
    dict={}
    list=[]
    for i in language_director:
        for j in i["director"]:
            if j not in list:
                list.append(j)
            # print(list)
    for x in list:
        dict1={}
        for y in language_director:
            if x in y["director"]:
                if "Language" in y:
                    a=y["Language"]
                    # print(a)
                    for g in a:
                        if g in dict1:
                            dict1[g]=dict1[g]+1
                        if g not in dict1:
                            dict1[g]=1
                    dict[x]=dict1
    with open ("my_task_10.json", "w+") as f:
        json.dump(dict,f, indent=4)
    return dict
analyse_language_and_directors()
                




