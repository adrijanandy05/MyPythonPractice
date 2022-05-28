import time

now_time=time.localtime(time.time())
# print(now_time)

now_time=time.asctime(time.localtime(time.time()))
print(now_time)