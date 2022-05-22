"""
def function1():
    c=print("Hello")
    return c
function1()
"""

def mean(a,b):
    """This function returns average of two nos."""
    avg=sum((a,b))/2
    return avg
print(mean.__doc__)
print(mean(4,8))