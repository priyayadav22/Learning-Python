# if __name__ == '__main__'
#  module can be run as standaloneprogram      OR
#  and can be imported and used by other module
# 
# python interpreter sets "special variables", one pf ehich is __name
# thn python will execute the code found within __main
# 
# print(__name__)
# import pythonBasics
# print(pythonBasics.__name__)
#if we import any other module. then name of that module will be passed n name

import time
# print(time.time())
# print(time.ctime(87873))
# print(time.ctime(time.time()))
# print(time.localtime())
# timestr= "20 Apr,2020"
# time.strptime(timestr, "%d %B, %Y")
# (year,month,day,hours,minutes,sec, dat, day, dst)
# time_tuple =(2024,4,20,2,20,0,0,0,0)
# time_string=time.asctime(time_tuple)
# print(time_string)

# thread = a flow of execution, like a seperatorof instruction
# GIL= global interpreter lock

# cpu bound = proud/task spend most of its time waiting for interal events - use multiprocessing
#ip bound = program/task spends most of its time waiting for external evenets (user input) - use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")
def drink_coffee():
    time.sleep(4)
    print("you are drnk cofee")
def study():
    time.sleep(5)
    print("i will sleep")

x= threading.Thread(target=eat_breakfast,args=())
x.start()

y= threading.Thread(target=study, args=())
y.start()

# eat_breakfast()
# drink_coffee()
# study()
# import time
print(threading.active_count())
print(threading.enumerate())   #use  main thread

