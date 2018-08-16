#create playist

playlist=[{
    "name":"a",
    "singer1":"a1",
    "singer2":"a2",
    "year":2017
},{"name":"b",
    "singer1":"b1",
    "singer2":"b2",
    "year":2014},
    {"name":"c",
    "singer1":"c1",
    "singer2":"",
    "year":2013},{"name":"d",
    "singer1":"d1",
    "singer2":"",
    "year":2012},{"name":"e",
    "singer1":"e1",
    "singer2":"e2",
    "year":2010},{"name":"f",
    "singer1":"f1",
    "singer2":2013,
    "year":""}]



print(len(playlist))
for s in playlist:
    for k,v in s.items():
        print(f"{k}: {v}",end="   ")
        #print("")
    print("")