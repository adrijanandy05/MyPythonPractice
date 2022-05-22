import datetime

def getDateTime():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c=int(input("Enter 1 for food or 2 for exercise:"))
        if (c==1):
            value=input("Type here:\n")
            with open("june-food.txt","a") as f:
                f.write(str([str(getDateTime())])+":"+value+"\n")
            print("Successfully written")
        elif c==2:
            value=input("Type here:\n")
            with open("june-ex.txt","a") as f:
                f.write(str([str(getDateTime())])+":"+value+"\n")
            print("Successfully written")
        else:
            print("Enter valid input")
    elif k==2:
        c=int(input("Enter 1 for food or 2 for exercise"))
        if c==1:
            value=input("Type here:\n")
            with open("ria-food.txt","a") as f:
                f.write(str([str(getDateTime())])+": "+value+"\n")
            print("Successfully written")
        elif c==2:
            value=input("Type here:\n")
            with open("ria-ex.txt","a") as f:
                f.write(str([getDateTime()])+": "+value+"\n")
            print("Successfully written")
        else:
            print("Enter valid input")
    else:
        print("Enter valid input")

def retrieve(k):
    if k==1:
        c=int(input("Enter 1 to retrieve food data or 2 to retrieve exercise data"))
        if c==1:
            with open("june-food.txt") as f:
                a=f.read()
            print(a+"\n")
        elif c==2:
            with open("june-ex.txt") as f:
                a=f.read()
            print(a+"\n")
        else:
            print("Enter valid input")
    elif k==2:
        c = int(input("Enter 1 to retrieve food data or 2 to retrieve exercise data"))
        if c == 1:
            with open("ria-food.txt") as f:
                a = f.read()
            print(a + "\n")
        elif c == 2:
            with open("ria-ex.txt") as f:
                a = f.read()
            print(a + "\n")
        else:
            print("Enter valid input")
    else:
        print("Enter valid input")
print("Health Management System:\n")
a=int(input("Enter 1 to log and 2 to retrieve: "))
if a==1:
    b=int(input("Enter 1 for June and 2 for Ria: "))
    take(b)
elif a==2:
    b=int(input("Enter 1 to retrieve June's data or 2 to retrieve Ria's data:\n"))
    retrieve(b)