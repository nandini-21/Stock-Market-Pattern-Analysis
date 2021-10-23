"""
    This contains class methods that will take the input from the files,
    and call the pattern file functions on that data.
    It also has the functions that will create the output file.
"""

# Import the supporting scripts
import noname_patterns as p


def initialise_result_file(stock_name):
    """
        Creates an output file.
    """

    # Creates and opens the result file in write mode.
    result_file = open(f'{stock_name}_analysis_file.txt', 'w')
    result_file.write(f'Here is the pattern analysis result for {stock_name}.\n\n')

    # Closes the result file.
    result_file.close()


class Watchlist:
    """A class to perform analysis of the prices and store the result."""

    def __init__(self, stock):
        self.stock = stock

    def data_to_list(self, stock):
        """
            Function to convert the input file into a 2D list.
            Each element of the 2D list is a list containing 1 day's stock data.
        """

        # data is a list containing lines of the input file as its elements.
        data = stock.readlines()

        # month_data would contain each day's data of one particular month.
        month_data = []

        for line in data:
            # Removes the new-line character.
            line = line.strip()

            # one_day_data is a list containing one day's stock data in the format : [open, low, high, close, date].
            one_day_data = line.split()

            for idx in range(len(one_day_data) - 1):    # Does not include the last element because it is date.
                one_day_data[idx] = float(one_day_data[idx].replace(',', ''))
            month_data.append(one_day_data)             # Lists of each day's data are appended to the list month_data.

        # The data file has data sorted in the order- 'latest to earliest'.
        # For analysis we need 'earliest to latest', so we reverse the list.
        month_data = month_data[::-1]
        return month_data

    def one_day_pattern(self, day):
        """
            Checks which pattern is observed on the particular day.
            Checks only those patterns which are independent of any other days.
        """

        return p.hammer(day) or p.shooting_star(day)

    def two_day_pattern(self, day1, day2):
        """
            Checks for those patterns which need two days' data as arguments.
        """

        return p.bull_engulfing(day1, day2) or p.piercing(day1, day2) or p.bear_engulfing(day1, day2) or p.dark_cloud(day1, day2)
    
    def three_day_pattern(self, day1, day2, day3):
        """
            Checks for those patterns which need three days' data as arguments.
        """

        return p.evening_star(day1, day2, day3) or p.morning_star(day1, day2, day3)

    def analyse_patterns(self, day1, day2, day3):   
        """
            Returns the observed pattern.
            Priority order: 1. three day pattern, 2. two day pattern, 3. one day pattern
        """

        return self.three_day_pattern(day1, day2, day3) or self.two_day_pattern(day1, day2) or self.one_day_pattern(day1)

    def format_keys(self, x):
        """
            Formats the date
        """
        x = x.replace("-", "/").replace("2021", "21")
        return x

    def create_dictionary(self, month_data):
        """
            Returns a dictionary containing the pattern observed against the date.
        """

        day_patterns = {}

        # To avoid the 'list index out of range error', traversal only till the third last element of month_data.
        if len(month_data) >= 3:
            for i in range(len(month_data) - 2):
                month_data[i][4] = self.format_keys(month_data[i][4])
                day_patterns[month_data[i][4]] = self.analyse_patterns(month_data[i], month_data[i + 1], month_data[i + 2])

        # Only one day and two day patterns would be applicable since there is no third day in this case.
        if len(month_data) >= 2:
            month_data[-2][4] = self.format_keys(month_data[-2][4])
            day_patterns[month_data[-2][4]] = (
                        self.two_day_pattern(month_data[-2], month_data[-1]) or self.one_day_pattern(month_data[-2]))

        month_data[-1][4] = self.format_keys(month_data[-1][4])

        # Only one day patterns would be applicable in this case.
        day_patterns[month_data[-1][4]] = self.one_day_pattern(month_data[-1])

        return day_patterns                    # Returns the dictionary.

    def append_output_to_file(self, dictionary, stock_name):
        """
            Writes the pattern analysis result to the output file.
        """
        
        result_file = open(f'{stock_name}_analysis_file.txt', 'a')  # Opens the result file in append mode.
        for item in list(dictionary.items()):                       # Traverses through the dictionary items.
            if item[1]:                                             # Does not include the item if no pattern found.
                string_to_append = str(item).replace("(", "").replace(")", "").replace(",", ":", 1)
                result_file.write(string_to_append + "\n")          # Writes the dictionary item to the result file.

        result_file.close()   # Closes the result file.

