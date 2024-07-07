data=[{"name":"alice","score":85},{"name":"bob","score":90},
{"name":"alice","score":82},{"name":"bob","score":82}]


#print(data.get("name"))
#get()
#update()
#value()
#keys()
#items()
def score():
 a={"name":"alice","score":85}
 b={"name":"bob","score":90}
 c={"name":"alice","score":82}
 d={"name":"bob","score":82}
  
score={}
for x in data:
  
    name=x["name"]
    s=x["score"]
if name in score:
    print(name,"is in score")
    score[name]=score[name]+s
else:
    print(name,"is not in score")
    score[name]=s
print(score)

    
