'''
SYNTAX OF A CLASS:
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

