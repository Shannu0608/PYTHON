#creating functions

'''def greet():
    print("hello")
greet()

#parameters
def sum(a,b,c):
    result = a+b+c
    print(result)
sum(10,20,30)#valid
sum(10)#invalid
sum(10,20,30,40)#invalid'''

#area of circle
'''
def area(radius):
  result =3.14*radius**2 
  print(result)
area(4)'''

#square
'''def square(number):
    result = number**2
    print(result)
square(2)'''

#shopping bill
'''def shopping_bill(price,quantity):
    result = price*quantity
    print(result)
shopping_bill(10,3)'''
'''
#even or odd
def even(number):
    if number%2==0:
        print(number,"is even")
    else:
        print(number ,"is not even")
even(2)

#return
def add(a,b):
    return a+b
result = add(5,3)
print(result)'''

'''#positional args
def greet(name,wish):
    print('hello',name,wish)
greet('avinash','good morning')

def sum_sub(a,b):
    sum = a+b
    sub = a-b
    result = sum,sub
    print(result)
sum_sub(100,500)
sum_sub(500,100)'''

'''#keywords arg
def greet(name,wish):
    print('hello',name,wish)
greet(name='srikhar' ,wish='good afternoon')
greet(wish='afternoon',name='srikhar')
greet(name='srikhar')#error

#name age city
def details(name,age,city):
    print("name:",name)
    print("age:",age)
    print("city:",city)
details(name='shannu',age='18',city='tirupati')
details(age='18',city='hyderabad',name='nani')'''

'''#default
def greet(name='shannu',age=25):
    print("hello",name,age)
greet('sam',18)

#variable length
def sum(*args):
    print(result)
sum(10,20)
def fun ():
    print("mrdu")
fun()

def mul(a,b):
    return a*b
print(mul(3,4))'''

'''#variable length
def f1(*a):
    print(a)
f1(10,20,30)
f1(10,20)
f1('vani','chinni')

def f2(n1,*s):
    print(n1)
    print(s)
f2(10,'n',20,30,40)

def f2(*s,n2):
    print(s)
    print(n2)
f2(10,20,30,40,n2=50)'''

'''def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f(3,2)
f(10,20,30,40)
f(25,50,arg4=100)
#f()error
#f(4,5,arg2=6)
#f(arg3=10,arg4=20,30,40)error
f(4,5,arg3=5,arg5=6)

# **kw args
def f1(**a):
    print(a)
    print(type(a))
f1(a=10,b=20,c=30,d=40)

#global variable
a = 'this is global variable'
b = 19
def g():
    print(a)
    print(b)
def g1():
    print(a)
    print(b)
g()
g1()

#local varable
def l():
    a = 'this is local variable'
    b = 10 
    print(a)
    print(b)
def l1():
    print(a)#name error
    print(b)#name error
l()
l1()'''