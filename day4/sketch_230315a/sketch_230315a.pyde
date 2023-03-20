# func 1


def func1():
    a = 10
    print('a in Func1',a)
    
a = 100
print('a in out 1',a)
func1()
print('a in out 2',a)


# func2

def func2():
    global b
    b = 10
    print('b in Func2',b)
    
b = 100
print('b in out 1',b)
func2()
print('b in out 2',b)
