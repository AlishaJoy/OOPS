#create a class 
class hello:
    pass
#manually assigning 
hi = hello()
print(hi)
hi.name = 'joy'
print(hi.name)

#assigning using init method 

class employee:
    def __init__(self,first,last,salary):
        self.fn = first
        self.ln = last
        self.s = salary
        
emp1 = employee('freddy','johnson',69900)  
emp2 = employee('greddy','markston',99000)      
print(emp1.fn)
print(emp2.s)