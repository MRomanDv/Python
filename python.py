#print("hhhhhhhhhaldugdl")
import time
from curses.ascii import isdigit
from difflib import Match
import math
from unittest import result


#VARIABLES INT,STR,BOOL,FLOAT -------------------------

var1 = 5
var2 = 7
#print( var1 + var2)
#print(type(var1))

greet = "hi my name is"
#name = "Miguel"
age = 26

#sentence = greet + " " + name + " " + "and i am " + "" + str(age) +  " years old" + "and my height is " + str(floate_number)
#print(sentence)
floate_number = 257.4687
#sentence = greet + " " + name + " " + "and i am " + "" + str(age) +  " years old" + "and my height is " + str(floate_number)
#print(type(floate_number))
#print(sentence)

boolean_var = False
#print(type(boolean_var))
#print("I think this if statement is " + str(boolean_var))



#MULTIPLE ASSIGNMENT --------------------------
color1 , color2, color3 = "green " , "blue " , "red "
print(color1 , color2 , color3)

person1age = person2age = person3age = 36
print(person1age , person2age , person3age)




#STR METHODS --------------------------
#name = "miguel romanaiee "
name2 = "michael roman"
name3 = "Leonara Carringhton"
name4= "aeu"
strnumber = "35"
#len
#print(len(name))
#print(name.find("a"))
#name_upercased = name.upper()
#print(name_upercased)
#print(name2.capitalize())
#print(name3.lower())
#print(name4.isalpha())
#print(strnumber.isdigit())
#print(name.count("e"))
#print(name3.count("a"))
#print(name4.replace("a","A"))
#print(name * 4)



#TYPE CASTING = CONVERT DATA TYPE INTO ANOTHER --------------------------

x = 23
y = 24.57
c = "356"

x = float(x)

print(float(x))
print(str(y)) 
print(int(c) * 2) 

print(x)


#INPUT --------------------------

#name_value = input("What is you name : ")
#age_value = int(input("And how old are you " + name_value + "?")) + 12
#tall_value = float(input("how tall are you ? "))
#print("ok " + name_value + "of " + str(age_value) +  " your data will be save in the db" + str(tall_value))




#MATH METHODS ---------------------

num = 3.1416
num_2 = 4.8
num_3 = -37
print(round(num)) #round 
print(math.ceil(num)) #round up
print(math.floor(num_2)) #round down
print(abs(num_3)) #convert to positive
print(pow(num_2,2)) #elevar a la potencia
print(math.sqrt(46)) #square root function
print(max(num, num_2, num_3)) #find max value
print(min(num, num_2, num_3))#find min value


#SLICING ---------------------- create substring by extracting slice of another
#[start:stop:step]
name = "Miguel Roman"
first_name = name[0:6]#start index is inclusive , stop index is exclusive
last_name = name[7:]
funky_name = name[0:13:3] #number of steps every 3 index > Mu m > this is equal to name[::3]
reverse_str = name[::-1]
reverse_lastname = first_name + " " + last_name[::-1]
reverse_firstname = first_name[::-1] + " " + last_name
print(first_name)
print(last_name)
print(len(name))
print(funky_name)
print(reverse_str)
print(reverse_lastname)
print(reverse_firstname)

website = "https://tesla.com"
slice = slice(8,-4)
print(website[slice])


#IF STATEMENTS  > orders of if statement matter 

sum1 = 20 + 30
sum2 = 20 + 30

if sum2 > sum1:
    print(float(sum1 + 100) * 2) 

elif sum2 == sum2:
    print('is equal') 
else:
    print('lower')


#LOGICAL OPERATORS (and(js=&&),or(||),not(in js = !))

#another_age = int(input("insert age"))

#if another_age >= 18 and another_age <=26:
    #print("you are probably in college")
#elif another_age > 26:
    #print("you are probably out of college already")    
#elif another_age <= 17 and another_age >=14:
    #print("you are probably in high school")
#elif another_age < 14 or another_age > 26:
    #print("you are either in elementary school or out of college")


#if not(another_age == 25):
    #print("hi you are 25")




#WHILE LOOP

#word = "worddd" 

#while word == "wordd":
    #print('x == y')


#FOR LOOP ----------------------------------------   range(firstindex, lastindex, steps)
#for i in range(10):
    #print(i + 1)  


#for i in range(20,80 + 1):
   # print(i)    


#for i in range(10,20,3):
    #print(i)

#for i in "Miguel":
    #print(i + "-")


#for seconds in range(15,0,-1):
    #print(seconds)
    #time.sleep(2)
#print("contdown!")







#NESTED LOOPS ------------------------------------------

rows = int(input("How many rows ? "))
columns = int(input("How many colums?"))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()




#def ------------------------------------------ >  python functions

def greet(number):
    res = number * 2
    print(res)
greet(5)
greet(9)
greet(14)  


def math_op(num1,num2):
    sum = num1 + num2
    multiply = num1 * num2
    division = num1 / num2
    rest = num1 - num2
    result = "sum result is: " + str(sum) + "multiply result is: " + str(multiply) + "division result is: " + str(division) + "rest result is: " + str(rest)
    return result
    

number1 = 38
number2 = 246

result = math_op(number1,number2) 
print(result)


list_nums = [35,46,24,57,24,365,35]

#def sum_it(list):
 #   rslt = sum(list)
    #return rslt

#rslt = sum_it(list_nums)   
#print(rslt)

def find_avarage(list):
    avarage = sum(list) / len(list)
    return avarage

avarage = find_avarage(list_nums)
print(avarage)  
if avarage > 80:
    print("You final Note is A")
elif avarage >= 60 and avarage < 80:
    print("You final Note is B")  
elif avarage >= 50 and avarage < 60:
    print("You final Note is C")       
elif avarage < 50:
    print("You final Note is F")    






#CLASSES ------------------------------------------------- OOP > vars = attrs > def = methods > self is not a reservedword can be anything
"""class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark   
    #methods
    def check_if_fail(self):
        if self.mark <= 40:
            return True
        else:
            return False    
    
    def check_if_pass(self):
        if self.mark >= 55:
            return True
        else:
            return False  
          

#Bad practice to date attr after/outside the CLASS
student1 = Student('David',80)
student2 = Student('Gabriela', 40)

did_fail = student1.check_if_fail() 
did_pass = student1.check_if_pass() 
print("did " + student1.name + " fail ? " + str(did_fail))
print("did " + student1.name + " pass ? " + str(did_pass))

did_fail = student2.check_if_fail() 
did_pass = student2.check_if_pass() 

print("did " + student2.name + " fail ? " + str(did_fail))
print("did " + student2.name + " pass ? " + str(did_pass))"""





"""class House:
    def __init__(self,color,number_bedrooms,adress):
        self.color = color
        self.number_bedrooms = number_bedrooms
        self.adress = adress
    
    def house_desc(self):
        return "This is a " + self.color + " house " + "has" + str(self.number_bedrooms) + " is located in " + self.adress

house1 = House("white",8,"1245 apey street zip code 135AA") 
description = house1.house_desc()
print(description)"""



"""class Animal:
    def eat(self):
        print("i can eat")

    
    
class Dog(Animal):
    def bark(self):
        print("i can bark")   


dog1 = Dog()
dog1.eat()"""