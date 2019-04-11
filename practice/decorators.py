def superfunction(str): 
   
    def addWelcome(): 
        return "Welcome to "
    return  addWelcome() +str

    def addGreetings():
        return "Hi Jay"
    return  addGreetings() + str

def subfunction(name): 
    return name 
print superfunction(subfunction("GeeksforGeeks")) 






'''def attach_data(func): 
       func.data = 60
       return func 
  
@attach_data
def add (x, y): 
       return x*y 
   
print"addition:",add(2, 3)  
print"additional value", add.data'''







