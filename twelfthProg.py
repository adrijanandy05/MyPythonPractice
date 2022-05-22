list1=[[1,5,5],[0,3,1],[2,4,4],[14,1,0]]
list1.sort()   #sorts on the basis of 1st element inside the list of the list
print(list1)
list1.sort(key=lambda x:x[1])   #sorts on the basis of 2nd element inside the list of the list
print(list1)
list1.sort(key=lambda x:x[2])   #sorts on the basis of 3rd element inside the list of list
print(list1)

a=int(input())
b=int(input())
sum=lambda x,y:x+y
print(sum(a,b))