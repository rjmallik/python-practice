import re


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) #Check if the string starts with "The" and ends with "Spain":
if x:
  print("YES! We have a match!")
else:
  print("No match")



txt = "The rain in Spain"
x = re.findall("ai", txt) #Return a list containing every occurrence of "ai":
print(x)


txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) # if none are found "None" will be printed



txt = "The rain in Spain"
x = re.split("\s", txt)  #Split the string at every white-space character:
print(x)



txt = "The rain in Spain"
x = re.split("\s", txt, 1) #Split the string at the first white-space character:
print(x)



txt = "The rain in Spain"
x = re.sub("\s", "9", txt) #Replace all white-space characters with the digit "9":
print(x)