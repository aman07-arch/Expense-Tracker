# helpers.py
# Input validation functions used by the menu in main.py

from datetime import datetime


def is_valid_date(date_string):
    # check that the date is in YYYY-MM-DD format and is a real date
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_today():
    # returns today's date as a YYYY-MM-DD string
    return datetime.now().strftime("%Y-%m-%d")


def get_positive_float(prompt):
    # keep asking until the user enters a positive number
    while True:
        user_input = input(prompt).strip()
        try:
            # convert input string to float and check if positive
            value = float(user_input)
            if value <= 0:
                print("Amount must be greater than 0. Try again.")
            else:
                return round(value, 2)
        except ValueError:
            print("Invalid number. Please enter something like 12.50")


def get_valid_date(prompt):
    # ask for a date, press enter to use today's date
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            return get_today()
        if is_valid_date(user_input):
            return user_input
        print("Invalid date. Use the format YYYY-MM-DD (e.g. 2025-03-15).")


def get_non_empty_string(prompt):
    # keep asking until the user types something
    while True:
        user_input = input(prompt).strip()
        if user_input != "":
            return user_input
        print("This field can't be empty.")


def get_menu_choice(prompt, min_num, max_num):
    # get an integer between min_num and max_num
    while True:
        user_input = input(prompt).strip()
        try:
            choice = int(user_input)
            if choice < min_num or choice > max_num:
                print("Please pick a number between " + str(min_num) + " and " + str(max_num) + ".")
            else:
                return choice
        except ValueError:
            print("That's not a number. Please try again.")


def get_yes_no(prompt):
    # returns True for yes, False for no
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "y" or user_input == "yes":
            return True
        elif user_input == "n" or user_input == "no":
            return False
        print("Please type y or n.")


def get_month_string(prompt):
    # asks for a month like 2025-03, or blank for all time
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            return ""
        try:
            datetime.strptime(user_input, "%Y-%m")
            return user_input
        except ValueError:
            print("Invalid month. Use YYYY-MM (e.g. 2025-03) or press enter for all time.")
