"""
l=10  #global ariable
def func1(n):
    l=5  #local variable
    print(l)  #will print the local variable if defined any otherwise will print the global variable
    print(n,"I have printed")
print(l)  #will print the global variable
func1("Hello")
print(l)  #even after calling the function once before, l takes the value of the global variable
"""
x=90
def harry():
    x=20
    def rohan():
        global x
        x=88
        print(x)
    rohan()
    print(x)  #prints 20 because it first looks for local variable inside function and then goes for global variable
print(x)
harry()
print(x)   #prints 88 because it first looked in global variable but after calling harry() it saw "global" keyword which changed the global variable so it took the changed value

"""
x=90
def harry():
	x=20
	def rohan():
		global x
		x=88
	print(x)    ------> takes the value of local variable of harry() so prints 20
	rohan()   
	print(x)   --------> takes the value of local variable of harry() so prints 20
harry()  ------> 20 20
print(x) -------> will change the x value to the global one so prints 88 even though its defined outside as 90 but since "global" been used inside the function so will change the value to 88
"""