# using for loop
#range(start)
# range(start, stop)
# range(start, stop, step)
# for i in range(10):  
#     print(i)

#1. print numbers from 0 to 9
# for i in range(10):
#     print(i)
#2. print numbers from 10 to 20
# for i in range(10, 21):
#     print(i)

#3. print even numbers from 2 to 40
# for i in range(2, 41, 2):
#     print(i)
# 4. print odd numbers from 1 to 31
# for i in range(1, 32, 2):
#     print(i)
# 5 print numbers from 10 to 1
# for i in range(10, 0, -1):
#     print(i)
# 6 print this pattern abc abc abc

# for i in range(3):
#     print("a")
#     print("b")
#     print("c")
# 7 print this pattern abbb abbb abbb
# for i in range(3):
#     print("a")
#     for j in range(3):
#         print("b")

##### INPUT VALIDATION ##########
### Code an addition program.
### ask for 2 numbers and validate that the 2 inputs are numbers
#### Keep asking until the person types in a proper value
# if not number, tell the person



# while loop to keep asking until the person types a proper number

# while True:
#     num1 = input("What is your number? ")

#     if num1.isdigit():
#         num1 = int(num1)
#         print("Number accepted ")
#         break
#     else:
#         print("You must enter a number! ")

# print("this runs after the loop ")


# write a program to ask for a name
# keep asking until a proper name (alphabets) is given

# while True: 
#     name1 = input("What is your name? ")

#     if name1.isalpha():
#         print(" Hello, ", name1)
#         break
#     else:
#         print("You must enter a name ")

# print("this runs after the loop ")

# write a program to ask for a valid postal code
# 

# while True:
#     postalcode1 = input("What is your postal code? ")

#     if postalcode1.isdigit() and len(postalcode1) == 6:
#         print(" This is your postal code ")
#         break
#     else:
#         print("A postal code must be 6 numbers only.")

# print("this runs after the loop ")

# Write a program to add 2 numbers and show the results
# Validate that both inputs are numbers

while True:
    num1 = input("What is your number 1? ")
    num2 = input("What is your number 2? ")

    if num1.isdigit() and num2.isdigit():
        answer = int(num1) + int(num2)
        # 10 + 20 = 30
        #print(num1 + num2 = answer)
        print(num1, "+" , num2, "=", answer)
        break
    else:
        print("You must enter a number ")

print("This runs after the loop")

        
        

'''
.isdigit() 
.isalpha()
.isalnum()

.isupper()
.islower()

length check >>>> len()
range check >>>>>  <, <=, >, >=
presence check >>>>>> checks for existenace of character
format check >>> string slicing T1234567U

'''