print("Aditya")

name = "Anshuman"
print(name)

# Addition of two numbers
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))
sum = number1 + number2
print(sum)

#Subtraction of 2 numbers
number3 = int(input("Enter 1st number: "))
number4 = int(input("Enter 2nd number: "))
diffrence = number3 - number4
print(diffrence) 

#Time and Date 
import time
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)

