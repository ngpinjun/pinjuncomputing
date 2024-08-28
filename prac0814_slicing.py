####### STRING SLICING #######
# listnums = [1,321,45,634,7,8,43,78,3,789]

# can slice up part of the list

# retrieve the first value from the list
# var1 = listnums[-1]
# print(var1)

# retrieve the first 3 items from the list
#[start:stop]
# var2 = listnums[0:3] # stop value is up to but not including
# print(var2)

# retrieve the every alternate item from list
# [start: stop: step]
# var3 = listnums[1::2]
# print(var3)
# listnum2 = []
# for i in var3:
#     listnum2.append(i*3)
# print(listnum2)

# reverse a list
# var4 = listnums[::-1]
#print(var4)

# word = "SINGAPORE"
# var5 = word[0:3]
# #print(var5)

# var6 = word[::2]
#print(var6)

# String and List Operators
# Using + to Concatenate
# List Slicing
'''
Question 1: Extract a portion of a list.
Write a function that takes a list and returns a new list 
that contains only the first three elements of the original list.
Example Input: [1, 2, 3, 4, 5]
Example Output: [1, 2, 3]
'''
## Write and test your code here
# listnums = [1, 2, 3, 4, 5]
# var1 = listnums[0:3]
# print(var1)
'''
Question 2: Get the last three items of a list.
Ask the user for a list of numbers and print the last three items.
Example Input: [10, 20, 30, 40, 50]
Example Output: [30, 40, 50]
'''
# Write and test your code here
listnums = [10, 20, 30, 40, 50,345,6,7,876,3,7,5,8,2345345,2354,5687678,9]
#var2 = listnums[2:5]
var2 = listnums[-3:] # retrieving the last 3
print(var2)

'''
Question 3: Create a sub-list from a list using slicing.
Given a list of elements, write a function that returns a 
sublist from the second element to the second last element.
Example Input: [0, 1, 2, 3, 4, 5]
Example Output: [1, 2, 3, 4]
'''
## Write and test your code here
# listnums = [0, 1, 2, 3, 4, 5]
# var3 = listnums[1:5]
# print(var3)


'''
Question 4: Reverse a list using slicing.
Write a function that takes a list and returns it reversed.
Example Input: [1, 2, 3, 4, 5]
Example Output: [5, 4, 3, 2, 1]
'''
## Write and test your code here
# listnums = [0, 1, 2, 3, 4, 5]
# var4 = listnums[::-1]
# print(var4)
'''
Question 5: Slice a list into halves.
Divide a list into two equal halves and returns both halves.
You may assume that the list has an even number of items
Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [1, 2, 3]  [4, 5, 6]
'''
## Write and test your code here
# listnums1 = [1, 2, 3]
# listnums2
# var5 = listnums
# print(var5)
'''
Question 6: Extract every second element from a list.
Write a function that returns a list of every second element from the given list.
Example Input: ['a', 'b', 'c', 'd', 'e', 'f']
Example Output: ['b', 'd', 'f']
'''
## Write and test your code here
listnums = ['a', 'b', 'c', 'd', 'e','f']
var6 = listnums[1::2]
print(var6)

'''
Question 7: Remove the first and last elements of a list using slicing.
Create a function that takes a list and returns it without 
the first and last elements.
Example Input: [0, 1, 2, 3, 4]
Example Output: [1, 2, 3]
'''
## Write and test your code here
def remove_first_and_last(lst):
    result = lst[1:-1] 
    print("Returned list:", result)  
    return result

templist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
var7 = remove_first_and_last(templist)
print(var7)

'''
Question 8: Create a function to reverse the order of elements in a 
list only from the second to the last but one.
Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [1, 5, 4, 3, 2, 6]
'''
## Write and test your code here
def reversinthemiddle(inlist):
    middle = inlist[1:-1]
    revmiddle = middle[::-1]
    return[inlist[0]] + revmiddle[inlist[-1]]

testlist = (1, 2, 3, 4, 5, 6)



'''
# Question 9: Extract the first three characters from a string
# Test case 1: example input: hello, example output: hel
# Test case 2: example input: Python, example output: Pyt
'''
## Write and test your code here
def first_three_chars(s):
    return s[:3]

print(first_three_chars("hello")) 

print(first_three_chars("Python"))

# Question 10: Extract the last three characters from a string
# Test case 1: example input: hello, example output: llo
# Test case 2: example input: Python, example output: hon

## Write and test your code here


'''
# Question 11: Extract a subset of a list from index 2 to 5
# Test case 1: example input: 1 2 3 4 5 6 7, 
example output: [3, 4, 5, 6]
# Test case 2: example input: 10 20 30 40 50 60, 
example output: [30, 40, 50]
'''
## Write and test your code here


'''
# Question 12: Extract every second character from a string
# Test case 1: example input: hello, example output: hlo
# Test case 2: example input: Python, example output: Pto
'''
## Write and test your code here



'''
# Question 13: Extract the middle three characters from a string
# You may assume the number of characters is odd
# Test case 1: example input: abcdefg, example output: cde
# Test case 2: example input: walking, example output: lki
'''
## Write and test your code here
word = 'singapore'
length = len(word)
midindex = length // 2
midword = word[midindex - 1: midindex + 2]
print(midword)
# [2:5]





'''
# Question 14: Extract the first half of a string
# Test case 1: example input: hello, example output: hel
# Test case 2: example input: Python, example output: Pyt
'''
## Write and test your code here


'''
# Question 15: Extract the second half of a string
# Test case 1: example input: hello, example output: llo
# Test case 2: example input: Python, example output: hon
'''
## Write and test your code here

'''
Question 16:
Write a function to split a string into half
and return the first half
Your function must handle an odd number length of characters
# If the length is odd, you will ignore the middle character
Example Input: "SINGING" Example Output: SIN
Example Input: "FLYING" Example Output: FLY
'''

'''
# Challenge 1:
Write a function `validate_nric(nric: str) -> bool` to 
validate if a given input is a valid Singapore NRIC number. 
A valid NRIC must start with 'S', 'T', 'F', or 'G', followed by 7 digits, 
and ends with an uppercase letter.

* In this case, assume that as long as the last character 
is an uppercase letter it is valid.

Normal Test: Input: "S1234567D", Output: True
Error Test: Input: "A1234567D", Output: False
Boundary Test: Input: "S123456", Output: False
'''
# define a function, parameter : nric, returns True/ False
def validate_nric(nric):
    if not nric[0].isupper() or nric[0] not in "STFG":
        print("First character must be S, T, F, G")
        return False
    elif not nric[1:-1].isdigit() or len(nric[1:-1]) != 7:
        print("Characters 2 to 7 must be numbers")
        return False
    elif not nric[-1].isalpha() or not nric[-1].isupper():
        print("The last character must be an upper case letter")
        return False
    return True

print(validate_nric('S1234567D'))   
        

'''
# Challenge 2:
Write a function `is_valid_username(username: str) -> bool` to 
check if a username is correctly generated. A valid username 
should be at least 6 characters long, should not contain any spaces, 
and must start with an uppercase letter followed by lowercase letters.

Normal Test: Input: "Johndoe", Output: True
Error Test: Input: "johnDoe", Output: False
Boundary Test: Input: "John", Output: False
'''

'''
# Challenge 3:
Write a function `validate_license_plate(plate: str) -> bool` 
to check if a vehicle license plate is valid. 
A valid plate starts with 3 uppercase letters, followed by 4 digits, 
and ends with an uppercase letter.

Normal Test: Input: "SAB1234Z", Output: True
Error Test: Input: "SA1234Z", Output: False
Boundary Test: Input: "SAB123Z", Output: False
'''
def validate_license_plate(plate):
    if not plate[0:3].isupper() or not plate[0:3].isalpha():
        print('the first three characters must be uppercase letters')
        return False
    elif not plate[3:-1].isdigit() or len(plate[3:-1]) != 4:
        print('followed by 4 digits')
        return False
    elif not plate[-1].isupper() or not plate[-1].isalpha():
        print('Ends with an uppercase letter')
        return False
    return True

print(validate_license_plate('SAB1234Z'))

'''
# Challenge 4:
Write a function `is_valid_postal_code(postal_code: str) -> bool` 
to validate a Singaporean postal code. A valid postal code consists 
of exactly 6 digits where the first digit must be between 1 and 7.

Normal Test: Input: "123456", Output: True
Error Test: Input: "823456", Output: False
Boundary Test: Input: "12345", Output: False
'''
def is_valid_postal_code(postal_code):
    if not postal_code[0:6].isdigit() or len(postal_code[0:6]) != 6:
        return False
    elif int(postal_code[0]) < 1 or int(postal_code[0]) > 7:
        return False
    return True
print(is_valid_postal_code('12346'))
        

'''
# Challenge 5:
Write a function `validate_date_format(date_str: str) -> bool` 
to check if a date string is in the format "DD/MM/YYYY" 
where DD, MM, and YYYY are valid digits. 

The function should ensure that DD is between 01 and 31, 
MM is between 01 and 12, and YYYY is a valid 4-digit positive integer.

Normal Test: Input: "29/02/2020", Output: True
Error Test: Input: "32/13/2020", Output: False
Boundary Test: Input: "01/01/0001", Output: True
'''