# Create the class instances.

options = ['x', 'y', 'z', 'w']    # Add the class instances to a list.

print("Hello! Welcome to the technical analysis software. \n")

# Make an infinite loop in-case the user wants to repeat the process.
while True:

    print('We have the pricing data of the following stocks:')

    # Show the user the available options
    for i in range(len(options)):
        print(f'{i+1}){options[i]}')
    stock_choice = input('Enter the number of the stock you want to analyse: ')

    # Open the corresponding stock file and perform the analysis on its data.
    try:
            index = int(stock_choice)-1
            if index < 0 or index >= len(options):
                print('\nYou entered number apart from the options shown.\nPlease choose a number from the list provided.\n')
                continue
            stock = open(f'{options[index]}_input_data.txt')

    except:
            print('\nPlease do not enter any other characters, only the numbers from the list given\n')
            continue

    # Ask if the user wants to repeat the process. Terminate the program for any unexpected input.
    if_repeat = input('Do you want to repeat this for some other stock?\nPress y for yes and n for no: ').lower()
    if if_repeat == 'n':
        print('\nThank you!')
        break
    elif if_repeat == 'y':
        pass
    else:
        print('\nUnknown choice.\nTerminating program by default.')
        break

