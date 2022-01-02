def multiplier(n):
    return lambda a:a*n

doubler=multiplier(2)
tripler=multiplier(3)

print(doubler(2))
print(tripler(56))


x= lambda a,b,c:a+b*c
print(x(5,6,2))
