"""
CONTRIBUTION

noname_main:
    Error handling: Nandini
    Rest: Shlok

noname_watchlist:
    File I/O: Shlok
    Rest: Nandini

noname_patterns:
    First 7 functions: Shlok
    Last 2 functions: Nandini

noname_user_stock:
    Error handling, user input function- Shlok
    Rest- Nandini
"""

""" This is the main program. It contains the user interface and function calls."""

# Import supporting scripts
from noname_watchlist import *
import noname_user_stock as us

# List of stocks with pre-loaded data
options = ['Adani enterprises', 'HDFC Bank', 'Tata Motors', 'ONGC', 'Mahindra', 'L and T']

# UI starts here
print("\nHello! Welcome to the technical analysis software. \n")

# Make an infinite loop in-case the user wants to repeat the process.
while True:

    print('We have the pricing data of the following stocks:')

    # Show the user the available options
    for i in range(len(options)):
        print(f'Stock ID: {i+1}) {options[i]}')

    # Check if the user wants to analyse existing stock or add a different data
    decision = input("\nEnter 1 to analyse an existing file and 2 to enter your own data: ")
    try:
        if decision == "1":

            # The user has chosen to analyse the stocks with preloaded data
            stock_choice = input('\nEnter the ID of the stock you want to analyse:')

            # Open the corresponding stock file and perform the analysis on its data.
            try:
                index = int(stock_choice) - 1

                # Check if the input is reasonable
                if index < 0 or index >= len(options):
                    print('\nYou entered number apart from the options shown.\nP'
                          'lease choose a number from the list provided.\n')
                    continue

                # The input is reasonable. Execute pattern analysis functions
                stock_name = options[index]
                stock = open(f'{stock_name}_input_data.txt')

                # Create an object to access class methods
                obj_placeholder = Watchlist(stock)

                # Initialises a result file to contain the pattern analysis result.
                initialise_result_file(stock_name)

                # Makes a list out of the file data.
                data_list = obj_placeholder.data_to_list(stock)

                print('Stock data is being analysed...\n')

                # Creates a dictionary to contain the day-wise pattern analysis result.
                pattern_analysis = obj_placeholder.create_dictionary(data_list)

                # Adds the dictionary data to the out file.
                obj_placeholder.append_output_to_file(pattern_analysis, stock_name)

                print(f"Pattern analysis of {stock_name} data can be found in the file named "
                      f"'{stock_name}_analysis_file.txt' in this very folder!\n")
                stock.close()

            except:
                # The user has entered something apart from integers
                print('\nPlease do not enter any other characters, only the numbers from the list given\n')
                continue

        elif decision == "2":

            # The user wants to enter his own data.
            stock_name = input("Enter the name of your stock\n")

            # Only take file names which are supported while saving.
            while not stock_name.replace(" ", "").isalnum():
                print("The stock name has unsupported character(s).\n")
                stock_name = input("Enter the name of your stock\n")
            tot_data = us.take_stock_input()
            us.analysis(tot_data, stock_name)

        else:
            # The user has entered a number apart from 1 and 2.
            print('Your number should be either 1 or 2')
            continue

    except Exception as e:
        # Unexpected error.
        print('Sorry for inconvenience\n', e)
        continue

    # Ask if the user wants to repeat the process. Terminate the program for any unexpected input.
    if_repeat = input('Do you want to repeat this for some other stock?\nPress '
                      'y for yes and n for no: ').strip().lower()
    if if_repeat == 'n':
        print('\nThank you!')
        break
    elif if_repeat == 'y':
        pass
    else:
        print('\nUnknown choice.\nTerminating program by default.')
        break


