# Assiment 1
# Amit Avigdor 316178144 ,Shir Benishu 207465840

print("---------------------ex1----------------------------")

def geometric_progression(a,q,n):
    """
    Function that will print geometric series using 3 parameters.
    :param a: is an integer
    :param q: is the jumps between numbers in the series
    :param n: is the size of the series
    """
    print("The geometric series is: ")
    for i in range (n):
        print(a,end='')
        if i != (n-1):
            print(",",end='')
        else:
            print("\n")
        a = a * q
geometric_progression(3,2,5)
geometric_progression(-2,4,6)
geometric_progression(6,-3,3)
print("---------------------ex2----------------------------")
def reverse(num):
    """
    Function that gets integer and will reverse it
    """
    revNum = 0
    while(num > 0):
     unitDig = num %10
     revNum = (revNum *10) + unitDig
     num = num //10
    return revNum
print("\n The revese number is: ",reverse(4596))
print("\n The revese number is: ",reverse(0))
print("\n The revese number is: ",reverse(55555))
print("---------------------ex3----------------------------")
def removeDigit(number,n):
    """
    Function that will remove a digit using 2 parameters.
    :param number: is an integer
    :param n: is the number that we would like to remove.
    """
    i=1
    newNum=0
    while (number > 0):
        temp = number %10
        if(temp != n):
            newNum = (temp*i) + newNum
            i=i*10
        number = number // 10
    return newNum
print("\n The new number is: ",removeDigit(78452813,8))
print("\n The new number is: ", removeDigit(3333,5))
print("\n The new number is: ",removeDigit(4444,4))
print("---------------------ex4----------------------------")
def figure(n):
    """
    Function that gets integer and prints a triangle in the size of that integer.
    :param n: is a Single digit
    """
    for k in range (n):
        for i in range (n-k):
            print(" ",end='')
        for j in range(1,k+2):
            print(j,end='')
        print("\n")
figure(8)
print("---------------------ex5----------------------------")
def printEvenDigits(number):
    """
    Recursive function that will print only the even numbers using 1 parameter
    :param number: an integer
    """
    if number > 0 :
        if number % 2 == 0:
            tempNum= number % 10
            number = number // 10
            printEvenDigits(number)
            print(tempNum,end='')
        else:
            number = number // 10
            printEvenDigits(number)
printEvenDigits(154682)
print("\n")
printEvenDigits(223)
print("\n")
printEvenDigits(5555)
print("\n")
printEvenDigits(4444)
print("\n")
print("---------------------ex6----------------------------")
def mulPrimeNumbers(number):
    """
    Function that will multiply only the prime numbers and return its answer
    :param number: an integer
    """
    mul =1
    flag = 0
    while number > 0:
        singleNum = number % 10
        if (singleNum == 1) or (singleNum == 2) or (singleNum == 3) or (singleNum == 5) or (singleNum == 7):
            mul = mul * singleNum
            flag = 1
        number = number // 10
    if flag == 0:
        return 0
    return mul
print("The multiplication result is: ",mulPrimeNumbers(124563))
print("The multiplication result is: ",mulPrimeNumbers(1875964))
print("The multiplication result is: ",mulPrimeNumbers(4444))
print("---------------------ex7----------------------------")
def luckyNumber(number):
    """
    Function that gets 6 figures and decide if its lucky number or not.
    to get a lucky number the sum of the first 3 digits needs to be even to the multiplication of the last 3 digits
    if its even the function will return True.
    else False
    """
    mul = 1
    sum = 0
    while number > 0:
        for i in range (3):
            singleNum = number % 10
            sum = sum + singleNum
            number = number // 10
        for i in range (3):
            singleNum = number % 10
            mul = mul * singleNum
            number = number // 10
    if sum == mul:
        return True
    return False
print("The answer is: ",luckyNumber(118242))
print("The answer is: ",luckyNumber(622888))
print("The answer is: ",luckyNumber(554651))




























