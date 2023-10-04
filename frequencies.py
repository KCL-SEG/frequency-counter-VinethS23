"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        currentItem = str(i)
        if currentItem in frequencies: 
            frequencies[currentItem] += 1 
        else:
            frequencies[currentItem] = 1
    return frequencies
# return call is the last statement of a function

print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))