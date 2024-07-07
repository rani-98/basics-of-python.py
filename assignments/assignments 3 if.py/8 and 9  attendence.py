classesheld=int(input("number of classes held: "))
classesattended=int(input("number of classes attend: "))
percentage = (classesattended/classesheld)*100
print("attendence is",percentage)
if percentage<75:
    print("not allowed to sit in exam")
else:
    print("allowed sit in exam")
#medical cause
    print("medical cause? Y or N")
if medical_cause == "Y":
    print("allowed")
else:
    print("not allowed")
    
