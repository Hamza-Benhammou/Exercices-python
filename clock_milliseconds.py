# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since midnight in milliseconds.

# def past(h, m, s):

# solution

def past(h, m, s):
    milliseconds = ((h * 60 + m) * 60 + s) * 1000
    return milliseconds