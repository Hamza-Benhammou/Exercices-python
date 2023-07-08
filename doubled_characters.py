
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# def double_char(s):

# solution


def double_char(s):
    doubled_string = ''
    for char in s:
        doubled_string += char * 2
        return doubled_string