#list1=["Hello","How","Are"]
#print(list1)

list1=[["Harry",1],["Larry",2],["Carie",3],["Marie",4]]
for item in list1:
    print(item)
for item,l1 in list1:
    print(item,l1)
dict1=dict(list1)
print(dict1)
for item in dict1:
    print(item)
for item,lollipop in dict1.items():
    print(item,lollipop)



list2=["Harry",76,"Pray",89,5]
for item in list2:
    if str(item).isnumeric() and item>6:
        print(item)
    else:
        print("Invalid")
