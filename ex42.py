# Bubble sort

def bubbleSort(numbers):
    total_numbers = len(numbers)
    for i in range(total_numbers - 1):
        for j in range(i + 1, total_numbers):
            if numbers[j] < numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j] # wrong way round - swap!
    return numbers

a = [2, 0, 4, 1, 3]
print(a)
print(bubbleSort(a))

assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
"""
import random
b = [random.randint(0, 10) for _ in range(20)]
print(b)
sorted_b = sorted(b)
print(bubbleSort(b))
print(sorted_b)
"""