
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
