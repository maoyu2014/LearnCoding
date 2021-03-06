s = (x*x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b 
        a,b = b,a+b
        n=n+1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

def triangles():
    L1 = []
    L2 = [1]
    while 1:
        yield L2
        L1 = L2
        L2 = []
        pre_num = 0
        for x in L1:
            y = pre_num + x
            L2.append(y)
            pre_num = x
        L2.append(x)

def triangles2():
    L = [1]
    while True:
        yield L
        L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]

n = 0
for t in triangles2():
    print(t)
    n += 1
    if n==10:
        break
