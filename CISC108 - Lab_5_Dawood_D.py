"""
Course: CISC108
Assignment: Lab 05
Author: Dina Dawood
"""

from cisc108 import assertEqual
import random
import math


# Problem 1:
n=1
def pattern(n):
    '''
    Computes n = 5 and prints a shape formed by asterisks going up to 5 and back
    Parameters:
        n: (int) - random integer n
    Returns:
        None
    '''
    while n<6:
        print ("*" * n)
        n = n+1
    while n>0:
        print ("*" * n)
        n = n-1
   
# Problem 2:

def evenNum():
    '''
    Computes num and prints a statement whether it's true or false
    Parameters:
        None
    Returns:
        None
    '''
    while True:
        num = int(input("Enter an even number: "))
        if num % 2 == 0:
            break
        print("Sorry that's not an even number")
    print("The number you entered", "'", num, "'", "is even")

# Problem 3:

def letter():
    '''
    Computes letter (lowercase only) and prints statement whether true or false
    Parameters:
        None
    Returns:
        None
    '''
    while True:
        letter = input("Enter a letter between a-z (lower): ")
        if len(letter) == 1 and letter.islower() :
            break
        print("Sorry that's not a letter between a-z")
    print("The letter you entered", "'", letter, "'", "is between a-z")

# Problem 4:

def digit_sum(n):
    '''
    Computes an integer n and returns the sum of all the digits
    Parameters:
        n: (int) - random integer n
    Returns:
        sum: (int) - sum of all digits
    '''
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n//10
    return sum

# Problem 5:

def guessing_game():
    '''
    Computes a random int from 1-10 and asks user to guess it
    Parameters:
        None
    Returns:
        None
    '''
    num = random.randint(1, 10)
    guess = int(input("Guess number btw 1-10: "))
    while guess != num:
        print("Wrong, guess again")
        guess = int(input("Guess number btw 1-10: "))
        if guess == 0:
            break
    print("Correct, you win!")
        
# Problem 6:

def multiplication_table():
    '''
    Computes values from user and creates a multiplication table
    Parameters:
        None
    Returns:
        None
    '''
    start = int(input("Enter start value: "))
    end = int(input("Enter end value: "))
    print('', end='\t')
    for row in range(start, end + 1):
        print(row, end = "\t")
    print()
    for row in range(start, end + 1):
        print(row, end = "\t")
        for col in range(start, end + 1):
            print(row * col, end = "\t")
        print()
        
# Problem 7:

def reverse_string(s):
    '''
    Computes a string and returns it in reverse order
    Parameters:
        s: (str) - random string s
    Returns:
        reverse: (str) - reverse string
    '''
    reverse = ""
    for char in s:
        reverse = char + reverse
    return reverse

# Problem 8:

def blank_index(string):
    '''
    Computes a string and returns the last index value of it
    Parameters:
        string: (str) - random string 
    Returns:
        index: (int) - last index value
    '''
    index = None
    for i in range(len(string)):
        if (string[i] == ' '):
            index = i
    return index
    
# Problem 9:

def print_histogram(lst):
    '''
    Computes a list of numbers and prints a histogram with asterisks 
    Parameters:
        lst: (list) - list of random integers
    Returns:
        None
    '''
    for value in lst:
        if (value > 0):
            print("*" * int(value))
        else:
            print()

# Problem 10:

def count_odds(lst, lower_bound, upper_bound):
    '''
    Computes and returns value of all  odd integers in the list btw bounds
    Parameters:
    lst: (list) - list of integers
    lower_bound: (int) - Starting range
    upper_bound: (int) - Ending range
      
    Returns:
    count: (int) - Number of odd numbers in the range
    '''
    count = 0
    for i in lst:
        if (i >= lower_bound) and (i <= upper_bound):
            if (i % 2 == 1):
                count = count + 1
    return count
    
assertEqual(count_odds([0, 30, 50, 80], 0, 80), 0)
assertEqual(count_odds([19, 30, 13, 6, 22, 8, 27], 0, 30), 3)
assertEqual(count_odds([5, 49, 20, 74, 13, 37, 66], 0, 100), 4)

# Problem 11:

#### COULDN'T GET IT TO WORK, KEPT GETTING TYPE ERROR AND NAME ERROR FOR PARAMETERS

def weighted_total(number_list, weights):
    '''
    Returns the weighted total of the values in list
    Parameters:
        number_list: (list) - list of numbers
        weights - (list) - list of weights
  
    Returns:
        total_weight: (int) - The weighted total of the numbers
    '''
    total_weight = 0
    for i in range(len(number_list)):
        total_weight += (number_list[i] * weights[i])
    return total_weight

assertEqual(round(weighted_total([1,2,3],[.1,.5,.4]),2), 2.3)
assertEqual(weighted_total([1, 2, 3], [4, 5, 6]), 32)
assertEqual(weighted_total([10, 22, 35], [23, 9, 16]), 988)


# Problem 12:
def num_negatives(lst):
    '''
    Computes a list and prints the number of negative integers in list
    Parameters:
        lst: (list) - random list of numbers
    Returns:
        None
    '''
    for num in lst:
        if num < 0:
            print(num, end = " ")

# Problem 13:

def remove_dash(string):
    '''
    Computes a string and returns it with the dashes
    Parameters:
        string: (str) - random string
    Returns:
        string: (str) - spilt string
    '''
    return string.split("-")

assertEqual(remove_dash("good-bye"), ["good", "bye"])
assertEqual(remove_dash("hello"), ["hello"])
assertEqual(remove_dash("cisc-108"), ["cisc", "108"])


# Problem 14:

def weave(str1, str2):
    '''
    Computes two strings and returns them interleaved together
    Parameters:
        str1: (str) - random string
        str2: (str) - random string
    Returns:
        weave_string: (str) - interleaved string
    '''
    length_min = min(len(str1), len(str2))
    weave_string = ''
    for i in range(length_min):
        weave_string += str1[i] + str2[i]
    if len(str1) == length_min:
        weave_string += str2[length_min:]
    else:
        weave_string += str1[length_min:]
    return weave_string

assertEqual(weave("hat", "cat"), "hcaatt")
assertEqual(weave("door", "mat"), "dmoaotr")
assertEqual(weave("book", "store"), "bsotookre")

# Problem 15:

def count_vowels(string):
    '''
    Computes a string and returns the number of vowels in that string
    Parameters:
        string: (str) - random string
    Returns:
        count: (int) - number of vowels
    '''
    count = 0
    vowel_list=['a','e','i','o','u','A','E','I','O','U']
    for letter in string:
        if letter in vowel_list:
            count += 1
    return count
    
assertEqual(count_vowels("hello"), 2)
assertEqual(count_vowels("bye"), 1)
assertEqual(count_vowels("ice cream"), 4)

# Problem 16:

def bools_2_str(lst):
    '''
    Computes a list of booleans and returns a string of the same length
    Parameters:
        lst: (list) - random list of true and/or false
    Returns:
        string: (str) - string of 'X' and ' ' based on true/false
    '''
    string = []
    for i in lst:
        if i == True:
            string.append('X')
        else:
            string.append(' ')
    return string

assertEqual(bools_2_str([True, False, True, False, True]), ['X', ' ', 'X', ' ', 'X'])
assertEqual(bools_2_str([True]), ['X'])
assertEqual(bools_2_str([False, True, False]), [' ', 'X', ' '])

# Problem 17:

def has_duplicates(lst):
    '''
    Computes a list and returns true if there are duplicates and false otherwise
    Parameters:
        lst: (list) - random list of numbers
    Returns:
        False/True: (bool) - whether there are duplicates
    '''
    duplicates = len(lst)
    for i in range(duplicates):
        if lst[i] in lst[i + 1:]:
            return True
    return False

assertEqual(has_duplicates([1, 2, 3, 1, 5]), True)
assertEqual(has_duplicates([1, 2, 3, 4, 5]), False)
assertEqual(has_duplicates([]), False)

# Problem 18:

def count_evens_NxN(nested_lst):
    '''
    Computes a nested list that represents a matrix and returns number of even numbers
    Parameters:
        nested_list: (list) - random list of lists of numbers
    Returns:
        count: (int) - number of even numbers in matrix
    '''
    count = 0
    for nums in nested_lst:
        for i in nums:
            if (i % 2 == 0):
                count = count + 1
    return count

assertEqual(count_evens_NxN([[1, 2], [3, 4], [5, 6]]), 3)
assertEqual(count_evens_NxN([[0, 4], [22, 80], [10, 75]]), 5)
assertEqual(count_evens_NxN([[5, 1], [56, 27], [18, 13]]), 2)

# Problem 19:

def diagonal_diff(nested_lst):
    '''
    Computes a nested list and returns the absolute difference btw sum of diagonals
    Parameters:
        nested_list: (list) - random list of lists of numbers
    Returns:
        (d1 - d2) or (d2 -d1): (int) - absolute difference
    '''
    num = len(nested_lst)
    d1 = 0
    d2 = 0
    for i in range(num):
        d1 = d1 + nested_lst[i][i]
        d2 = d2 + nested_lst[i][num-i-1]
    if (d1 > d2):
        return d1 - d2
    else:
        return d2 - d1

assertEqual(diagonal_diff([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15)
assertEqual(diagonal_diff([[0, 5, -10], [3, -7, 12], [33, -26, 19]]), 4)
assertEqual(diagonal_diff([[22, -42, 14], [2, 1, -11], [100, -25, -36]]), 128)

if __name__ == "__main__":
    pattern(n)
    evenNum()
    letter()
    print(digit_sum(456))
    guessing_game()
    multiplication_table()
    print(reverse_string("hello"))
    print(blank_index("Where are you, Will?"))
    print(print_histogram([0, 2, 4, 1]))
    print(count_odds([0, 30, 50, 80], 0, 80))
    print(weighted_total([1, 2, 3], [4, 5, 6]))
    print(num_negatives([1, 2, 3, -4, -5]))
    print(remove_dash("good-bye"))
    print(weave("hat", "cat"))
    print(count_vowels("hI"))
    print(bools_2_str([True, False, True, False, True]))
    print(has_duplicates([1, 2, 3, 1, 5]))
    print(count_evens_NxN([[1, 2], [3, 4], [5, 6]]))
    print(diagonal_diff([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))