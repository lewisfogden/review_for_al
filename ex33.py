# Exercise 33 - commaFormat

def commaFormat_f(number):
    # f string version
    return f"{number:,}"

assert commaFormat_f(1) == '1'
assert commaFormat_f(10) == '10'
assert commaFormat_f(100) == '100'
assert commaFormat_f(1000) == '1,000'
assert commaFormat_f(10000) == '10,000'
assert commaFormat_f(100000) == '100,000'
assert commaFormat_f(1000000) == '1,000,000'
assert commaFormat_f(1234567890) == '1,234,567,890'
assert commaFormat_f(1000.123456) == '1,000.123456'

# bit lazy, more basic - gave up as getting late and I didn't quite get it right!
"""
def commaFormat(number):
    # turn it into a string
    str_num = str(number)
    if "." in str_num:
        # floating, chop up at the "."
        split_num = str_num.split(".")
        suffix = "." + split_num[1]
        str_num = split_num[0] # now an integer
    else:
        suffix = ""
    
    #deal with the integer part (this is now str_num)
    str_int = str_num # 
    prefix = ""
    # chop up str_num, and add to prefix with "," in between
    l = len(str_num)
    # can use something along the lines of l // 3 to work out how many commas there are
    # then insert them appropriately (and move the counter along one each time)
    

    # stick it together
    return int_str + suffix
"""

# check on supplied code
def commaFormat(number):
    # Convert the number to a string:
    number = str(number)
    # Create a variable to hold triplets of digits and the
    # comma-formatted string as it is built:
    triplet = ''
    commaNumber = ''
    # Remember the fractional part and remove it from the number, if any:
    if '.' in number:
        fractionalPart = number[number.index('.'):]
        number = number[:number.index('.')]
    else:
        fractionalPart = ''
    # Loop over the digits starting on the right side and going left:
    for i in range(len(number) - 1, -1, -1):
    # Add the digits to the triplet variable:
        triplet = number[i] + triplet
    # When the triplet variable has three digits, add it with a
    # comma to the comma-formatted string:
        if len(triplet) == 3:
            commaNumber = triplet + ',' + commaNumber
            # Reset the triplet variable back to a blank string:
            triplet = ''
    # If the triplet has any digits left over, add it with a comma
    # to the comma-formatted string:
    if triplet != '':
        commaNumber = triplet + ',' + commaNumber

    # Return the comma-formatted string:
    return commaNumber[:-1] + fractionalPart

print("part 2")
assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'