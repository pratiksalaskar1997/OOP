#SYNTAX OF A CLASS:
class SampleInfo():
    this is a sample class <== # docstring
    x = 20
    y = 30
    def method_1(self):
        print('m1 of class sample')
        print(SampleInfo.x)
SampleInfo().method_1()
print(SampleInfo.y)000
print(SampleInfo.__doc__)
print(help(SampleInfo))
print(dir(SampleInfo))

class test:
    def sample(self, name = 'Guest'):
        print('hello',name,'good morning')
t = test()
t.sample('pratik')
t.sample()

name = 'pratik'
age = 24
def sample():
    global name
    global age
#def display():
    #print(name, age)
sample()
display()
======================================================================================================================
# Write a Python program to create an instance of a specified class and display the namespace of the said instance
class sample:
    def __init__(self,name,marks):
        self.n = name
        self.m = marks

s = sample('pratik',88)

print(s.n ,'and',s.m)

class Circle:
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r
    def area(self):
        print('area:',(3.142)*float((self.r)**2))
    def perimeter(self):
        print('perimeter:', 2*3.142*self.r)
    def testbelongs(self):
        x = 25
        y = 10
        if ((x-self.a)*(x-self.a))+((y-self.b)*(y-self.b)) <= (self.r)*(self.r):
            print('inside')
        else:
            print('outside')
#x,y = int(input('enter two point to check circle: '))
c = Circle(0,0,40)
c.area()
c.perimeter()
c.testbelongs()
======================================================================================================================
class computation:
    def __init__(self):
        pass

    def facto(self,x):
            f = 1
            for i in range(x):
                f *= (x-i)
            print(f)
    def Sum(self,n):
        sum = 0
        for i in range(n+1):
            sum+=i
        print(sum)
    def testPrime(self,a):
        if (all(a%y!=0 for y in range(2,a))) == True:
            return True
            #print('prime')

        else:
            return False
            #print('not prime')
    def testPrimes(self,n1,n2):
        if self.testPrime(n1) == self.testPrime(n2):
            print('co-prime')
        #if (all(n1 % y!=0 for y in range(2,n1))) and (all(n2 % y!=0 for y in range(2,n2))) == True:
            #print('co-prime')
        else:
            print('not co-prime')
    def tableMult(self,b):

        for i in range(1,11):
            print(b*i)
        #print(x1)

    def alltableMult(self, d):

        for i in range(1, d + 1):
            print('table of:',i)
            for j in range(1, 11):
                print((i * j))


    def listdiv(self,n4):
        x3 = []
        for i in range(1, n4):
            if (n4 % i) == 0:
                x3.append(i)
        print(x3)
    def listDivPrim(self,n5):
        x4 = []
        i = [u for u in range(2, n5) if all(u % y != 0 for y in range(2, u))]
        #print(i)
        for j in i:
            if (n5 % j) == 0:
                x4.append(j)
        print(x4)


c = computation()
c.facto(5)
c.Sum(5)
c.testPrime(2)
c.testPrimes(3, 4)
c.tableMult(2)
c.alltableMult(9)
c.listdiv(10)
c.listDivPrim(10)
======================================================================================================
# instance method:

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        # dot format method
        print('hello {} your age is {}'.format(self.name,self.age))
s = student('pratik',24)
s.display()
=======================================================================================================
# using for loop:(name and marks)

class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark


    def display(self):
        print('hello {} your age is {}'.format(self.name,self.mark))
    def grade(self):
        if int(self.mark) >= 75:
            print(self.name, 'you got distinction')
no = int(input('enter how many student:'))
for i in range(no):
    name = input('enter the name: ')
    mark = input('enter the marks: ')
s = student(name, mark)
s.display()
s.grade()
========================================================================================
