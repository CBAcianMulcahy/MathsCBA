"""
    * @author Cian Mulcahy
    * @version 0.0.1 01/03/2020
    * @since v3.6.8
    Simple Program to determine the probability of any random integer x being prime and graphing values using matplotlib
"""

from math import sqrt
from itertools import count, islice
from fractions import Fraction
import matplotlib.pyplot as plt

def isPrime(x):
    if x < 2:
        return False
    
    for n in islice(count(2), int(sqrt(x) - 1)):
        if x % n == 0:
            return False
        
    return True

def primeProbability(min, max, isReadable):
    counter = 0
    for i in range(min+1, max+1):
        if(isPrime(i)):
            counter+=1
    if(isReadable):
        return str(Fraction(counter, max-min)) + "   " + str(counter/(max-min))
    else:
        return counter/(max-min)

def graphPrimes(min, max):
    x = []
    y = []
    for i in range(min+1, max+1):
        x.append(i)
        y.append(primeProbability(min, i, False))
    del x[0]
    del y[0]
    plt.plot(x, y)
    plt.show()

graphPrimes(0, 10000)


        

