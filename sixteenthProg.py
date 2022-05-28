import time

l1=["A","B","C","D"]
initial=time.time()
i=1
for item in l1:
    if i%2!=0:
        print(item)
    i+=1
print(time.time()-initial)

l2=["E","F","G","H"]
initial2=time.time()

for index,item in enumerate(l2):
    if index%2==0:
        print(item)
    # i+=1
print(time.time()-initial2)
