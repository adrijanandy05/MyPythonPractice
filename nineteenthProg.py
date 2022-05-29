#even if we del func1, func2() executes as it already stored a copy before func1 was deleted
def func1():
    print("Hello")
func2=func1
del func1
func2()

#function can return another built in function
def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
a=funcret(1)
print(a)

#function argument can be a function also
def executor(func):
    func("this")
executor(print)

#decorator concept
def dec1(func3):
    def nowexec():
        print(f"Executing now {func3}")
        func3()
        print(f"{func3} executed")
    return nowexec
@dec1
def hello_me():
    print("Hello")
hello_me()
