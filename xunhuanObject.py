f=open('test.txt','r')
f.__next__()


for line in open('test.txt'):
    print(line)

def gen():
    a=100
    yield a
    a=a*8
    yield a
    yield 1000

L=[]
for x in range(10):
    L.append(x**2)

for i in gen():
    print(i)

L=[x**2 for x in range(10)]