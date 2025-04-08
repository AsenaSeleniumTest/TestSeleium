import math
import os
import re
import sys


def pageCount(n, p):
    # Calculate the number of pages from the front and back
    front = p // 2
    back = (n // 2) - (p // 2)
    
    # Return the minimum of the two counts
    return min(front, back)

print(pageCount(6, 2))  