# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:31:53 2015

@author: Sailung Yeung
email: yeungsl@bu.edu
"""

import math
import random


## Problem 6
##(a)
def nextExponential(lamb):
    u = random.random()
    t = (-1 * math.log(u)) / lamb
    return t
    
def Exponential(lamb, c):
    sumx = 0
    var = 0
    for i in range(c+1):
        x = nextExponential(lamb)
        sumx += x
        var += x ** 2
    mean = sumx / c
    var = (var /c) - mean ** 2
    print ('\nmean: ', mean)
    print ('\nVar: ', var)
    
def ExponentialE(lamb):
    return (1/ lamb)
    
def ExponentialVar(lamb):
    return (1 / lamb**2)
    
    
"""
comparing:

In [89]: Exponential(5,1000000)

mean:  0.1998767083902042

Var:  0.03981731325109584

In [90]: ExponentialE(5)
Out[90]: 0.2

In [91]: ExponentialVar(5)
Out[91]: 0.0

"""
##(b)
def nextNormal(mu , var):
    std = math.sqrt(var)
    mean = 0
    varN = 0
    for i in range(1000001):
        u = random.random()
        v = random.random()
        x = math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v)
        y = math.sqrt(-2 * math.log(u)) * math.sin(2 * math.pi * v)
        x = x * std + mu
        y = y * std + mu
        mean += x
        mean += y
        varN += x **2
        varN += y **2
    mean = mean / 2000002
    varN = (varN / 2000002) - mean **2
    print('\nMean: ', mean)
    print('\nVar:', varN)
    
"""
comparing:
In [97]: nextNormal(39.8, 4.2025)

Mean:  39.80084168683948

Var: 4.214580877850722

the mu and variance given:

39.8 and 4.2025


"""

##(c)
def c(k):
    r = 0
    cons = 10**(k)
    for j in range(cons + 1):
        counter = 0
        for i in range(21):
            u = random.random()
            v = random.random()
            x = math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v)
            y = math.sqrt(-2 * math.log(u)) * math.sin(2 * math.pi * v)
            x = x * 2.05 + 39.8
            y = y * 2.05 + 39.8
            mean = x + y
            mean /= 2
            if mean >= 40:
                counter += 1
                
        if counter == 5:
            r += 1
            
    return (r / cons)
        
        
"""
comparing:
In [107]: c(2)
Out[107]: 0.02

In [108]: c(3)
Out[108]: 0.032

In [109]: c(4)
Out[109]: 0.0312

In [110]: c(5)
Out[110]: 0.0285

In [111]: c(6)
Out[111]: 0.028625

the result of formlua :

p = 0.0303
"""