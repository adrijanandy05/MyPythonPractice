num1=input("Enter 1st value:")
num2=input("Enter 2nd value:")
try:
    print("The sum of these 2 values is",int(num1)+int(num2))
except Exception as e:
    print(e)
print("Rest of the code")