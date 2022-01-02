def thisFunction(n):
    return lambda a:a*n

doubler=thisFunction(2)
tripler=thisFunction(3)

print(doubler(12))
print(tripler(12))

x= lambda a,b,c:a+b*c
print(x(5,6,2))