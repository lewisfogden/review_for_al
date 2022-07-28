# exercise 32 strings > integers

def convertStrToInt(stringNum):
    numbers_by_index = "0123456789" # or could use a dictionary

    # chop off the negative, and keep this for the end to correct the sign
    if stringNum[0] == "-":
            sign = -1
            stringNum = stringNum[1:]
    else:
            sign = 1

    # if we have "-1234"
    # construct as -1 * (1*1000 + 2*200 + 3*30 + 4)
    # can do this with a loop, scaling up number by 10 each time.
    number = 0 # start at zero
    for s in stringNum:
        # walk through each number
        number *= 10 # scale up all existing digits, e.g. 1 -> 10, 12 -> 120 etc
        # (as 10 * 0 = 0 we can do this from the start.)
        number += numbers_by_index.index(s) # lookup and return index
    
    return sign * number

print(convertStrToInt("-1234"))
print(convertStrToInt("-0"))
print(convertStrToInt("-5"))
print(convertStrToInt("555"))
print(convertStrToInt("-0009"))
print(convertStrToInt("987654321"))

for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i

# check on original
def convertStrToInt_orig(stringNum):
    # This dictionary maps string digits to single integer digits:
    DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    # Make a note whether the number is negative or not, and make
    # integerNum positive for the rest of the function's code:
    if stringNum[0] == '-':
        isNegative = True
        stringNum = stringNum[1:]
    else:
        isNegative = False
    # integerNum holds the converted integer, and starts off at 0:
    integerNum = 0
    # Track the power of ten to multiply digits by, starting at 1:
    powerOfTen = 1
    # Loop over the digits in the string, starting on the right end
    # of the string and going left:
    for i in range(len(stringNum) - 1, -1, -1):
        # Get the integer digit from the string digit:
        digit = DIGITS_STR_TO_INT[stringNum[i]]
        # Add this to the integer number:
        integerNum += digit * powerOfTen
        # Increase powerOfTen to the next power of ten:
        powerOfTen *= 10

    # If the number was originally negative, make the integer
    # negative before returning it:
    if isNegative:
        return -integerNum
    else:
        return integerNum

for i in range(-10000, 10000):
    assert convertStrToInt_orig(str(i)) == i