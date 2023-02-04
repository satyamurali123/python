#format
txt3 = "My name is {}, I'm {},studying {}".format("John",36,"10th class")
print(txt3)
#functions

def my_function(fname,fno):
  print(fname + " is studying pragati")
  print(fno)
#9182644653 
my_function("ajay",66)
my_function("uma",77)
my_function("sai",88)
#functions
def total(a,b):
    d=a+b
    print(d)
def diff(a,b):
    d1=a-b
    print(d1)
def multi(a,b):
    d2=a*b
    print(d2)
def divi(a,b):
    d3=a//b
    print(d3)
a=int(input())
b=int(input())
total(a,b)
diff(a,b)
multi(a,b)
divi(a,b)

# vaiables
var = "chaitanya"
def show():
    global var1
    var1='tall'
    print("in function var cis",var)
show()
print("outside fun",var1 )
print("var is",var)

def outf():
    var =10
    def innf():
        var=20
        print("inner var",var)
    innf()
    print("outer var",var)
outf()

#wap with the user defined function which returns an integer value to the colon

def add(x):
    return(8+6+4+2+10+0)
  
num=6    
result=add(num)
print("output of the evalution is",result)


def display(str1):
    print(str1)
str1="hi"
display(str1)

#wap to print fibanncio series using recurrsion by functions till 7 terms

def fib(n):
    if n<2:
        return 1
    return(fib(n-1)+fib(n-2))

n=int(input())
for i in range(n):
    print("fibonacci(",i,")=",fib(i))
    
    #perforamnce of compiler
from time import*
t1=perf_counter()
i=sum=0
while i<1000000:
    sum+=i
    i+=1
sleep(0)
t2=perf_counter()
print('execution time =%fseconds',t2-t1)

#swapping
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        if a:
            c.append(a.pop())
            
        hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzle")
print(a,b,c)
hanoi(len(a),a,b,c)
print("after puzzle")
print(a,b,c)

#date
from datetime import *
d=date.today()
print(d)
d=date(2023,2,3)
for x in range(1,10):
    nextdate=d+timedelta(days=x)
    print(nextdate)
    

#krishnamurthy number
import math
def krishnamurthy(number):
    n = number
    Sum = 0
    while n > 0:
        fact = 0
        r = n % 10
        fact = math.factorial(r)
        Sum = Sum + fact
        n = n // 10

    if Sum == number:
        print(number, "is a Krishnamurthy Number" )
    else:
        print(number," is Not a Krishnamurthy Number" )
number=int(input("enter a number"))       
krishnamurthy(number)    

