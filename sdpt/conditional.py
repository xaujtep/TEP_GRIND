#If statement
age = int(input("Enter your age: "))

if age >=18:
    print("Legal age")
print("Thankyou for using the program")

#--------------------------------------------

#If-else statement

age = int(input("Enter your age: "))

if age >=18:
    print("Legal age")

else:
    print("Too young")
age = int(input("Enter your age: "))

if age >=18:
    print("Legal age")

print("Thankyou for using the program")

#--------------------------------------------

# If-elif-else statement

age = int(input("Enter your age: "))

if age >=18:
    print("Legal age")
elif age >=13:
    print("Teenager")
else:
    print("Too young")

#----------------------------------------------

#Nested Condition

age = int(input("Enter your age: "))
height = int(input("Enter your height: "))

if age >=18:
    if height >= 176:
        print("Tall and Legal")
    elif height>= 150:
        print("Average and Legal")
    else:
        print("Short")
else:
    print("Too young")

#------------------------------------------------

#Logical Operator 
#or  & and

age = int(input("Enter your age: "))
height = int(input("Enter your height: "))

if age >=18 and height >= 176:
    print("Tall and Legal")
elif age >=18 and height>= 150:
    print("Average and Legal")
else:
    print("Short")

#-----------------------------------------------
