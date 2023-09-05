# Assignment 3
# Amit Avigdor 316178144
import math
print("---------------------Part A---------------------")
print("---------------------ex1---------------------")
def make_circle(x, y, radius):
    """making immutable type of a circle using dispatch
    :param x: is the x coordinates of the circle
    :param y: is the y coordinates of the circle
    :param radius: is the radius of the circle
    """
    def dispatch(index):
        if (index) == 0:
            return x
        elif (index) == 1:
            return y
        elif (index) == 2:
            return radius
    return dispatch


def x(circle):
    """
    gets a circle and return coordinates of x
    :param circle: gets a circle
    """
    return circle(0)


def y(circle):
    """
    gets a circle and return coordinates of y
    :param circle: gets a circle
    """
    return circle(1)


def radius(circle):
    """
    gets a circle and return its radius
    :param circle: gets a circle
    """
    return circle(2)


def print_circle(circle):
    """
    gets a circle and print it
    :param circle: gets a circle
    """
    print("Circle: point = (", x(circle), ",", y(circle), "); radius =", radius(circle))


def perimeter(circle):
    """
    gets a circle and returns the perimeter
    :param circle:gets a circle
    """
    return 2*math.pi*radius(circle)


def area(circle):
    """
    gets a circle and returns the area
    :param circle:gets a circle
    """
    return math.pi*(radius(circle))*(radius(circle))


def distance(c1, c2):
    """
    gets two circles and returns the distance between them
    :param c1: first circle
    :param c2: second circle
    """
    return math.hypot(x(c2) - x(c1), y(c2) - y(c1))


def replace(c1,x,y):
    """
    gets a circle and new coordinates of the center of the circle and returns a new circle with new center
    :param c1: a circle
    :param x: new coordinates
    :param y: new coordinates
    :return: a new circle with new center
    """
    return make_circle(x,y,radius(c1))


def set_radius(c1,radius):
    """
    :param c1: a circle
    :param radius: a new radius
    :return: a new circle with the new radius
    """
    return make_circle(x(c1),y(c1),radius)


def add(c1,c2):
    """
    :param c1: first circle
    :param c2: second circle
    :return: a new circle with the sum of c1 and c2 radius and placing it in the middle of both circles
    """
    newRadius = radius(c1)+radius(c2)
    averageX = (x(c1)+x(c2))/2
    averageY = (y(c1) + y(c2))/2
    return make_circle(averageX,averageY,newRadius)


c1 = make_circle(4,5,10)
print(c1)
print(x(c1))
print(y(c1))
print(radius(c1))
print_circle(c1)
print(perimeter(c1))
print(area(c1))
print(distance(c1, make_circle(7,4,5)))
print_circle(replace(c1, 6, -7))
print_circle(set_radius(c1, 9))
print_circle(replace(set_radius(c1, 5), 1.5, 3.2))
c2 = make_circle(4, 6, 7)
print_circle(add(c1,c2))
print_circle(add(c2,add(c1,set_radius(make_circle(1,2,3),1))))

print("\n---------------------ex2---------------------")
def make_date(d,m,y):
    """
    :param d: gets a day
    :param m: gets a month
    :param y: gets a year
    :return: a full date, or dispatch
    """
    def dispatch(index):
        if (index) == 0:
            return d
        elif (index) == 1:
            return m
        elif (index) == 2:
            return y
    return dispatch


def day(date):
    """
    :param date: gets a date
    :return:the day of that date
    """
    return date(0)


def month(date):
    """
    :param date: gets a date
    :return: the month of that day
    """
    return date(1)


def year(date):
    """
    :param date: gets a date
    :return: the year of that date
    """
    return date(2)


def print_date(date,str):
    """
    :param date: gets a date
    :param str: a string that according to it the date format will be printed
    """
    if (date == None):
        return
    if(str == 'mdy'):
        print(month(date),"/",day(date),"/",year(date))
        return

    if (str == 'ymd'):
        print(year(date),"/",month(date),"/",day(date))
        return

    if (str == 'dmy'):
        print(day(date),"/",month(date),"/",year(date))
        return
    else:
        print("Error date format!")
        return


def next_date(date):
    """
    :param date: gets a date
    :return: the day after
    """
    if (month(date) == 1 or month(date) == 3 or month(date) == 5 or month(date) == 7 or month(date) == 8 or month(date) == 10 or month(date) == 12):
        maxDays = 31
    if (month(date) == 4 or month(date) == 6 or month(date) == 9 or month(date) == 11):
        maxDays = 30
    if (month(date) == 2):
        maxDays = 28
    if (maxDays == 31 or maxDays == 30 or maxDays ==28):
        if(month(date) == 12):
            return make_date(1,1,year(date)+1)
        if (day(date) == maxDays):
            return make_date(1, month(date) + 1, year(date))
        if (maxDays < day(date)):
            print("Error Day")
            return None
        if (maxDays > day(date)):
            return make_date(day(date)+1, month(date), year(date))


def set_day(date,day):
    """
    :param date: gets a date
    :param day: gets a day
    :return: a new date with the new day
    """
    if ( month(date) == 1 or  month(date)== 3 or  month(date)== 5 or  month(date) == 7 or  month(date) == 8 or  month(date) == 10 or  month(date) == 12):
        maxDays = 31
    if ( month(date) == 4 or month(date) == 6 or  month(date) == 9 or  month(date) == 11):
        maxDays = 30
    if ( month(date) == 2):
        maxDays = 28
    if (day < 1):
        print("Error day")
        return None
    if (maxDays < day):
        print("Error day")
        return None
    return make_date(day,month(date),year(date))

def set_month(date,month):
    """
    :param date: gets a date
    :param month: gets a month
    :return: a new date with the new month
    """
    if(month > 12 or month < 1):
        print("Error month")
        return
    if (month== 1 or month== 3 or month== 5 or month == 7 or month == 8 or month == 10 or month == 12):
        maxDays = 31
    if (month == 4 or month == 6 or month == 9 or month == 11):
        maxDays = 30
    if (month == 2):
        maxDays = 28
    if (maxDays < day(date)):
        print("Day-Month inconsistency")
        return None
    return make_date(day(date),month,year(date))


def set_year(date,year):
    """
    :param date: gets a date
    :param year: gets a year
    :return: a new date with the new year
    """
    if (year > 2050 or year < 1900):
        print("Error year")
        return
    return make_date(day(date),month(date),year)


def diff(date1,date2):
    """
    :param date1: first date
    :param date2: second date that contains the same month and year as the first date
    :return: the amount of days between them, or -1 if the dates has a different month or year
    """
    if(month(date1)!=month(date2) or year(date1) !=year(date2)):
        return -1
    return abs(day(date1) - day(date2))


d = make_date(23,6,2021)
print(d)
print(day(d))
print(month(d))
print(year(d))
print_date(d,'mdy')
print_date(d,'dmy')
print_date(d,'ymd')
print_date(d,'ydm')
print_date(set_year(d, 1890), 'dmy')
print_date(set_year(d, 2018), 'dmy')
print_date(set_month(d, 14), 'dmy')
print_date(set_month(make_date(30, 6, 2020), 2), 'dmy')
print_date(set_month(d, 11), 'dmy')
print_date(set_day(d,0), 'dmy')
print_date(set_day(d,31), 'dmy')
print_date(set_day(d,30), 'dmy')
print_date(set_year(set_month(set_day(d,15),7),2015),'dmy')
print_date(next_date(make_date(25, 7, 2021)),'dmy')
print_date(next_date(make_date(31, 7, 2021)),'dmy')
print_date(next_date(make_date(31, 12, 2021)),'dmy')
print_date(next_date(next_date(next_date(make_date(27,2,2010)))),'dmy')
print(diff(make_date(26,4,1999),make_date(15,4,1999)))

print("\n---------------------Part B---------------------")
print("---------------------ex1---------------------")

def convert(lst):
    """
    :param lst: a list of integers
    :return: a fixed list with the numbers between 0 to 100 which is sorted by the grades: A,B,C,D,Fail
    """""
    lstA = list(filter(lambda x: x >=91 and x <=100,lst))
    lstB=  list(filter(lambda x: x >= 81 and x <= 90, lst))
    lstC = list(filter(lambda x: x >=71 and x <= 80, lst))
    lstD = list(filter(lambda x: x >= 56 and x <= 70, lst))
    lstF = list(filter(lambda x: x <=56 and x >= 0, lst))
    if(lstA==[]):
        return (('A:'),lstA),(('B:'),lstB),(('D:'),lstD),(('Fail:'),lstF)
    if(lstB == []):
        (('A:'), lstA),(('C:'), lstC), (('D:'), lstD), (('Fail:'), lstF)
    if (lstC == []):
        return (('A:'),lstA),(('B:'),lstB),(('D:'),lstD),(('Fail:'),lstF)
    if (lstD == []):
        (('A:'), lstA), (('B:'), lstB), (('C:'), lstC), (('Fail:'), lstF)
    if (lstF == []):
        (('A:'), lstA), (('B:'), lstB), (('C:'), lstC), (('D:'), lstD)
    else:
        (('A:'), lstA), (('B:'), lstB), (('C:'), lstC), (('D:'), lstD), (('Fail:'), lstF)


lst = (20, 45, 90, 3, 68, -30, 81, 98, 104, 63, 61)
print(convert(lst))

print("\n---------------------ex2---------------------")


def fact(listOflists, factor):
    '''
    :param listOflists: list of grades
    :param factor: factor to multiply the grades
    :return: returns list of minimum grade, maximum grade and average of each list
    '''
    lstAfterFactor = (tuple(map(lambda x: tuple(map(lambda x: x*factor if x*factor <=100 else (100),x)), listOflists)))
    lstAfterFactor = (tuple(map(lambda x:(min(x),max(x),sum(x)/len(x)),lstAfterFactor)))

    return lstAfterFactor


lst = ((30, 80, 72, 40), (24,), (88, 50, 34, 90, 56))
print(fact(lst,1.5))


print("\n---------------------Part C---------------------")
print("---------------------ex4---------------------")


def make_currency(value,curr):
    '''
    Creates new data type named currency with the ability to get values, set values, converting the values and printing
    :param value: the value of the new currency
    :param curr: the mark representing of the new currency
    '''
    def get_value(y):
        if y == 'symbol':
            return curr
        if y == 'amount':
            return f'{value}'

    def set_value(y, z):
        nonlocal value
        if y == 'amount':
            value = z

    def convert(y, z):
        nonlocal value, curr
        curr = z
        value = y(value)

    def dispatch(x):
        if x == 'get_value':
            return get_value
        elif x == 'set_value':
            return set_value
        elif x == 'str':
            return f'{curr}{value:.2f}'
        elif x == 'convert':
            return convert
        else:
            return "Error"
    return dispatch


c = make_currency(10.50,'$')
print(c)
print(c('get_value')('amount'))
print(c('get_value')('symbol'))
c('set_value')('amount', 50)
print(c('get_value')('amount'))
print(c('str'))
(c('convert')(lambda x: x*3.87, '₪'))
print(c('str'))

print("\n---------------------ex5---------------------")


def make_medical_Record(name,num):
    '''
    represents medical files using dictionary
    :param name: the name of the patient
    :param num: file number
    '''
    medicalFile={}
    timeFile={}
    def addData(t,n):
        nonlocal medicalFile
        if n not in medicalFile.keys():
            medicalFile[n] = [t,]
        else:
            medicalFile[n].append(t)
            medicalFile[n].sort()

        if t not in timeFile.values():
            timeFile[t] = n
        else:
            timeFile[t].append(n)

    def inData(station):
        return True if (station in medicalFile.keys()) else False

    def notInData(station):
        return True if (station not in medicalFile.keys()) else False

    def view(station):
        if inData(station) == True:
            for i in range (len(medicalFile[station])):
                if i!= medicalFile[station]:
                    print(medicalFile[station][i],",",end='' )
        else:
            print('\nno events')

    def printRecord():
        i=0
        print(name,num)
        def next():
            nonlocal i
            listByTime = sorted(timeFile.items())
            print(f'{listByTime[i][0]}-{listByTime[i][1]}')
            i+=1

        def hasMore():
            nonlocal i
            if i == len(timeFile):
                return False
            else:
                return True

        return {'hasMore': hasMore,'next': next}
    return {'inData':inData,'notInData':notInData,'addData':addData,'view':view,'printRecord':printRecord }


mr=make_medical_Record('David',1)
print(mr)
mr['addData']('11:30','registration')
print(mr['inData']('registration'))
print(mr['inData']('registration'))
print(mr['inData']('procedure'))
print(mr['notInData']('procedure'))
mr['addData']('12:50','doctor checkup')
mr['addData']('11:40','doctor checkup')
mr['addData']('12:40','procedure')
mr['addData']('14:30','doctor checkup')
mr['addData']('13:30','radiography')
mr['addData']('13:40','blood test')
mr['view']('doctor checkup')
mr['view']('hospital discharge')
mr['addData']('15:00','hospital discharge')
pr=mr['printRecord']()
print(pr)
pr['next']()
while pr['hasMore']():
    pr['next']()


