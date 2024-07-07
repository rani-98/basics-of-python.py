
#write and appen method
s=open("fruits.txt","w")
s.write("first line of python code class\n")
s.close()

#read mehod
with open ("fruits.txt") as file:
    content=file.read()
    print(content)

    print("end of the program")