import csv
updated_list = []


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
    # Comment// Print Places Saved
    print("{} places saved to {}".format(len(updated_list), file_places.name))
    print("Have a nice day :)")
    with open("places.csv", "w", newline="") as file_places:
        list_places = csv.writer(file_places)
        for place in updated_list:
            list_places.writerow(place)


def menu(places, user_choice):
    # Comment// Calling global, as alternative methods to retrieve places would be tedious
    global updated_list
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
        # Comment// Checking how many places unvisited to recommend adding new place
        not_visited_places = 0
        for place in places:
            if place[3] == "*":
                not_visited_places += 1
        if not_visited_places == 0:
            print("{} places. No places left to visit. Why not add a new place?".format(len(places)))
        else:
            print("{} places. You still want to visit {} places.".format(len(places), not_visited))

    elif menu_choice == "A":
        # Comment// Asks for a new location, appends to a list, which is added to the master list.
        given_name = input("Name: ")
        while string_check(given_name):
            given_name = input("Name: ")
        new_location.append(given_name)

        given_country = input("Country: ")
        while string_check(given_country):
            given_country = input("Country: ")
        new_location.append(given_country)
        # Comment// Loop to make sure both checks are met before value is appended to the list
        while True:
            try:
                given_priority = int(input("Priority: "))
            except ValueError:
                print("Invalid Input; enter a valid number")
                continue
            else:
                if given_priority < 1:
                    print("Number must be > 0")
                    continue
                else:
                    break
        new_location.append(str(given_priority))
        new_location.append("*")
        places.append(new_location)
        print("{} in {} (priority {}) added to Travel Tracker".format(new_location[0], new_location[1], new_location[2]))

    elif menu_choice == "M":
        # Comment// Mark a place as visited
        not_visited_places = 0
        for place in places:
            if place[3] == "*":
                not_visited_places += 1
        if not_visited_places != 0:
            places = display_list(places, give_list=True)
            not_visited = 0
            for location in places:
                if location[3] == "*":
                    not_visited += 1
            print("{} places. You still want to visit {} places.".format(len(places), not_visited))
            print("Enter the number of a place to mark as visited")
            while True:
                try:
                    place_value = int(input(">>> "))
                except ValueError:
                    print("Invalid Input; enter a valid number")
                    continue
                else:
                    if place_value < 1:
                        print("Number must be > 0")
                    else:
                        try:
                            place_list = places[place_value - 1]
                        except IndexError:
                            print("Invalid place number")
                            continue
                        else:
                            if place_list[3] == "":
                                print("That place is already visited")
                                break
                            else:
                                place_list[3] = ""
                                print("{} in {} visited!".format(place_list[0], place_list[1]))
                                break
        else:
            print("No unvisited places")

    elif menu_choice == "Q":
        updated_list = places
        return False
    else:
        print("Invalid menu choice")
    return True


def string_check(given_string):
    if given_string == "":
        print("Input can not be blank.")
        return True
    else:
        return False


def display_list(given_list, give_list=False):
    list_numeric = 1

    # Comment// Had to make own sort because .sort was not working with list
    priority_list = []
    for place in given_list:
        priority_list.append(int(place[2]))
    priority_list.sort()
    new_sorted_places = []
    for number in priority_list:
        for place in given_list:
            if str(number) == place[2]:
                new_sorted_places.append(place)
    given_list = new_sorted_places

    # Comment// Had to use two loops here for sorting if place was visited.
    new_list = []
    for index in given_list:
        if index[3] == "*":
            print("{:<2}{}. {:<8} {:^5} {:<12} {} {:>5}".format(index[3], list_numeric, index[0], "in", index[1],
                                                                "priority", index[2]))
            new_list.append(index)
            list_numeric += 1
    for index in given_list:
        if index[3] == "":
            print("{:<2}{}. {:<8} {:^5} {:<12} {} {:>5}".format(index[3], list_numeric, index[0], "in", index[1],
                                                                "priority", index[2]))
            list_numeric += 1
            new_list.append(index)
    if give_list:
        return new_list


main()
