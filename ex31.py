# convert integers to strings

def convertIntToStr(n):
    # equvalent of str(n)
    # works for positive and negative integers
    # TODO: use "".join() rather than `+`

    # start with checking if negative
    #print("raw n", n)
    NUMS = "0123456789"
    if n < 0:
        # nail a negative sign to the start and keep going (with a positive)
        result = "-"
        n = abs(n)
    else:
        result = ""

    if n < 10:
        result += NUMS[n]
        return result
    else:
        # split n (e.g. 1234) into 123 and 4, by taking integer divisor and remainder
        # perfect for divmod!
        n, units = divmod(n, 10)
        result += convertIntToStr(n) + NUMS[units]
    return result

print(convertIntToStr(0))
print(convertIntToStr(5))
print(convertIntToStr(53))
print(convertIntToStr(23632623))
print(convertIntToStr(-1234))
print(convertIntToStr(-1))


for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)
