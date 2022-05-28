def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
    print(type(kwargs))

har=["Harry","Hammad","Skillf","Rohan"]
dict1={"Harry":"Monitor","Hammad":"Programmer","Shivam":"Cook"}
funargs(*har,**dict1)

def funny(n):
    print(n)
funny()