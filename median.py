"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(numbersList):
    numbersList = sorted(numbersList)
    if len(numbersList) % 2 == 1: # odd number length
        return numbersList[len(numbersList)//2]
    else: # even number length
        num1 = numbersList[len(numbersList)//2 - 1]
        num2 = numbersList[len(numbersList)//2]
        return (num1 + num2)/2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(numbers))
