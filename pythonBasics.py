import time
# age=21
# age=age+2
# print (age *2)
# print(type(age))


# name= "priya"
# print(name)
# print(type(name))
# print(name + " age is :" + str(age))

# height= 23.990
# print(height)
# print(type(height))
# print("hello cutie " + str(height))

# human= True
# print(type(human))
# print("My baby is heelo?" + str(human))
# print(human)

# prya = hhsjd = saurabh = nikhil = "hiran"
# print(prya)
# print(40)

# name= "priya yadav"
# print(len(name))
# print(name.find('o'))
# print(name.capitalize())
# print(name.upper())
# print(name.isdigit())
# print(name.isalpha())
# print(name.replace('a','s'))

# x=1
# y=1.0988
# z="98"
# print(type(int(y)))
# print(type(y))
# print(type(str(y)))

# y= int(y)
# z= float(z)
# print(z)
# z= bool(z)
# print(y)
# print(z)

# name= input("what name?")
# age = int(input("old: "))
# height= float(input("height: ?"))

# print("hello" + name)
# print("you are" + str(age) + str(height))

# #[start:stop:set]
# name= "Bro code"
# firstname= name[2]
# lastname=name[:3]
# funkyname= name[::2]  //2 -2 skip krke
# print(funkyname)
# reversedame=name[::-1] //reverse
# print(reversedame)
# print(firstname)
# print(lastname)

# website1= 'http:ljhdieu.com'
# slice = slice(7,-1)
# print(website1[slice])

# age = int(input('how old? '))
# if age>=18:
#     print("i m cute")

# elif age < 0:
#     print('you r still in belly')

# else:
#     print('you are child!')

# l=2
# while l==1:
#     print("cute")

# for i in range(10):
#     print(i+1)

# for minutes in 'priya yadav':
#     time.sleep(1)
#     print(minutes)

# for i in range(50,200,2):
#     print(i)

# for i in range(

# break= use to break the loop entirely;
# continue- to skip the uteration
# pass= do nothing and act lke as a placehold3r

# while True:
#     name=input("Enter name:")
#     if name!="":
#         break
#     print("your beautiful name is  " + name)

# food = ['piza', 'wtd', 'hekkd', 'gol']
# food[1]='sushi'
# food.pop()
# food.append('you')
# food.sort()
# food.clear()
# for x in food:
#     print(x)

# tuple = collection whhihch is ordered and unchangeable used to group together related data
# student = ("Bro", 21, 'male')
# print(student.count('Bro'))
# print(student.index('male'))

# for i in student:
#     print(i)
# if "Bro" in student:
#     print("good")

# set = collection which is unordered and unindexed , no duplicate value
# utensils = {"fork", 'spoon', 'knife', 'cup', 'cup'}
# ute={'fg', 'd', 'e'}
# utensils.add('napkin')
# utensils.remove('cup')
# asde = utensils.union(ute)
# utensils.update(ute)
# print(utensils.intersection(ute))
# for x in utensils:
#     print(x)
# for i in asde:
#     print(i)


# dictionary = changeable,unordered collection of unique key:value pairs 
# this is fast because they use hashing which allow us to access a value quickly

# capit = {'USA': 'dd', 'ssd': 'ashs', 'asd': 'aaa'}
# print(capit.get('fee'))
# capit.update({'fee' : 'dd'})
# print(capit.keys())
# print(capit.values())
# # print(capit.items())
# for key,value in capit.items():
#     print(key,value)
# capit.pop('USA')
# print(capit.items( ))

# def hello(first,last,age):
#     print('hello' + first + last)
# hello("Bro","uhd",21)

# keyword argument = argument preceded by identifier when to pass them to fxn
# def hello(first,middle,last):
#     print('hello' + first + middle + last);
# hello(last = 'code' , first = 'gsfd' , middle = 'dude')

# nested function calls = 
# print(round(abs(float(input('enter hhd : ')))))

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accepta verying amount of arguments.

# def add(*args):
#     sum=0
#     # tupes are inchangabel
#     # args[0]=1
#     # list ca be chnaged
#     args=list(args)
#     args[0]=0
#     for i in args:
#         sum+=i
#     return sum
# print(add(1,2,3,3,3,4))
# print(add(4,3,0))

# **kwargs = parameter that will pack all arguments into dictionary
            #  useful so that a function can accept a varying amount of keyword

# def hello(**kwargs):
#     print('helo' ,end=' ')
#     for key,value in kwargs.items():
#         print(value,end= ' ')
#     # print("hello" + kwargs['first'] + kwargs['last'])
# hello(title= 'Mr.', first ='Bro',middle='middle' ,last='Code')

# animal = 'cow'
# item= 'table'
# print("the " + animal + " jumped on " + item)
# print("the {} jumped on {}".format(animal,item))
# print("the {1} jumped on {0}".format(animal,item))
# print("the {animal} jumped on {item}".format(animal='cow',item='moon'))


# name= 'snow'
# print('helo,my name is {}'.format(name))
# #add to padding
# print('helo,my name is {:10}.nice '.format(name))
# print('helo,my name is {:<10}.nice '.format(name))
# print('helo,my name is {:>10}.nice '.format(name))
# print('helo,my name is {:^10}.nice '.format(name))

# number=4.334554784757
# print("the number is {:.4f}".format(number))
# num=10000
# print("{:,}".format(num)) #thousanddd
# print("{:b}".format(num))  #binary
# print("{:o}".format(num))   
# print("{:X}".format(num))
# print("{:E}".format(num))   #exponential

# try:
#     num=int(input('Enter a number: '))
#     dem=int(input("enter a num to divide: "))
#     res = num/dem
# except ZeroDivisionError as e:
#     print(e)
#     print('helo')
# except ValueError as e:
#     print(e)
# else:
#     print(int(res))
# finally:
#     print('learning python')

# import os
# path = 'C:\\Users\\priyayad\\Desktop\\219-933.html'
# if os.path.exists(path):
#     print('that location exists')
#     if os.path.isfile(path):
#         print('this is file')
#     elif os.path.isdir(path):
#         print("this is folder")
#     else:
#         print('it is what is it')
# else:
#     print("lol")

# try:
#     with open('text.html') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('file not found ')

# text= "Anacondaaaaaa"
# with open('text.txt','w') as file:
#     file.write(text)

# text= "kkkkkk"
# with open('text.txt','a') as file:
#     file.write(text)

# copyfile()= copy content of File
# copy()= copyfile()+permisiion mode+ destination can be a directory
# copy2() = copy() + copies metadata (files creation and modification times)

# import shutil
# # shutil.copyfile(source, destination)
# shutil.copyfile('text.txt','copy.txt')

# move a file
# os.replace(source,destination)


# fruits= ("aple", "blueberry",2)
# print (fruits)
# fruits[1]=5
# print (fruits)

# code to find if word is present in file or not take word as an input
# occurance of eah word via dictionary

# import os
# path = 'copy.txt'
# os.remove(path)

# os.remove = delete a File 
# os.rmdir  delete empty dirctory
# shutil.rmtree = delete directry with al fie

#OOPS
# class Car:
#     wheels=5
#     def __init__(self, make, model, year,color):
#         self.make=make
#         self.model = model
#         self.year = year
#         self.color = color

#     def drive(self):
#         print('Drive')
#     def stop(self):
#         print('stopping')

#inheritace
# class Animal:
#     alive= "thik h"
#     def eat(self):
#         print("Eating")
#     def sleep(self):
#         print("sleepig")

# class rabbit(Animal):
#     pass #plceholder it is
# class dog(Animal):
#     def bhowbhow(self):
#         print("bhowbhow")
# class cat(Animal):
#     pass
# cat1= cat()
# rabbit1=rabbit()
# dog1= dog()
# dog1.bhowbhow()
# print(rabbit1.alive)


# Multiple Inheritance
# class pray:
#     def hunt(self):
#         print("this animal is haunting")

# class predeter:
#     def hunter(self):
#         print("this animal is craxzy")

# class Rabbit(pray, predeter):
#     pass

#method chaining= calling multiple methods sequentially            cart1.turn_on().drive() 
                #  each call performs aactio on same object and return self

# class Cart:
#     def turn_on(self):
#         print("you start the engine")
#         return self

#     def drive(self):
#         print("drived")

# cart1= Cart()
# # cart1.drive()
# # cart1.turn_on().drive()   # this will give error, but if we return self in function it will pass
# cart1.turn_on()\
#      .drive()

# super() = fxn used to give access to method of parent class and return a temporary object of paret class

#abstract cls prevent user from creating an object of that cls
#abstract cls is a cls which contains one or more abstract methods
# abstract method has a declaration but dont have implemetation
# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
# class car(Vehicle):
#     def go(self):
#         print("car")
# class train(Vehicle):
#     def go(self):
#         print("train")
# # v=Vehicle()
# c=car()
# t=train()

# # v.go()
# c.go()
# t.go()

# walrus operator :=
#assignmet  expresssion aka walrus operator

# foods =list()
# while food := input("enter food : ")!="quit":
#     foods.append(food)

# def heelo():
#     print("hello python")

# print(heelo)

# pyhton =print
# pyhton("python is easy")

#higher order function= accept a fxn as argument or return fxn
# def loud(text):
#     return text.upper()
# def quiet(text):
#     return text.lower()
# def hello(fxn):
#     text = fxn("Hello")
#     print(text)

# hello(quiet)
# hello(loud)

#lambda fxn= fxn written in 1 line using lambda kwy
# doubte = lambda x: x+2
# multiply = lambda x,y:x*y
# print(doubte(8))
# print(multiply(4,9))

# sort() method = used with lists
# sort() fxn = used with iterables

# students=["s","a","e","t"]
# students.sort(reverse = True)
# for i in students:
#     print(i)
# ww_students=sorted(students)
# for i in ww_students:
#     print(i)

# students= [("ssddf" , "F" , 60),
#            ("sdff" , "A" , 10),
#            ("aadf" , "D" , 69),
#            ("ffdf" , "B" , 90),
#            ("jjdf" , "C" , 10),
#            ]
# grade = lambda grades:grades[2]
# students.sort(key=grade)
# for i in students:
#    print(i)

# filter() creates collection of element from an iterals
#filter(fxn,iterables)

# friend = [("ried" , 19),
#           ("monica",90),
#           ("jow",18)]
# age = lambda data:data[1] >18
# drinking =list(filter(age,friend))
# for i in drinking:
#     print(i)

# reduce =apply a fxn to an iterable and reduce
# reduce(fxn, iterable)

# import functools
# letters = [1,2,3,4,5,6]
# word = functools.reduce(lambda x,y,:x*y, letters)
# print(word)

#list comprehension = a way to create a new list with less syntax
# sq=[]
# for i in range(1,11):
#     sq.append(i+10)
# print(sq)

# oo= [i*i for i in range(1,11)]
# print(oo)

# stu = [100,2,9,69,44,23,56,99]
# pasus = list(filter(lambda x: x>=60, stu))
# print(pasus)

# dictionary comparhension = creae dictionary using an expression
# dic= {key: expression for(key,val) in iterab}

# cities = {"NY":32 ,"Boston":75,"LA" : 100}
# cities1 = {key:round((value-32)*(5/9)) for (key,value) in cities.items()}
# print(cities1)

# girss = {'pr': "ni", 'sh': "sh", 'pip': 'ff'}
# # qa= {key:value for (key,value) in girss.items() if value == 'sh'}
# qa= {key:("tue" if value == 'ni' else 'false') for (key,value) in girss.items()}
# print(qa)

# zip(*iterables) = aggregate element from two or more iterables (list, tuples, sets, etc.)

# username = ["Dude", "Bro", "ass"]
# password = ("ryrryu7","375735", 88)
# userse=zip(username,password)
# for i in userse:
#     print(i)
# us=list(password)
# print(us)
# print(type(us))
