import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n>= 1000:
        break

cs = itertools.cycle('ABC')
t= 10
for c in cs:
    print(c)
    t -= 1
    if t==0:
        break
