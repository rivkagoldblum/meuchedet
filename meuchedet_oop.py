  

import datetime as dt
from datetime import date
from meuchedet2 import Basic
from meuchedet2 import Adif
from meuchedet2 import C

print('Welcome to Meuchedet!')
tz = input('Please enter your Teudat Zehut number: ')
DOB = input('Please enter your  Date of Birth as "dd/mm/YYYY": ')
age = int(input('Please enter your age: '))
firstname = input('Please enter your first name: ')
lastname = input('Please enter your last name: ')
coverageplan = input('Please enter your coverage plan: Basic, Adif or C: ')
phonenumber = input('Please enter your phone number: ')

# gender = input('Please enter your gender M/F: ')



class Meuchedet:
#    alias patient

    def __init__(self, tz, firstname, lastname, age, coverageplan, phonenumber):
        self.tz = tz
        self.firstname = firstname
        self.lastname = lastname
        self.DOB = dt.datetime.strptime(DOB, "%d/%m/%Y")
        self.age = round(((dt.datetime.today() - self.DOB).days)/365)
        self.coverageplan = coverageplan
        self.phonenumber = phonenumber 
      
       # self.gender = gender 

        if coverageplan == 'C':
           self.meuchedet2 = C()
        elif coverageplan == 'Basic':
            self.meuchedet2 = Basic()   
        elif coverageplan == 'Adif':
            self.meuchedet2 = Adif() 
         

     
   # no need, it updates itself according to the day'sdate
   # def age(self, DOB):
   #     age = round(((dt.datetime.today() - self.DOB).days) / 365)
   #     self.age = age

   # def update_age(self, birthdate):
   #   # today = date.today()
   #   days_in_year = 365.2425
   #   self.age = int(date.today() - birthdate) / days_in_year)            
   #   return self.age 
 
    def charge(self):
        if self.age < 18 or self.age > 60:
            return  0
        else:
            return self.meuchedet2.get_cost()                    
                    
  

    def name_update(self, new_lastname):
        new_lastname = input('If your name has changed, enter your new last name?')
        self.lastname = new_lastname
        return self.lastname 


#        if self.age<18:
#                age_bracket = 'child'
#                if self.coverageplan == 'basic':
#                    print('your monthly charge is 20 shekel')
#                elif self.coverageplan == 'adif':
#                    print('your monthly charge is 50 shekel')
#                elif self.coverageplan == 'c':
#                    print('your monthly charge is 90 shekel')
#        else:
#                age_bracket = 'adult'
#                if self.coverageplan == 'basic':
#                    print('your monthly charge is 30 shekel')
#                elif self.coverageplan == 'adif':
#                    print('your monthly charge is 60 shekel')
#                elif self.coverageplan == 'c':
#                    print('your monthly charge is 90 shekel')
#
# Callback function
    def callback(self, tz):
        input("Enter tz number :")
        return (f'Phone number is {phonenumber}')       
           
# Prevention of duplication of tz numbers
    def __eq__(self, other):
        if self.tz == other.tz:
            return "Duplicate tz! Please enter another number:"
#        else:
#            return "Valid tz" 
# Sting method to give patient's information
    def __str__(self):
        return f'{self.lastname}, {self.firstname}, {self.age}, {self.coverageplan}'                   

patient1 = Meuchedet(tz, firstname, lastname, age, coverageplan, phonenumber)
patient2 = Meuchedet(123456, 'abc', 'def', 56, 'Adif',654321)

print('Age = ', patient1.age)
print('New last name is', patient1.name_update(lastname))
print(patient1.callback(tz))

#print(patient1.monthly_price())
print(patient1.charge())

print(patient1.tz)
print(patient1.firstname)
print(patient1.lastname)    
print(patient1.age)
print(patient1.coverageplan)
print(patient1.phonenumber)
print(patient1.charge())
print(patient1.callback(tz))
print(patient1.meuchedet2.therapy())
