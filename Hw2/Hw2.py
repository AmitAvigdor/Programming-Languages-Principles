# assignment 2
# Amit Avigdor 316178144

# Q4
def Trapez_rule(f,a,b,n):
    """
    function that gets function and calculate integral by the trapez_rule
    :param:f is the function
    :param:a is the lower bound
    :param:b is the upper bound
    :param:n is an integer
    """
    h = (b-a)/n
    sum = 0.5*(f(a)+f(b))
    for i in range(1,n):
        sum += f(a+i*h)
    trapezIntegral = h * sum
    return trapezIntegral

# Q5
def myFilter(Lst,func):
    """
    function that gets a list of numbers and a function. the myFilter function will return a fixed list of all the numbers that return True from the function.
    :param:Lst is a list of numbers
    :param: func is a list of functions
    """
    for i in range(len(Lst)):
        Lst = list(filter(func,Lst))
    return Lst

def myFilterMulti(Lst,funcL):
    """
    function that gets a list of numbers and a list of functions. myFilterMulti function will return a fixed list of all the numbers that return True from all of the function in that list.
    :param:Lst is a list of numbers
    :param: func is a list of functions
    """
    for i in range(len(funcL)):
        for j in range(len(Lst)):
            Lst = list(filter(funcL[i],Lst))
    return Lst

def myPrime(x):
    """
    function that gets number and return True if its a prime number and False if its not
    :param:x number that will be checked if prime
    """
    flag = False
    if x ==1 or x ==2:
        return True
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                flag = True
                break
        if flag:
            return False
        else:
            return True

def isFib(x):
    """
    function that gets number and return True if its a Fibonacci number and False if its not
    :param:x number that will be checked if Fibonacci
    """
    n1=0
    n2=1
    while (n1 + n2 <= x):
        for i in range(x):
            if(n1 + n2 == x):
                return True
            else:
                nTemp = n1
                n1 = n2
                n2 = nTemp + n2
    return False


print(Trapez_rule(lambda x:x**9,0.0,10.0,100000))
print(myFilter([2,4,5,6],myPrime))
print(myFilterMulti([2,4,5,6,7,13],[myPrime,isFib]))
print(myPrime(1))
print(isFib(144))
print(myFilter([1,2,4,5,6,144],isFib))
print(myFilterMulti([2,4,5,13,41,55,89,107,144],[myPrime,isFib,lambda x: x>9 and x<100]))

