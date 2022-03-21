# 1. Multiplication
# Create a function that gets a number as a parameter, and then prints the multiplication table for that number from 1 
# to 10. E.g., when the parameter is 12, the first line printed is “1 x 12 = 12” 
# and the last line printed is “10 x 12 = 120.”

def multiplication( num ):
    i = 0
    while i <= num:
        print(f'{i} x 12 = ', i*12)
        i += 1

multiplication(10)

# 2. Sum of two strings
# Write a function that gets as parameters two strings. The function returns the number of characters 
# that the strings have in common. Each character counts only once, e.g., the strings "bee" and "peer"
# only have one character in common (the letter “e”). You can consider capitals different from lower case letters. 
# Note: the function should return the number of characters that the strings have in common, and not print it. 
# To test the function, you can print the result in your main program.
import collections
def sumStrs(str1, str2):
    sumStr = str1 + str2
    frequencies = collections.Counter(sumStr)
    duplicate = []
    # print("Freq :", frequencies)
    for key, value in frequencies.items():
        # print(key, value)
        if value > 1:
            duplicate.append(key)
    return len(duplicate)
print(sumStrs("HeelloD", "weorlLD"))

# 3. Guessing number
# Write a guessing number function that holds a random number between 1 and 10 and get a parameter number. 
# The return for that function will be :
# "Too big" if the parameter number is bigger than the held number.
# "Too small" if the parameter number is smaller than the held number.
# "You are SUPER" if the parameter number is the same as the held number.
# Enter the parameter number via the terminal with a help of the input method.

def guessNum(num):
    import random
    rand = random.randint(1,10)
    if num > rand:
        print("Too big ", rand)
    elif num < rand:
        print("Too small", rand)
    else:
        print("You are supper", rand)

i = input("Input your number: ")
guessNum(int(i))