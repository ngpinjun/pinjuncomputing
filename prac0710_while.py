###### keep asking for a value until a certain criteria ####
#### a person's age must be from 1 to 100, 

# 3 ways of printing statements
yourname = "David" # string
myname = "Pin Jun" # string
myage = 15         # integer

### option 1 : using the + concatenation, most troublesome, need to convert type
print("Hello, " + yourname + ". My name is " + myname + ". I am " + str(myage) + " years old.")

## option 2: use the comma, NOTE that this works only within the print()
print("Hello,",yourname,".My name is",myname,". I am", myage," years old.")

# option 3: .format() # recommended because it backward compatible, don't have to worry about conversion
print("Hello, {}. My name is {}, I am {} years old.".format(yourname, myname, myage))

# option 4: f"" string
print(f"Hello {yourname}. My name is {myname}. I am {myage} years old.")

# infinite while loop
while True:
    
    age = int(input("What is your age? "))
    if age > 0 and age < 101:
        print(f"Your age is {age}") # SUCCESS
        break # break out of the loop
    else:
        print("Age must be between 1 to 100 only.")

#### ask a person for height
# height between 30 to 240
while True:

    height = int(input("What is your height? "))
    if height > 29 and height < 241:
        print(f"Your height is {height}")
        break
    else:
        print("Height must be between 30 to 240 only.")