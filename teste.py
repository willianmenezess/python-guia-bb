def x(u):
    for i in range(u):
        yield(i**i)

def z(n): return lambda x:x+n

w=0
for k in x(5):
    w+=(lambda x:x//2)(z(k)(k))
print(w)
