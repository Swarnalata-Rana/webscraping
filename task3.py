from task2 import scrape_top_list
import json
data=scrape_top_list()
def group_by_decade(movies):
    movie_decade={}
    list1=[]
    list2=[]
    for i in movies:
        for  j in  i:
            if j ==("Year"):
                if i[j] not in list2:
                    list2.append(i[j])
    list2.sort()
    for i in list2:
        module=i%10
        mo=i-module
        if mo not in list1:
            list1.append(mo)
    for x in list1:
        movie_decade[x]=[movies]
    for x in list1:
        # print(x)
        mod=x+9
        for i in movies:
            # print(i)
            for j in i:
                # print(j)
                if j==("year"):
                    if i[j]<=mod and i[j]<=i:
                        movie_decade[x].append(movies)

        
    with open("my_task_3.json","w") as f:
        json.dump(movie_decade,f,indent = 4)
    
    return (movie_decade)

   
group_by_decade(data)