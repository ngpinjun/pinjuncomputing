'''
Task 2
The following program is written for prospective customers of a painting services company. 
The program provides a price quotation for the painting services after 
customers enter their selection.
'''

print("Welcome to ColorBest Painting Services!")
apartment = input("Select apartment type (A)3-room, (B)4-room, (C)5-room:")
if apartment == "A":
    no_rooms = 3
elif apartment == "B":
    no_rooms = 4
elif apartment == "C":
    no_rooms = 5
print(no_rooms)

paint_type = input("Select paint package (A)Easy-clean, (B)Mould-free, (C)Premier all-in-one:")

if paint_type == "A":
    base_cost = 1200
elif paint_type == "B":
    base_cost = 1800
elif paint_type == "C":
    base_cost = 2200
print(base_cost)

   
colour_type = []
for i in range(1,no_rooms+1): #loops through the number of rooms you have
    while True:
        
        paint_colour = int(input("Select paint color(01 to 58) for Room #{}: ".format(i)))
       
        if paint_colour > 0 and paint_colour < 59:
            print(f"Thank you, your colour selection is {paint_colour}")
            break
        else:  
            print("Your colour selection is wrong and it should between 01 to 58 only")
            
            
    colour_type += [paint_colour] # adds the number to the colour_type list

# while True:
    
# colour_type = []
# for i in range(1,no_rooms+1): #loops through the number of rooms you have
    
#     paint_colour = int(input("Select paint color(01 to 58) for Room #{}: ".format(i)))
#     if paint colour < 0 and paint colour > 59:
#         print(f"Thank you, your colour selection is {paint colour}")
#         break
#     else:
#         print("Your
#     colour_type += [paint_colour] # adds the number to the colour_type list




    
    
print("Colours selected are:")
j = 1
for colour in colour_type:
    print("Color code for Room {0}: {1}".format(j,colour))
    j += 1
'''
Open the file PAINT.py
Save the file as MYPAINT_2023_<your name>_<centre number> <index number>.py

7 The company will extend their services to 5-room apartments. 
5-room apartments consist of 5 rooms in total.
Edit the program so that it allows users of 
5-room apartments to enter that as a selection. [2]

8 The company has just added a third paint package “Premier all-in-one” 
to its existing list of services.
Edit the program so that it allows users to select the 
“Premier all-in-one” package. The base cost of the package is $2200. [2]

9 The customer is required to enter the colour codes for all the rooms.
The colour code must be an integer between 1 to 58 (inclusive).
Edit the program so that it validates the colour code entry and 
prompts for the colour code to be entered again each time 
an invalid colour code is entered. [4]

10 The total cost of the painting service package includes the 
base cost and a variable cost. The variable cost depends on the total 
number of rooms to be painted, with $120 charged per room to the total cost.
Edit the program so that it computes the total package price and displays 
it at the end of the program.

Save your program. [2]
'''