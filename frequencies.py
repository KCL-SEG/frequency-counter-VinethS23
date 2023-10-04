"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        currentItem = i
        if i in frequencies: 
            frequencies[str(currentItem)] += 1 
        else:
            frequencies[str(currentItem)] = 1
    return frequencies
# return call is the last statement of a function

#print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))