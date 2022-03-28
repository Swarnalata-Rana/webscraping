from task1 import scrape_top_list
import json
movie_details=scrape_top_list()
def group_by_year(movies):
    years=[]
    movie_dict={}
    for i in movies:
        year=i["Year"]
        if i not in years:
            years.append(year)
            # print(years)
    movie_dict={i:[]for i in years}
    # print(movie_dict)
    for i in movies:
        year=i["Year"]
        # print(year)
        for x in movie_dict:
            # print(x)
            if str(x)==str(year):
                movie_dict[x].append(i)
    # print(movie_dict)
    
    with open("my_task_2.json","w") as file:
        json.dump(movie_dict,file,indent=4)
    
    return movie_dict
group_by_year(movie_details)
                

