print("Enter the no. of rows:")
rows=int(input())
print("Type 1 or 0")
c=int(input())
a=bool(c)
if a==True:
    for i in range(0,rows):
        for j in range(0,i+1):
            print("*",end="")
        print()
else:
    for i in range(rows,0,-1):
        for j in range(0,i):
            print("*",end="")
        print()