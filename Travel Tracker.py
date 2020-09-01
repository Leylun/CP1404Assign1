import csv


def main():
    with open("places.csv", "r", newline="") as file_places:
        list_places = list(csv.reader(file_places))
    print("Travel Tracker 1.0 - by Tristan Harrington")
    print(len(list_places), "places loaded from places.csv")
    arranged_list = list_places
    for place in arranged_list:
        if place[3] == "v":
            place[3] = "*"
        else:
            place[3] = ""
    arranged_list.sort()
    # print(arranged_list)
    display_list(arranged_list)
    program_continue = True
    while program_continue:
        print("L - List places", "A - Add new place", "M - Mark place as visited", "Q - Quit", sep="\n")
        # TODO: Not correct handling just placeholder --
        user_choice = input(">>")
        program_continue = menu(arranged_list, user_choice)


def menu(places, user_choice):
    new_location = []
    menu_choice = user_choice.upper()
    if menu_choice == "L":
        # Comment// Prints places; in ascending order. (relative to priority with places visited as top)
        display_list(places)
    elif menu_choice == "A":
        # Comment// Asks for a new location, appends to a list, which is added to the master list.
        # TODO: This is just a placeholder not correct handling
        new_location.append(input("Name: "))
        new_location.append(input("Country: "))
        new_location.append(input("Priority: "))
        new_location.append("")
        places.append(new_location)
    elif menu_choice == "M":
        # Comment//
        display_list(places)
    elif menu_choice == "Q":
        # say places saved
        print("Have a nice day :)")
        return True
    else:
        # TODO: Not correct handling; just placeholder --
        print("Incorrect Response: Please Try Again")
    return False


def type_check(given_type):
    # TODO: Finish this during last update to help with user handling
    return given_type


def display_list(given_list):
    # TODO: This is just a placeholder and not correct handling
    for index in given_list:
        print("{} {} {} {}".format(index[3], index[0], index[1], index[2]))

main()
