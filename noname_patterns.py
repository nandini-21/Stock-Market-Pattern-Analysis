"""
    This contains the functions that determine whether a pattern exist in the data passed to it or not
    Inputs are lists with the following order of prices: open, low, high, close, date
    Functions return the name of the pattern if it exists. Otherwise, they return None datatype
"""


def almost_same(price1, price2):
    """ Returns true if the difference between the prices is less than or equal to 4%"""
    percent_diff = (price2 - price1) * 100 / max(price1, price2)
    return -4 < percent_diff < 4


def bull_engulfing(day1, day2):
    """
        Checks for bullish engulfing pattern:
        1) The close of day 1 must be greater than the open of day 2.
        2) The close of day 2 must be greater than the open of day 1 (should not be almost same).
        3) Day 2 must be bullish.
        4) Day 1 must be bearish.
    """

    if day1[0] > day1[3]:                       # Check for 4
        if day2[0] < day2[3]:                   # Check for 3
            if day2[0] <= day1[3]:              # Check for 1
                if day2[3] > day1[0]:           # Check for 2
                    return 'Bullish engulfing- (profit)'
    else:
        return None


def piercing(day1, day2):
    """
        Checks for piercing pattern:
        1) The close of day 1 must be almost same as open of day 2.
        2) The close of day 2 should be between half and open of day 1.
        3) Day 2 must be bullish.
    """

    if day2[3] > day2[0]:                                   # Check for 3
        if almost_same(day1[3], day2[0]):                   # Check for 1
            if (day1[0]+day1[3])/2 <= day2[3] <= day1[0]:   # Check for 2
                return 'Piercing- (profit)'
    else:
        return None


def morning_star(day1, day2, day3):
    """
        Checks for morning star pattern:
        1) The open and close of day 2 are almost the same.
        2) The close of day 1 is almost the same as open of day 3
        3) The high of day 2 is less than midpoint of the body of both day 1 and day 3.
        4) The high/open/close of day 2 is the same as close of day 1 or open of day 3.
    """

    if almost_same(day2[0], day2[3]):                                                       # Check for 1
        if almost_same(day1[3], day3[0]):                                                   # Check for 2
            if (day2[2] < (day1[0] + day1[3])/2) and (day2[2] < (day3[0] + day3[3])/2):     # Check for 3
                for price in day2:                                                          # Check for 4
                    if almost_same(price, day1[3]) or almost_same(price, day3[0]):
                        return 'Morning star- (profit)'
    else:
        return None


def hammer(day):
    """
        Checks for hammer pattern:
        1) The body of the candle must be <= the wick below.
        2) The wick above must be smaller than the body of the candle.
    """

    if (max(day[0], day[3]) - min(day[0], day[3])) <= (min(day[0], day[3])-day[1]):         # Check for 1
        if (day[2] - max(day[0], day[3])) <= (max(day[0], day[3]) - min(day[0], day[3])):   # Check for 2
            return 'Hammer- (profit)'
    else:
        return None


def bear_engulfing(day1, day2):
    """
        Checks for bearish engulfing pattern:
        1) The close of day 1 must be lesser than the open of day 2.
        2) The close of day 2 must be lesser than the open of day 1.
        3) Day 2 must be bearish.
        4) Day 1 must be bullish.
    """

    if day1[0] < day1[3]:                           # Check for 4
        if day2[0] > day2[3]:                       # Check for 3
            if day2[0] >= day1[3]:                  # Check for 1
                if day2[3] < day1[0]:               # Check for 2
                    return 'Bearish engulfing- (loss)'
    else:
        return None


def evening_star(day1, day2, day3):
    """
        Checks for evening star pattern:
        1) The open and close of day 2 are almost the same.
        2) The close of day 1 is almost the same as open of day 3
        3) The low of day 2 is more than midpoint of the body of both day 1 and day 3.
        4) The high/open close of day 2 is the same as close of day 1 or open of day 3.
    """

    if almost_same(day2[0], day2[3]):                                                       # Check for 1)
        if almost_same(day1[3], day3[0]):                                                   # Check for 2)
            if (day2[1] > (day1[0] + day1[3])/2) and (day2[1] > (day3[0] + day3[3])/2):     # Check for 3)
                for price in day2:                                                          # Check for 4)
                    if almost_same(price, day1[3]) or almost_same(price, day3[0]):
                        return 'Evening star- (loss)'
    else:
        return None


def dark_cloud(day1, day2):
    """
        Checks for dark cloud cover pattern:
        1) The close of day 1 must be almost same as open of day 2.
        2) The close of day 2 should be between half and open of day 1.
        3) Day 2 must be bearish.
    """

    if day2[0] > day2[3]:                                       # Check for 3)
        if almost_same(day1[3], day2[0]):                       # Check for 1)
            if (day1[0] + day1[3]) / 2 >= day2[3] > day1[0]:    # Check for 2)
                return 'Dark cloud cover- (loss)'
    else:
        return None


def shooting_star(day):
    """
        Checks for shooting star pattern:
        1) The body of the candle must be <= the wick above.
        2) The wick below must be smaller than the body of the candle.
    """

    if (max(day[0], day[3]) - min(day[0], day[3])) <= (day[2] - max(day[0], day[3])):       # Check for 1)
        if (min(day[0], day[3]) - day[1]) <= (max(day[0], day[3]) - min(day[0], day[3])):   # Check for 2)
            return 'Shooting star- (loss)'
    else:
        return None
