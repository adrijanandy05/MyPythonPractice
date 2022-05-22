"""
f=open("anyProg.txt")
content=f.read()
print(content)
f.close()

f=open("anyProg.txt","a")
h=f.write("\tBye")
print(h)  #points where the cursor is currently in the file which it's reading
f.close()

f=open("anyProg.txt","r")
f.seek(10)
c=f.read()
print(c)
f.seek(5)
print(f.tell())

f=open("anyProg.txt")
print(f.tell())
"""
with open("anyProg.txt") as f:
    c=f.read()
    print(c)
f=open("anyProg.txt")
g=f.read()
print(g)


