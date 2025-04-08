import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    # Write your code here
     
    suma_total=total_amount(bill)
    suma_anna = fee_for_anna(bill,k)
    print(resultado(suma_total,suma_anna,b))
    
                   

def fee_for_anna(bill,k):
    summa=0
    for indice in range(len(bill)):
        if indice != k:
            summa += bill[indice]
    return int(summa /2)    
       
def total_amount(bill):
    suma_total=0
    for indice in range(len(bill)):
        suma_total= suma_total + bill[indice]
    return suma_total
    
    
def resultado(suma_t,suma_a,b_charged):
    total_entre_dos = int(suma_t/2)
    if total_entre_dos == b_charged:
        return b_charged - suma_a
    else:
        return "Bon Appetit"


bonAppetit([3, 10, 2, 9], 1, 12)