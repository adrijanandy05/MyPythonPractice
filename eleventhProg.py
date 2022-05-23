def fact(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

num=int(input("Enter a number: "))
print("Factorial of the number is ",fact(num))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
num1=int(input("Enter a number: "))
print("Fibonacci number is ",fib(num1))