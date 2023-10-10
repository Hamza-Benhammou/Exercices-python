# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

# def maps(a):

# solution

def maps(a):
    new_array = []
    for num in a:
        new_array.append(num * 2)

    return new_array