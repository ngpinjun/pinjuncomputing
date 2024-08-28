############################### FOR LOOP #############################

# FOR LOOP - repeat block in scratch
# WHen you use a for loop, you know EXACTLY HOW MANY TIMES TO REPEAT

# for every i in the range of 10

# print 5 "hello"

# print the numbers from 0 to 10

# print the numbers from 0 to 20
    
# for i in range(5):
#     print("hello")

# for i in range(11):
#     print(i)

# for i in range(21):
#     print(i)
## INDENTATION IS THE SPACE IN FRONT OF CODE
# nested loop - loop in a loop
# for i in range(3):
#     print("a")

#     for i in range(3):
#         print("b")
    

# range function

# for i in range(10): # 0,1,2,3,4,5,6,7,8,9
#     print(i)




# option 1: range(stop) 
# range(10)  >>>> 0,1,2,3,4,5,6,7,8,9

# how do i count from 1 to 10
# option 2: range(start, stop)
# for i in range(21, 31):
#     print(i)


# how do i count multiples of 2
# option 3: range(start, stop, step)
# for i in range(3, 37, 3):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

'''
# Question 1: Print numbers from 0 to a given number (exclusive)
# Test case 1: example input: 5, example output: 0 1 2 3 4
# Test case 2: example input: 3, example output: 0 1 2
'''
## Write and test your code here
# num1 = int(input("what number? "))
# for i in range(num1):
#     print(i)
    

'''
# Question 2: Print numbers from a given start number 
# to a given stop number (exclusive)
# Test case 1: example input: 3 8, example output: 3 4 5 6 7
# Test case 2: example input: 1 5, example output: 1 2 3 4
'''
## Write and test your code here
# num1 = int(input("what number? "))
# num2 = int(input("what number? "))
# for i in range(num1, num2):
#     print(i)

           
'''
# Question 3: Print even numbers from 0 to a given number (exclusive)
# Test case 1: example input: 10, example output: 0 2 4 6 8
# Test case 2: example input: 7, example output: 0 2 4 6
'''
## Write and test your code here

# num1 = int(input("what number? "))
# num2 = int(input("what number? "))
# num3 = int(input("what number? "))
# for i in range(num1, num2, num3):
#     print(i)


# count down from 100 to 89
for i in range(100, 88, -1):
    print(i)

'''
# Question 5: Print the squares of numbers from 
# 0 to a given number (exclusive)
# Test case 1: example input: 5, example output: 0 1 4 9 16
# Test case 2: example input: 3, example output: 0 1 4
'''
## Write and test your code here
num1 = int(input("what number? "))
# num2 = int(input("what number? "))
# num3 = int(input("what number? "))
for i in range(num1):
    print(i**2)