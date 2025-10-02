
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def is_imdb_above_5_5(x):
    if movies[x]["imdb"]>5.5:
        return True
    else:
        return False
    
print(is_imdb_above_5_5(0))

#2
def is_imdbs_above_5_5():
    x=[]
    for i in range(len(movies)):
        if movies[i]["imdb"]>5.5:
            x.append(movies[i]["name"])
    return x
print(is_imdbs_above_5_5())

#3
def is_same_category(c):
    x=[]
    for i in range(len(movies)):
        if movies[i]["category"]==c:
            x.append(movies[i]["name"])
    return x
print(is_same_category("Romance"))

#4
def avg_movies(x):
    avg=0
    for i in x:
        for j in range(len(movies)):
            if movies[j]["name"]==i:
                avg+=movies[j]["imdb"]
    return avg/len(x)
print(avg_movies(["We Two", "Exam"]))

#5
def avg_movies_category(x):
    avg=0
    cnt=0
    for j in range(len(movies)):
        if movies[j]["category"]==x:
            avg+=movies[j]["imdb"]
            cnt+=1
    return avg/cnt
print(avg_movies_category("Romance"))
