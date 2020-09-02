import csv


def main():
    with open("places.csv", "r", newline="") as file_places:
        list_places = list(csv.reader(file_places))
    print("Travel Tracker 1.0 - by Tristan Harrington")
    print(len(list_places), "places loaded from places.csv")
    arranged_list = list_places
    for place in arranged_list:
        if place[3] == "n":
            place[3] = "*"
        else:
            place[3] = ""
    arranged_list.sort()
    program_continue = True
    while program_continue:
        print("Menu:", "L - List places", "A - Add new place", "M - Mark place as visited", "Q - Quit", sep="\n")
        user_choice = input(">>> ")
        program_continue = menu(arranged_list, user_choice)


def menu(places, user_choice):
    new_location = []
    menu_choice = user_choice.upper()
    if menu_choice == "L":
        # Comment// Prints places; in ascending order. (relative to priority with places visited as top)
        display_list(places)
        # Comment// Loop to check how many places are visited, then print result
        not_visited = 0
        for location in places:
            if location[3] == "*":
                not_visited += 1
        print("{} places. You still want to visit {} places.".format(len(places), not_visited))
    elif menu_choice == "A":
        # Comment// Asks for a new location, appends to a list, which is added to the master list.
        new_location.append(input("Name: "))
        new_location.append(input("Country: "))
        new_location.append(input("Priority: "))
        new_location.append("*")
        places.append(new_location)
    elif menu_choice == "M":
        # Comment// Mark a place as visited
        display_list(places)
    elif menu_choice == "Q":
        # say places saved
        print("Have a nice day :)")
        return False
    else:
        # TODO: Not correct handling; just placeholder --
        print("Invalid menu choice")
    return True


def display_list(given_list):
    list_numeric = 1
    # Comment// Had to use two loops here for sorting if place was visited.
    for index in given_list:
        if index[3] == "*":
            print("{:<2}{}. {:<8} {:^5} {:<12} {} {:>5}".format(index[3], list_numeric, index[0], "in", index[1],
                                                                "priority", index[2]))
            list_numeric += 1
    for index in given_list:
        if index[3] == "":
            print("{:<2}{}. {:<8} {:^5} {:<12} {} {:>5}".format(index[3], list_numeric, index[0], "in", index[1],
                                                                "priority", index[2]))
            list_numeric += 1


main()
