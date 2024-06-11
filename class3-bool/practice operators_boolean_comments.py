
#Script to convert temperature

fahrenheit=89 #temp to convert

#Conversion Formula
celsius =(fahrenheit-32)*5/9

print(celsius) #output

'''Shortcut Operators'''
#Add 5 to me
age=25
age +=5 #adding 5 via shortcut operator
print (age)


#Add to 2024
year=2024
year +=10
print (year)

#subtracting 20
num_one=55
num_one -=20
print (num_one)

#subtracting 15
num_two =11
num_two -=15
print (num_two)

#trying multiplication 
my_value =9
my_value *=3
print(my_value)

#multiply by10
mileage=15
mileage *=10
print (mileage)

#divide by 2
pizza_slices =8
pizza_slices /=2
print (pizza_slices)

#Divide by 7 
fees = 8.90
fees /=7
print(fees)

#Raise to the 3rd Power
num_three=6
num_three **=3
print(num_three)

#raise to the 2nd Power
data=16
data **=2
print(data)

#integer division, how many times does 3 go into 16
val_one=16
val_one /=3
print(val_one)

#Integer divide by 4
val_two=9
val_two /=4
print(val_two)

#Modulus we use often to find if a value is odd or even
#Find the remainder if divided by 3  (%)
val_three=10
val_three %=3
print(val_three)

#find remainder if divided by 5 (%)
val_four=14
val_four %=5
print(val_four)

#Refactor me! Using split editor windows to copy paste
fahrenheit=89 #temp to convert
celsius =(fahrenheit-32)*5/9
print(celsius) #output

fahrenheit=89
fahrenheit -=32 #parenthesis
fahrenheit *=5/9 #multiplication/division
celsius=fahrenheit
print (celsius)

'''Boolean Operators'''
#is 7 less than 5?
print(7 <5)
result=(7<8)
print (result)

result=(7<5)
print("Is 7 less than 5?", result) #Is 7 question is a string, the result is a boolean (True/False expression)

comparative=(4<=4)
print ("Is four less than or equal to 4?", comparative)

#Is 6>2
result=(6>2)
print ("Is 6 greater than 2?", result)

#Is 5>=6
result=(5>=6)
print ("Is five greater than or equal to six?", result)

#Is 5=5
result=(5==5)
print ("Is five equal to five?", result)

#And Functions
"""
true-true = true
false-true = false
false-false = false
"""

log_1 = (5==3)
log_2 = (4==7)
print ("Log 1", log_1)
print ("Log 2", log_2)
print ("Log 1 and Log 2)", log_1 and log_2)

#Or
print ("Playing with Or function", 5==5 or 5==3) #True if at least 1 is true

#Not
Is_it_autumn=True
print("Is it autumn?", not Is_it_autumn)

x=11
y=10

#Is x less than y?
print ("Is x less than Y", x<y)

#Are we the same object?
fname='Taylor'
first_name='Taylor'
#print(fname is first_name)
#print(fnam ==first_name)

#in
print ('J' in January)
