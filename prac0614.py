'''
Task 2 
You have been asked to write a program that will create a password for a user. 
Open the file RM_SP.py 
You will see the following function that: 
Takes the name of the user 
Returns a text string of the name without the spaces 
'''

def removesp(text): 
    newtext = "" 
    for char in text: 
        if not char.isspace(): 
            newtext += char 
    return newtext 
'''
6. In your program, write a function changecase() that: 
Takes a single character as a parameter 
Returns the following: 
The lowercase letter of the character if the character is a uppercase alphabet 
The uppercase letter of the character if the character is a lowercase alphabet 
The character if the character is not an alphabet 
Save your program as CHGCASE_<your name>_<class>_<index_number>.py [3] 
'''
# check if uppercase? ===> .isupper() --> True or False
# check if lowercase? ===> .islower()  --> True or False
# change to upper case ===> .upper() - returns the string in upper case
# change to lower case ===> .lower() - returns the string in lower case
# check if alphabet? === > isalpha() -- > returns True or False


def changecase(char):
    if char.isalpha(): ### check if the char is a alphabet
        if char.isupper(): # check if the alphabet is in uppercase
            return char.lower() #if it is uppercase change it to lowercase
        else:
            return char.isupper() #if it is lowercase change it to uppercase
    else: 
        return char #do not change
    
x = changecase("A")
y = changecase("a")
z = changecase("1")
print(x)
print(y)
print(z)

##### def function changecase()
# check if alphabet >>> isalpha()
# check if uppercase >>> isupper(), islower()
# change to lower/ upper case >> .lower(), .upper()
'''
7. Extend the program by writing a function pwdgenerate() that: 
Takes the name of the user as a parameter 
Removes the spaces in the name using the removesp() function 
Creates a password by taking each alternate character in the name (without spaces) 
and changing the case of the character using changecase() function 
Appends a random digit of 0 to 9 inclusive at the end of the password 
Returns the generated password 

Sample Executions: 
>>> pwdgenerate(“John Tan”) 
‘jHtN2’ 

>>> pwdgenerate(“jOHN tAN”) 
‘JhTn9’ 

Save your program as PWDGEN_<your name>_<class>_<index_number>.py	[5] 
'''

'''
8. Save your program as PASSWD_<your name>_<class>_<index_number>.py 
Extend your program to create a user interface. The program must: 
Allow the user to input the name of the user with a suitable prompt message 
Loop until the user enters a valid name that has at least 5 characters with a suitable error message 
Generate and display the generated password of the user with a suitable message. 

Save your program [4] 
'''

###### Function Practice #############

def hello(yourname, myname):
    # body of the function i.e. what the function is supposed to do
    print("hello", yourname, "my name is", myname)

# call the function
#hello("Joshua", "David")

####### write a function to add 2 numbers
def add(num1, num2):
    answer = num1 + num2 # add the 2 numbers
    return answer

mynumber = add(234234234, 324234)
print(mynumber)

###### write a function to calculate area of triangle
###### base, height. 0.5 * base * height
def area(base , height):
    answer = 0.5 * base * height
    return answer
    
t1 = area(34, 99)
t2 = area(12, 654)
t3 = area(23, 55)

total = t1 + t2 + t3

#### triangle 1, b = 34, h=99
#### triangle 2, b = 12, h=654
#### triangle 3, b = 23, h=55
#### add up the areas of the 3 triangle

