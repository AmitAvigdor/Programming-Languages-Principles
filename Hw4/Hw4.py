# Assignment 4
# Amit Avigdor 316178144, Yaron Aharon Saadon  315924985
import re
import math
from functools import reduce
from operator import mul

# ############################################## PART A: ex1 ##############################################


class Time:
    def __init__(self, hours, minutes):
        '''
        set new Time object
        :param hours: of clock
        :param minutes: of clock
        '''
        self.hours = hours if hours>=0 and hours<=23 else 0
        self.minutes = minutes if minutes>=0 and minutes<=59 else 0

    def __repr__(self):
        '''
        :return: prints value for computer
        '''
        return 'Time({0}, {1})'.format(self.hours, self.minutes)

    def __str__(self):
        '''
        :return: prints value for human
        '''
        return '{:02d}:{:02d}'.format(self.hours, self.minutes)


class Event(Time):
    def __init__(self, time, data):
        '''
        set new Event object
        :param time: Time object
        :param data: data on stations
        '''
        Time.__init__(self, time.hours, time.minutes)
        self.data = data

    def __repr__(self):
        '''
        :return: prints value for computer
        '''
        return "Event({0}, '{1}')".format(Time.__repr__(self), self.data)

    def __str__(self):
        '''
        :return: prints value for human
        '''
        return '{0} - {1}'.format(Time.__str__(self), self.data)


class MedicalRecord:
    def __init__(self, name, id, data={}):
        '''
        set new Medical Record
        :param name: name of patience
        :param id: ID of patience
        :param data: data on stations of patience
        '''
        self.name = name
        self.id = id
        self.data = data

    def __repr__(self):
        '''
        :return: prints value for computer
        '''
        return "MedicalRecord('{0}',{1}, {2})".format(self.name, self.id, self.data)

    def add(self, addTime, addStation):
        '''
        add new station to the data
        :param addTime: time of arriving the station
        :param addStation: new station name to add to the data
        '''
        H, M = addTime.split(':')
        H, M = int(H), int(M)
        self.data[addTime] = Event(Time(H, M), addStation)

    def view(self):
        '''
        :return: prints all the data and values of the medical record of the patience
        '''
        print('name:',self.name)
        print('ID:',self.id)
        for i in range(len(self.data)):
            listByTime = sorted(self.data.items())
            print(f'{listByTime[i][1]}')


time1 = Time(8, 2)
time1
print(time1)
time2 = eval(repr(time1))
print(time2)

event1=Event(time1, 'registration')
print(repr(event1))

event2 = eval(repr(event1))
print(event2)
record1=MedicalRecord('David',1)
record1.add('08:02','registration')
print(record1.data)
record1.add('09:15','doctor checkup')
record1.add('08:45','doctor checkup')
record1.add('09:00','procedure')
record1.add('11:00','doctor checkup')
record1.add('09:25','radiography')
record1.add('11:30','hospital discharge')
record1.add('10:30','blood test')
record1.view()
print(record1)

# # ############################################## PART A: ex2 ##############################################


## Our custom OOP
def make_class1(attrs, base=None):  # class_name
    """Return a new class (a dispatch dictionary) with given class attributes"""

    # print(attrs)
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):
            attrs[name] = value

        # instance dictionary
        obj = {'get': get, 'set': set}

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = {'get': get, 'set': set, 'new': new}
    # ----------------
    return cls


### class TimeClass
def make_time_class():

    def __init__(self,hours, minutes):
        '''
        set new time (Shmython)
        :param self:
        :param hours: of clock
        :param minutes: of clock
        '''
        self['set']('hours', hours)
        self['set']('minutes', minutes)

    def __str__(self):
        '''
        :return: prints value for human
        '''
        return '%02d:%02d' % (self['get']('hours'), self['get']('minutes'))

    return make_class1(locals())
TimeClass = make_time_class()


### class TimeClass
def make_event_class():

    def __init__(self,time, data):
        '''
        set new event (Shmython)
        :param self:
        :param time: from time
        :param data: data on stations
        '''
        self['set']('timeObj', TimeClass['new'](time['get']('hours'), time['get']('minutes')))
        self['set']('data', data)

    def __str__(self):
        '''
        :return: prints value for human
        '''
        return "{0} - {1}".format(self['get']('timeObj')['get']('__str__')(), self['get']('data'))

    return make_class1(locals(), TimeClass)
EventClass = make_event_class()


def make_medical_record_class():

    def __init__(self,name, id, data={}):
        '''
        set new medical record (Shmython)
        :param self:
        :param name: name of patience
        :param id: ID of patience
        :param data: data on stations of patience
        '''
        self['set']('name', name)
        self['set']('id', id)
        self['set']('data', data)

    def add(self, time, name):
        '''
        add new station to the data
        :param self:
        :param time: time of arriving the station
        :param name: new station name to add to the data
        :return:
        '''
        H, M = time.split(':')
        H, M = int(H), int(M)
        self['get']('data')[time] = EventClass['new'](TimeClass['new'](H,M),name)

    def view(self):
        '''
        :return: prints all the data and values of the medical record of the patience
        '''
        print('name: {}\nID: {}'.format(self['get']('name'), self['get']('id')))
        times = [time for time in self['get']('data')]
        times.sort()
        for time in times:
            print(EventClass['get']('__str__')(self['get']('data')[time]))

    return make_class1(locals(), TimeClass)
MedicalRecordClass = make_medical_record_class()


time1=TimeClass['new'](8,2)
print(time1['get']('hours'))
print(time1['get']('__str__')())
event1=EventClass['new'](time1,'registration')
print(event1['get']('__str__')())
record1=MedicalRecordClass['new']('David',1)
record1['get']('add')('08:02','registration')
print(record1['get']('data')['08:02']['get']('__str__')())
print(record1)
record1['get']('add')('09:15','doctor checkup')
print(record1['get']('data'))
record1['get']('add')('08:45','doctor checkup')
record1['get']('add')('09:00','procedure')
record1['get']('add')('11:00','doctor checkup')
record1['get']('add')('09:25','radiography')
record1['get']('add')('10:30','blood test')
record1['get']('add')('11:30','hospital discharge')
record1['get']('view')()

# # ############################################## PART A: ex3 ##############################################

def make_class(className, attrs, base=None):  # class_name
    """Return a new class (a dispatch dictionary) with given class attributes"""

    # print(attrs)
    # Getter: class attribute (looks in this class, then base)

    def info():
        '''
        :return: adding new info about class
        '''
        if base:
            base['info']()
        print('Class: {}'.format(className))
        methods, attributes = [], {}
        for key in attrs.keys():
            if callable(attrs[key]):
                methods += [key]
            else:
                attributes[key] = attrs[key]
        print('methods:')
        for method in methods:
            print('{}'.format(method))
        print('attributes:')
        for attribute in attributes.keys():
            print('{}: {}'.format(attribute, attributes[attribute]))
        print('name: {}\n'.format(className))

    def get(name):
        if name in attrs:
            return attrs[name]
        elif name == 'name':
            return className
        elif base:
            return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):
            attrs[name] = value

        def OBJinfo():
            '''
            :return: adding info on the object
            '''
            info()
            print('object attributes:')
            for i in attrs:
                print('{}: {}'.format(i, attrs[i]))

        # instance dictionary
        obj = {'get': get, 'set': set, 'info': OBJinfo}

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = {'get': get, 'set': set, 'new': new, 'info': info}
    # ----------------
    return cls


def make_account_class():
    def __init__(self, owner, ID):
        self['set']('owner', owner)
        self['set']('ID', ID)

    return make_class('Account',{ '__init__' : __init__ , 'interest' : 0.05})

Account = make_account_class()

def make_saving_account_class():
    interest=0.075
    type_acc='saving'
    def strAccount(self):
        s=self['get']('name')+'(owner:'+self['get']('owner')+',ID:'+str(self['get']('ID'))
        return s+ ',interest:'+ str(self['get']('interest'))+')'
    return make_class('SaveAccount',locals(),Account)

SaveAccount = make_saving_account_class()

print(Account['get']('name'))
print(SaveAccount['get']('name'))
acc=SaveAccount['new']('Bob',1)
print(acc['get']('name'))
Account['info']()
acc['info']()

# # ############################################## PART B: ex4 ##############################################


class Feets:
    def __init__(self, val):
        '''
        initiate new Feet class
        :param val: value of feet
        '''
        self.val = val

    def __repr__(self):
        '''
        :return: prints value for human
        '''
        return 'Feets({0})'.format(self.val)


class Inches:
    def __init__(self, val):
        '''
        initiate new Inch class
        :param val: value of inch
        '''
        self.val = val

    def __repr__(self):
        '''
        :return: prints value for human
        '''
        return 'Inches({0})'.format(self.val)


class Centimeters:
    def __init__(self, val):
        '''
         initiate new Centimeter class
        :param val: value of centimeter
        '''
        self.val = val

    def __repr__(self):
        '''
        :return: prints value for human
        '''
        return 'Centimeters({0})'.format(self.val)

#-------------------------------add-------------------------------#
##Feets
def add_feets_feets(feet,feet2):
    '''
    adding one feet with another
    :param feet: first value
    :param feet2: second value
    :return: sum of two values
    '''
    return Feets(feet.val+feet2.val)


def add_feets_inches(feet,inch):
    '''
    adding feet to inch
    :param feet: feet value
    :param inch: inch value
    :return: sum of two values
    '''
    return Feets(feet.val+(inch.val/12))


def add_feets_centimeters(feet,centimeter):
    '''
     adding feet to centimeter
    :param feet: feet value
    :param centimeter: centimeter value
    :return: sum of two values
    '''
    return Feets(feet.val+centimeter.val/30.48)


##Inches
def add_inches_inches(inch,inch2):
    '''
    adding one inch with another
    :param inch: first value
    :param inch2: second value
    :return: sum of two values
    '''
    return Inches(inch.val+inch2.val)


def add_inches_feets(inch,feet):
    '''
    adding inch to feet
    :param inch: inch value
    :param feet: feet value
    :return: sum of two values
    '''
    return Inches(inch.val+(feet.val*12))


def add_inches_centimeters(inch,centimeter):
    '''
    adding inch to centimeter
    :param inch: inch value
    :param centimeter: centimeter value
    :return: sum of two values
    '''
    return Inches(inch.val+centimeter.val/2.54)


##Centimeters
def add_centimeters_centimeters(centimeter,centimeter2):
    '''
    adding one centimeter with another
    :param centimeter: first value
    :param centimeter2: second value
    :return: sum of two values
    '''
    return Centimeters(centimeter.val+centimeter2.val)


def add_centimeters_feets(centimeter,feet):
    '''
    adding inch to feet
    :param centimeter: centimeter value
    :param feet: feet value
    :return: sum of two values
    '''
    return Centimeters(centimeter.val+(feet.val*30.48))


def add_centimeters_inches(centimeter,inch):
    '''
    adding centimeter to inch
    :param centimeter: centimeter value
    :param inch: inch value
    :return: sum of two values
    '''
    return Centimeters(centimeter.val+(inch.val*2.54))

#-------------------------------sub-------------------------------#
##Feets
def sub_feets_feets(feet,feet2):
    '''
    sub one feet with another
    :param feet: first value
    :param feet2: second value
    :return: sub of two values
    '''
    return Feets(feet.val-feet2.val)


def sub_feets_inches(feet,inch):
    '''
    sub feet to inch
    :param feet: feet value
    :param inch: inch value
    :return: sub of two values
    '''
    return Feets(feet.val-(inch.val/12))


def sub_feets_centimeters(feet,centimeter):
    '''
     sub feet to centimeter
    :param feet: feet value
    :param centimeter: centimeter value
    :return: sub of two values
    '''
    return Feets(feet.val-centimeter.val/30.48)


##Inches
def sub_inches_inches(inch,inch2):
    '''
    sub one inch with another
    :param inch: first value
    :param inch2: second value
    :return: sub of two values
    '''
    return Inches(inch.val-inch2.val)


def sub_inches_feets(inch,feet):
    '''
    sub inch to feet
    :param inch: inch value
    :param feet: feet value
    :return: sub of two values
    '''
    return Inches(inch.val-(feet.val*12))


def sub_inches_centimeters(inch,centimeter):
    '''
    sub inch to centimeter
    :param inch: inch value
    :param centimeter: centimeter value
    :return: sub of two values
    '''
    return Inches(inch.val-centimeter.val/2.54)


##Centimeters
def sub_centimeters_centimeters(centimeter,centimeter2):
    '''
    sub one centimeter with another
    :param centimeter: first value
    :param centimeter2: second value
    :return: sub of two values
    '''
    return Centimeters(centimeter.val-centimeter2.val)


def sub_centimeters_feets(centimeter,feet):
    '''
    sub inch to feet
    :param centimeter: centimeter value
    :param feet: feet value
    :return: sub of two values
    '''
    return Centimeters(centimeter.val-(feet.val*30.48))


def sub_centimeters_inches(centimeter,inch):
    '''
    sub centimeter to inch
    :param centimeter: centimeter value
    :param inch: inch value
    :return: sub of two values
    '''
    return Centimeters(centimeter.val-(inch.val*2.54))


def type_tag(x):
    """Return the tag associated with the type of x."""
    return type_tag.tags[type(x)]


type_tag.tags = {Feets: 'Feets', Inches: 'Inches', Centimeters: 'Centimeters'}

def apply(operator_name, obj1, obj2):

    tags = (operator_name, type_tag(obj1), type_tag(obj2))
    return apply.implementations[tags](obj1, obj2)

apply.implementations={}

#-------------------------------add-------------------------------#
apply.implementations[('add','Feets', 'Feets')] = add_feets_feets
apply.implementations[('add','Feets', 'Inches')] = add_feets_inches
apply.implementations[('add','Feets', 'Centimeters')] = add_feets_centimeters

apply.implementations[('add','Inches', 'Inches')] = add_inches_inches
apply.implementations[('add','Inches', 'Feets')] = add_inches_feets
apply.implementations[('add','Inches', 'Centimeters')] = add_inches_centimeters

apply.implementations[('add','Centimeters', 'Centimeters')] = add_centimeters_centimeters
apply.implementations[('add','Centimeters', 'Feets')] = add_centimeters_feets
apply.implementations[('add','Centimeters', 'Inches')] = add_centimeters_inches

#-------------------------------sub-------------------------------#
apply.implementations[('sub','Feets', 'Feets')] = sub_feets_feets
apply.implementations[('sub','Feets', 'Inches')] = sub_feets_inches
apply.implementations[('sub','Feets', 'Centimeters')] = sub_feets_centimeters

apply.implementations[('sub','Inches', 'Inches')] = sub_inches_inches
apply.implementations[('sub','Inches', 'Feets')] = sub_inches_feets
apply.implementations[('sub','Inches', 'Centimeters')] = sub_inches_centimeters

apply.implementations[('sub','Centimeters', 'Centimeters')] = sub_centimeters_centimeters
apply.implementations[('sub','Centimeters', 'Feets')] = sub_centimeters_feets
apply.implementations[('sub','Centimeters', 'Inches')] = sub_centimeters_inches


print(apply('add',Inches(1),Centimeters(150)))
print(apply('add',Centimeters(100),Feets(1.5)))
print(apply('add',Feets(2),Inches(5)))
print(apply('sub',Inches(1.5),Centimeters(100)))
print(apply('sub',Feets(2),Inches(5)))
print(apply('sub',Centimeters(100),Inches(15)))


# ############################################## PART B: ex5 ##############################################

def feets_to_inches(x):
    '''
    converting feet to inch
    :param x: value to convert
    :return: inch value
    '''
    return Inches(x.val*12)


def feets_to_centimeters(x):
    '''
    converting feet to centimeter
    :param x: value to convert
    :return: centimeter value
    '''
    return Centimeters(x.val*30.48)


def inches_to_feets(x):
    '''
    converting inch to feet
    :param x: value to convert
    :return: feet value
    '''
    return Feets(x.val/12)


def inches_to_centimeters(x):
    '''
    converting inch to centimeter
    :param x: value to convert
    :return: centimeter value
    '''
    return Centimeters(x.val*2.54)


def centimeters_to_inches(x):
    '''
    converting centimeter to inch
    :param x: value to convert
    :return: inch value
    '''
    return Inches(x.val/2.54)


def centimeters_to_feets(x):
    '''
    converting centimeter to feet
    :param x: value to convert
    :return: feet value
    '''
    return Feets(x.val/30.48)


coercions = {('Feets', 'Inches'): feets_to_inches, ('Feets', 'Centimeters'): feets_to_centimeters,
             ('Inches', 'Feets'): inches_to_feets, ('Inches', 'Centimeters'): inches_to_centimeters,
             ('Centimeters', 'Inches'): centimeters_to_inches, ('Centimeters', 'Feets'): centimeters_to_feets}

def coerce_apply(operator_name, obj1, obj2):

    tobj1, tobj2 = type_tag(obj1), type_tag(obj2)
    if tobj1 != tobj2:
        if (tobj1, tobj2) in coercions:
            tobj1, obj1 = tobj2, coercions[(tobj1, tobj2)](obj1)
        elif (tobj2, tobj1) in coercions:
            tobj2, obj2 = tobj1, coercions[(tobj2, tobj1)](obj2)
        else:
            return 'No coercion possible.'
    assert tobj1 == tobj2
    key = (operator_name, tobj1)
    return coerce_apply.implementations[key](obj1, obj2)

coerce_apply.implementations = {('add', 'Feets'): add_feets_feets,
                                ('add', 'Inches'): add_inches_inches,
                                ('add', 'Centimeters'): add_centimeters_centimeters,
                                ('sub', 'Feets'): sub_feets_feets,
                                ('sub', 'Inches'): sub_inches_inches,
                                ('sub', 'Centimeters'): sub_centimeters_centimeters}


print(coerce_apply('add',Inches(1),Centimeters(150)))
print(coerce_apply('add',Centimeters(100),Feets(1.5)))
print(coerce_apply('add',Feets(2),Inches(5)))
print(coerce_apply('sub',Inches(1.5),Centimeters(100)))
print(coerce_apply('sub',Feets(2),Inches(5)))
print(coerce_apply('sub',Centimeters(100),Inches(15)))


# ############################################## PART C: ex6 ##############################################

def make_medical_Record(name,num):
    '''
    represents medical files using dictionary
    :param name: the name of the patient
    :param num: file number
    '''

    try:
        if (type(name) != str or type(num) != int):
            raise TypeError('TypeError')

    except TypeError:
        print(TypeError('{0}: invalid parameters type \nname: {1}\nID: {2}'.format(TypeError, type(name), type(num))))
        return


    medicalFile={}
    timeFile={}
    def addData(t,n):
        try:
            if len(t) != 5:
                raise TypeError('TypeError')

        except TypeError:
            print(TypeError('{0}: invalid time format XX:XX\ntime: {1}'.format(TypeError, t)))
            return

        if t[0] == '2':
            try:
                if not re.match(r"[2][0-3][:][0-5][0-9]", t):
                    raise TypeError('TypeError')

            except TypeError:
                print(TypeError('{0}: invalid time value\ntime: {1}'.format(TypeError, t)))
                return

        else:
            try:
                if not re.match(r"[0-1][0-9][:][0-5][0-9]", t):
                    raise TypeError('TypeError')

            except TypeError:
                print(TypeError('{0}: invalid time value\ntime: {1}'.format(TypeError, t)))
                return

        nonlocal medicalFile
        stationList = ('registration', 'doctor checkup', 'procedure', 'radiography', 'blood test', 'hospital discharge')

        try:
            if n not in stationList:
                raise ValueError('ValueError')

        except ValueError:
            print(ValueError('{0}: this event not possible\nevent: {1}'.format(ValueError, n)))
            return

        try:
            if (n == 'registration' or n == 'hospital discharge') and n in medicalFile.keys():
                raise ValueError('ValueError')

        except ValueError:
            print(ValueError('{0}: this event is present\nevent: {1}'.format(ValueError, n)))
            return

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
            try:
                print(f'{listByTime[i][0]}:{listByTime[i][1]}')
                i += 1
            except IndexError:
                return print(IndexError('{0}: list index out of range'.format(IndexError)))

        def hasMore():
            nonlocal i
            if i == len(timeFile):
                return False
            else:
                return True

        return {'hasMore': hasMore,'next': next}
    return {'inData':inData,'notInData':notInData,'addData':addData,'view':view,'printRecord':printRecord }



mr=make_medical_Record(1,'David')
mr=make_medical_Record('David',1)
mr['addData']('11:30:20','registration')
mr['addData']('11:3','registration')
mr['addData']('11:62','registration')
mr['addData']('11:30','registration')
mr['addData']('11:40','registration')
mr['addData']('11:40','abcd')
mr['addData']('12:50','doctor checkup')
mr['addData']('11:40','doctor checkup')
mr['addData']('12:40','procedure')
mr['addData']('13:30','radiography')
mr['addData']('13:40','blood test')
mr['addData']('15:00','hospital discharge')
pr=mr['printRecord']()
pr['next']()
for _ in range(8):
    pr['next']()


# ############################################## PART D: ex7 ##############################################

class Tree():
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        if not self.left and not self.right:
            return "Tree({0})".format(repr(self.entry))
        return "Tree({0},{1},{2})".format(repr(self.entry),repr(self.left),repr(self.right))


def build_tree(tree):
    '''
    build new tree
    :param tree: tree object
    :return: printing Tree
    '''
    if type(tree) != tuple:
        return tree
    return eval('Tree{}'.format(tuple(map(build_tree, tree))))


def max_tree(tree):
    '''
    finds the max value on the tree
    :param tree: tree object
    :return: max value
    '''
    if tree.left is None and tree.right is None:
        return tree.entry

    max_index = tree.entry
    left_val = max_tree(tree.left)
    right_val = max_tree(tree.right)

    if left_val>max_index:
        max_index = left_val

    if right_val>max_index:
        max_index = right_val

    return max_index


def min_tree(tree):
    '''
    finds the min value on the tree
    :param tree: tree object
    :return: min value
    '''
    if tree.left is None and tree.right is None:
        return tree.entry

    min_index = tree.entry
    left_val = min_tree(tree.left)
    right_val = min_tree(tree.right)

    if left_val<min_index:
        min_index = left_val

    if right_val<min_index:
        min_index = right_val

    return min_index


def is_BST_tree(tree):
    '''
    check if tree is BST
    :param tree: tree object
    :return: True if BST or False if not
    '''
    if tree.left is None and tree.right is None:
        return True
    left_val = max_tree(tree.left)
    right_val = min_tree(tree.right)

    if left_val > tree.entry:
        return False
    if right_val < tree.entry:
        return False
    if is_BST_tree(tree.left) and is_BST_tree(tree.right):
        return True

    return False


tree1 = (12, (6, (2,), (8,)), (15, (14,), (18,)))
t1=build_tree(tree1)
print(t1)
print(max_tree(t1))
tree2 = (12, (6, (2,), (8,)), (15, (7,), (20,)))
t2=build_tree(tree2)
print(t2)
print(min_tree(t2))
print(is_BST_tree(t1))
print(is_BST_tree(t2))


# ############################################## PART E: ex8 ##############################################
"""Calculator

An interpreter for a calculator language using prefix-order call syntax.
Operator expressions must be simple operator names or symbols.  Operand
expressions are separated by commas.

"""


def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return


# Eval & Apply

class Exp(object):
    """A call expression in Calculator.

    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)


def calc_eval(exp):
    """Evaluate a Calculator expression.

    """
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def calc_apply(operator, args):
    """Apply the named operator to a list of args.

    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer / denom

    if operator in ('sqrt', 'V'):
        if len(args) != 1:
            raise TypeError(operator + ' requires exactly 1 argument')
        return math.sqrt(args[0])

    if operator in ('round', '~'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 argument')
        if type(args[1]) != int:
            raise TypeError(operator + ' A second parameter must be integer')
        return round(args[0], args[1])

    if operator in ('weight', '&'):
        if len(args) != 1:
            raise TypeError(operator + ' requires exactly 1 argument')
        if type(args[0]) != int:
            raise TypeError('{} is not {}'.format(args[0], int))
        return int(''.join((map(lambda n: str(10-n), filter(lambda n: n != 0, list(int(i) for i in str(args[0])))))))


# Parsing
def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree


def tokenize(line):
    """Convert a string into a list of tokens.

    """
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.strip().split()


known_operators = ['add', 'sub', 'mul', 'div', 'sqrt', 'round', 'weight', '+', '-', '*', '/', 'V', '~', '&']


def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.

    Operand expressions can be separated by commas, spaces, or both.

    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)


def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands


def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


def run():
    read_eval_print_loop()


run()




