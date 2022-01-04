class humanBeing:
    def __init__ (self,name,age,haircolor):
        self.name=name 
        self.age=age
        self.haircolor=haircolor


    def greetingFunc(self):
        print("Hello my name is " + self.name)


hB1= humanBeing("RJ", 17, "yellow")
hB1.greetingFunc()
hB1.haircolor = "brown"
#print(hB1)
"""
print(hB1.name)
print(hB1.age)
print(hB1.haircolor)
"""
class teenager(humanBeing):
    def __init__(self,name,age,height, haircolor="black" ):
        humanBeing.__init__(self,name,age,haircolor)
        # or you can add super function: super().__init__(self,name,age,haircolor)
        self.height= height # in inches
        self.misc="Miscellaneous"
    def welcomeStatement(self):
        print ("Hello I am ", self.name, "and am", self.height, "inches tall!")

footballTeen=teenager("Jack", 18, 68, "blonde")
footballTeen.welcomeStatement()

#print(footballTeen.height)
#print(footballTeen.name)
t1=teenager("Ruthika", 11, 60)
print(t1.haircolor)


