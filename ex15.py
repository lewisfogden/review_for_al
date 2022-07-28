# exercise 15: Median

def median(numbers):
    if len(numbers) == 0:
        return None
    # put them in order & get length
    sorted_numbers = sorted(numbers)
    length = len(numbers)

    # even or odd?
    if length % 2 == 0:
        # even, e.g.: length 6
        # [0, 1, 2, 3, 4, 5]  <- indices
        #        ^--^---------we want these  (2 and 3)
        upper = sorted_numbers[length // 2]
        lower = sorted_numbers[length // 2 - 1]
        return (upper + lower) / 2
    else:
        # odd, e.g.: length 5
        # [0, 1, 2, 3, 4] <- indices
        #        ^-------- index 2 calculated as: (4-0)/2
        return sorted_numbers[(length - 1) // 2]

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
assert median([1,]) == 1
assert median([1,2]) == 1.5

import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6