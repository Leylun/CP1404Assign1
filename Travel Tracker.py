import csv


def main():
    with open("places.csv", "r", newline="") as file_places:
        list_places = list(csv.reader(file_places))
    print("Travel Tracker 1.0 - by Tristan Harrington")
    print(len(list_places), "places loaded from places.csv")


def menu(user_choice, places):
    menu_choice = user_choice.upper()
    print("L - List places", "A - Add new place", "M - Mark place as visited", "Q - Quit", sep="\n")
    if menu_choice == "L":
        # display list of places (arranged)
        print(places)
    elif menu_choice == "A":
        # add a new place
        name = input("Name:")
    elif menu_choice == "M":
        # mark a place as visited
        print(places)
    elif menu_choice == "Q":
        # say places saved
        print("Have a nice day :)")


main()
