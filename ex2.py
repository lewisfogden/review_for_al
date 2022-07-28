# Exercise #2: Temperature Conversion

# check: (32°F − 32) × 5/9 = 0°C

# [°C] = ([°F] − 32) × 5⁄9
# [°F] = [°C] × 9⁄5 + 32

def convertToFahrenheit(degrees_celsius):
    return degrees_celsius * 9/5 + 32

def convertToCelsius(degrees_fahrenheit):
    return (degrees_fahrenheit- 32) * 5 / 9

print("Running tests")
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
print(convertToCelsius(convertToFahrenheit(42)))
assert convertToCelsius(convertToFahrenheit(42)) == 42
print("tests complete")