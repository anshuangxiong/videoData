# 包裹传递

def func(*name):
    print(type(name))
    print(name)

func(1,4,6)
func(5,6,7,1,2,3)


def func2(**dict):
    print(type(dict))
    print(dict)

func2(a=1,b=9)
func2(m=2,n=1,c=11)


def func3(a,b,c):
    print(a,b,c)

args=(1,3,4)
func3(*args)