import math
import os
import random
import re
import sys


def getTotalX(a,b):
    low_value = max(a)
    high_value = min(b)
    contador_divisiones=len(a)+len(b)
    counting = 0
    cont_final=0
    for val in range(low_value, high_value+1):
        for i in range(len(a)):
            if val % a[i] == 0:
                counting += 1
        for j in range(len(b)):
            if b[j] % val == 0:
                counting += 1
        if counting == contador_divisiones:
            cont_final += 1
        counting = 0
    return cont_final

print(getTotalX([2,4],[16,32,96])) 

