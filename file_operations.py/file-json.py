import json
with open("MOCK_DATA.json")as file:
    content=file.read()
    print(type(content))#string type
    #print(content)
    covert_json=json.loads(content)
    #print(covert_json)
    print(type(covert_json))#convert to list

with open("data.csv","w")as file:
    file.write("first_name,last_name,email,gender\n")
    for user in covert_json:
     first_name=user["first_name"]
     last_name=user["last_name"]
     email=user["email"]
     gender=user["gender"]
     file.write(f"{first_name},{last_name},{email},{gender}\n")
    
  