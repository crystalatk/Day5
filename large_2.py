# ***Starting Imports, Data, and Variables*****

# Import random list of numbers for assigning rooms
import random

from ascii_art import hotel_front, hotel_room, room_receipt, easter_egg

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


def is_hotel_occupied(dictionary):
    is_occupied = False
    for floor in dictionary:
        is_occupied = bool(dictionary[floor])
        if is_occupied:
            return True
    print("\n***We are so happy to have you checking in with us today!***")
    return is_occupied


def menu_check_in_or_out(dictionary):
    invalid_response = is_hotel_occupied(dictionary)
    if invalid_response == False:
        status_check = "1"
    while invalid_response:
        status_check = input(
            "\n\nHello! Will you be (choose 1 or 2): \n1. Checking in\n2. Check out\n")
        if status_check == "1":
            print("\n***That's great! We are so happy to have you.***")
            invalid_response = False
        elif status_check == "2":
            return status_check
        elif status_check == "246":
            print(easter_egg)
        else:
            print("****I have no idea what you want.****\nPlease choose 1 or 2 only!\n\n")
    return status_check


def get_number_occupants():
    while True:
        try:
            occupants = int(input(
                "\nCould you please tell me how many people are in your party?\n"))
            if 0 < occupants <= 6:
                print("***Wonderful! We can accommodate that.***")
                return occupants
            elif occupants < 0:
                print("At least one person must stay in every room!")
            else:
                print("Oh no, looks like your group is too big! ")
        except ValueError:
            print("Please enter a number.\n")


def get_floor_and_room_assignment(dictionary):
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
    return floor_assigned, room_assigned


def get_occupant_names(total):
    occupant_names = []
    print(
        "\n\n***For our records, we need to know the names of our guests.***")
    for idx in range(total):
        occupant_names.append(input(
            f"Please tell me the name of the {number_fancied_up[idx]} guest staying with us this trip.\n"))
    return occupant_names


def append_dictionary(key_value, names, dictionary):
    if key_value[0] in dictionary:
        dictionary[key_value[0]][key_value[1]] = names
    else:
        dictionary[key_value[0]] = {
            key_value[1]: names}
        name_of_occupants = " & ".join(names)
        floor_index = int(key_value[0]) - 1
        print(
            f"\n\n\n\n***Welcome, {name_of_occupants}!***\n\nWe have you in room {key_value[1]} on the {number_fancied_up[floor_index]} floor.\n ")
        print(hotel_room)


def get_which_room():
    while True:
        try:
            room_leaving = int(
                input("\n****Please tell me your room number:**** \n"))
            return room_leaving
        except ValueError:
            print("Please enter a valid room number.")
    return room_leaving


def is_room_taken(dictionary, room_attempt):
    checking = True
    while checking:
        for floor in dictionary:
            for room in dictionary[floor]:
                if room_attempt == int(room):
                    names = " & ".join(
                        dictionary[floor][room])
                    print(
                        f"\n\n\nThank you, {names}.\nWe hope you enjoyed your stay at DC Hotel!\n\nHere is your receipt:")
                    check_out_receipt = room_receipt(room_attempt)
                    print(check_out_receipt)
                    floor_out = floor
                    room_out = room
                    checking = False
                    del dictionary[floor_out][room_out]
                    return False
        if checking:
            print(
                "Oops, looks like this room is unoccupied. Please choose an occupied room!")
            checking = False
            return True


def print_out(dictionary):
    while True:
        print_out = input(
            "\n\nWould you like a print out of the current guests?\n****Hotel Employees Only****\n y or n? \n")
        if print_out.lower() == "y":
            for floor in dictionary:
                print(f"\n****Floor {floor}****")
                for room in dictionary[floor]:
                    guest_list = " & ".join(dictionary[floor][room])
                    print(f"Room number: {room}\nGuests: {guest_list}")
            return
        elif print_out.lower() == "n":
            return
        else:
            print("****Sorry, I didn't get that.****")


def is_continue_game():
    while True:
        continue_working = input(
            "\n\n\n****Would you like to continue?****\ny or n? \n")
        if continue_working.lower() == "n":
            print("\n*****Thanks for stopping by!*****")
            return False
        elif continue_working.lower() == "y":
            return True
        else:
            print("\n****Sorry, I didn't get that....****")
            return True


print(hotel_front)
active_status = True
while active_status:
    user_choice = menu_check_in_or_out(hotel)
    if user_choice == "1":
        number_of_occupants = get_number_occupants()
        floor_room = get_floor_and_room_assignment(hotel)
        occupant_names = get_occupant_names(number_of_occupants)
        append_dictionary(floor_room, occupant_names, hotel)
    elif user_choice == "2":
        checking_out = True
        while checking_out:
            room_leaving = get_which_room()
            checking_out = is_room_taken(hotel, room_leaving)
    print_out(hotel)
    active_status = is_continue_game()
