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
    def fullname(self):
        return '{} {} '.format(self.fn,self.ln)
    
    
emp1 = employee('freddy','johnson',69900)  
emp2 = employee('greddy','markston',99000)      
print(emp1.fn)
print(emp2.s)

# methods
#to print full name manually

print('{} {}'.format(emp1.fn,emp2.ln))



# create a method to print full name
#class employee:
 #   def fullname(self):
  #      return '{} {} '.format(self.fn,self.ln)
    
print(emp2.fullname())
# or we can print as 
print(employee.fullname(emp1))

