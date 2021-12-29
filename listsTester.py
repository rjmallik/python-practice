thislist=["apple","banana", "cherry","blackberry"]
thislist[0:2]=["banana", "watermelon", "plums"]
if "watermelon" in thislist:
    print("Yes, 'watermelon' is in thislist." )
else:
    print("No 'watermelon' is not in thislist...")

print(thislist)

def myfunc():
    thislist=["juice","soda","sparkling water"]
    print(thislist[-3:-1])
myfunc()

thislist.insert(1,"papaya")
print(thislist)

veggielist=["brocolli", "carrots", "cabbage"]
veggielist.append("lettuce")
print(veggielist)

thislist.extend(veggielist)
print(thislist)

thislist.remove("brocolli")
print(thislist)

# thislist.clear()  -method allows list to still exist but erase everything in list
# del thislist - does the same thing as thislist.clear method

thislist.sort()
print(thislist)

numberlist=[50,39,80,200,55]
thislist.extend(numberlist)
print(thislist)

thislist.sort()
print(thislist)