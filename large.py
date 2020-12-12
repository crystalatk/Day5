# Exercise 2 (Large)

# Hotel Manager

# Imagine that you're running a hotel, and you want to keep track of guests by floor and room number. Start with the following dictionary:

#  hotel = {
#   '1': {
#     '101': ['George Jefferson', 'Wheezy Jefferson'],
#   },
#   '2': {
#     '237': ['Jack Torrance', 'Wendy Torrance'],
#   },
#   '3': {
#     '333': ['Neo', 'Trinity', 'Morpheus']
#   }
# }
# Write a program that does the following:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# After checking in or out, display a list of all the occupants and their rooms.
# Additional Rules:

# Do not allow anyone to check into a room that is already occupied!
# Do not allow checking out of a room that isn't occupied!
# Hints

# Start by writing down (analog style, pen & paper, or in a text file) all the steps you think a user will need to go through.
# Use input to ask the user for their status (checking in/out), number of occupants, floor, and room numbers.
# Use functions to break up your programs behaviors based on the responses.
# Functions should encapsulate the steps you outlined earlier.
# Examples might include:
# Checking In
# Checking Out
# Assigning a room and floor during check in
# Clearing a room after check out
# Use while loops and conditionals, if...else to determine if a room is available or not.
# For example while occupants > 0 ...
# Start with just adding a single occupant to a room, then add more.
# A combination of a for loop and the range() function might be helpful when collecting a list of occupants names. https://pynative.com/python-range-function/
# Bonus

# Limit the max number of occupants in a room to 6.
# Loop the program so that it goes back to the first question after displaying a list of all the occupants.
# Import Python's pprint module for printing out the list of occupants. https://docs.python.org/3/library/pprint.html


# ***Starting Imports, Data, and Variables*****

# Import random list of numbers for assigning rooms
import random

from ascii_art import hotel_front, hotel_room, room_receipt

# This is the immutable data from the problem.
hotel = {
    '1': {
        '101': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}

# This list allows me to request the hotel guest in a fancier way.
number_fancied_up = ['first', 'second', 'third', 'fourth',
                     'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']


# ****Functions*****

# Checking in Function:
# -asks for number of guests
# -assigns random room on random floor
# - checks room against current guests in dictionary to assure no duplicates
def checking_in(dictionary):
    while True:
        try:
            occupants = int(input(
                "\nCould you please tell me how many people are in your party?\n"))
            if 0 < occupants <= 6:
                print("***Wonderful! We can accommodate that.***")
                floor_assigned = str(random.randrange(1, 10))
                room_on_floor = random.randrange(10, 50)
                room_assigned = floor_assigned + str(room_on_floor)
                restart = True
                while restart:
                    restart = False
                    for floor in dictionary:
                        if floor_assigned == floor:
                            for room in dictionary[floor]:
                                if room_assigned == room:
                                    floor_assigned = random.randrange(1, 10)
                                    room_assigned = random.randrange(10, 50)
                                    room_assigned = str(
                                        floor_assigned) + str(room_assigned)
                                    restart = True
                                    break
                occupant_names = []
                print(
                    "\n\n***For our records, we need to know the names of our guests.***")
                for idx in range(occupants):
                    occupant_names.append(input(
                        f"Please tell me the name of the {number_fancied_up[idx]} guest staying with us this trip.\n"))
                if floor_assigned in dictionary:
                    dictionary[floor_assigned][room_assigned] = occupant_names
                else:
                    dictionary[floor_assigned] = {
                        room_assigned: occupant_names}
                name_of_occupants = " & ".join(occupant_names)
                floor_index = int(floor_assigned) - 1
                print(
                    f"\n\n\n\n***Welcome, {name_of_occupants}!***\n\nWe have you in room {room_assigned} on the {number_fancied_up[floor_index]} floor.\n ")
                print(hotel_room)
                break
            elif occupants < 0:
                print("At least one person must stay in every room!")
            else:
                print("Oh no, looks like your group is too big! ")
        except ValueError:
            print("Please enter a number.\n")


# Checking out function:
# -asks for guest room
# -checks user input against dictionary to ensure it is an occupied room
# -removes room from dictionary (does not remove empty floors)
def checking_out(dictionary):
    checking_out = True
    while checking_out:
        try:
            room_leaving = int(
                input("\n****Please tell me your room number:**** \n"))
            checking = True
            while checking:
                for floor in dictionary:
                    for room in dictionary[floor]:
                        if room_leaving == int(room):
                            name_of_occupants = " & ".join(
                                dictionary[floor][room])
                            print(
                                f"\n\n\nThank you, {name_of_occupants}.\nWe hope you enjoyed your stay at DC Hotel!\n\nHere is your receipt:")
                            print(room_receipt(room_leaving))
                            floor_out = floor
                            room_out = room
                            checking_out = False
                            checking = False
                            del dictionary[floor_out][room_out]
                            break
                if checking:
                    print(
                        "Oops, looks like this room is unoccupied. Please choose an occupied room!")
                    checking = False
        except ValueError:
            print("Please enter a valid room number.")


# ****Hotel Program!*******
# Program Details:
# -asks if checking in or out and runs calls appropriate function passing current dictionary into function.
# -asks if you would like to print out current dictionary (this is to make user experience easier)
# -asks if you would like to continue- gives another opportunity to check in/out or exits program
# -continually checks for user input errors and handles those within a loop.
print(hotel_front)
active_status = True
while active_status:
    invalid_response = True
    while invalid_response:
        status_check = input(
            "\n\nHello! Will you be (choose 1 or 2): \n1. Checking in\n2. Check out\n")
        invalid_response = False
        if status_check == "1":
            print("\n***That's great! We are so happy to have you.***")
            checking_in(hotel)
        elif status_check == "2":
            checking_out(hotel)
        else:
            print("****I have no idea what you want.****\nPlease choose 1 or 2 only!\n\n")
            invalid_response = True
    while True:
        print_out = input(
            "\n\nWould you like a print out of the current guests?\n****Hotel Employees Only****\n y or n? \n")
        if print_out.lower() == "y":
            for floor in hotel:
                print(f"****Floor {floor}****")
                for room in hotel[floor]:
                    guest_list = " & ".join(hotel[floor][room])
                    print(f"Room number: {room}\nGuests: {guest_list}\n")
            break
        elif print_out.lower() == "n":
            break
        else:
            print("****Sorry, I didn't get that.****")
    while True:
        continue_working = input(
            "\n\n\n****Would you like to continue?****\ny or n? \n")
        if continue_working.lower() == "n":
            print("\n*****Thanks for stopping by!*****")
            active_status = False
            break
        elif continue_working.lower() == "y":
            break
        else:
            print("\n****Sorry, I didn't get that....****")
