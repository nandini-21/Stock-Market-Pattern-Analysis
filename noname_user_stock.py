# Import supporting scripts.
from noname_watchlist import *


def take_stock_input():
    """
    This function is invoked when the user decides to enter his own data.
    This function collects takes the day-wise user input and appends it to a list.
    """

    total_data = []

    while True:
        try:
            n = int(input("How many days' data do you wish to add?\n"))
            break
        except:
            print("Enter an integer")
            continue

    while n <= 0:
        print("Enter a number greater than 0.\n")
        n = int(input("How many days' data do you wish to add?\n"))

    i = 0
    while i < n:
        print(f'\nDay{i + 1}\n')
        try:
            date = input(f"Enter the date or any label for your day {i + 1} data \n")
            open = float(input("Enter the day's opening price\n"))
            low = float(input("Enter the day's low\n"))
            high = float(input("Enter the day's high\n"))
            close = float(input("Enter the day's closing price\n"))
            total_data.append([open, low, high, close, date])
            i += 1
        except:
            print("Please check your values and rerun.")
            continue

    return total_data


def analysis(total_data, stock_name):
    """
    Does analysis of the user inputted stock data.
    """

    # Create an object to access class methods
    watchlist = Watchlist(stock_name)

    # Initialises a result file that to contain the pattern analysis result.
    initialise_result_file(stock_name)

    # Creates a dictionary to contain the day-wise pattern analysis result.
    pattern_analysis = watchlist.create_dictionary(total_data)

    # Adds the dictionary data to the out file.
    watchlist.append_output_to_file(pattern_analysis, stock_name)

    result_file = open(f'{stock_name}_analysis_file.txt', 'r')

    # If the out file has only two lines written i.e. the initialisation lines, it means no pattern found.
    if len(result_file.readlines()) == 2:
        result_file.close()
        result_file = open(f'{stock_name}_analysis_file.txt', 'w')
        result_file.write("No pattern found.")
        print("No pattern found for your data.")
    else:
        print(f"Pattern analysis of {stock_name} data can be found in the file named '{stock_name}'_analysis_file.txt' "
              f"in this very folder!")
    result_file.close()



