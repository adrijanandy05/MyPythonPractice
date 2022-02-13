#Faulty Calculator
#Design a calculator which will return wrong answer for addition,multiplication and division. For all other operations it'll eturn correct answer
op=input("Enter your operator:")
num1=int(input("Enter your 1st no."))
num2=int(input("Enter your 2nd no."))
if op=="+":
    print(num1*num2)
elif op=="*":
    print(num1+num2)
elif op=="/":
    print(num1-num2)
elif num1>num2:
    print(num1-num2)
else:
    print(num2-num1)