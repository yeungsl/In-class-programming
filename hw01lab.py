# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:03:20 2015

@author: Sailung Yeung
email: yeungsl@bu.edu
"""

import random

## problem one: varification of the randomness
## (a)
def randomnessTest1(N):
    x = [0] * 10
    
    for i in range(0,N):
        r = random.randint(0,9)
        for j in range(0,10):  ## using for loop to count for each number generated.
            if r == j:
                x[j] += 1
                
    return x
    
"""
test1 result:

Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> runfile('/Users/davidyeung/Desktop/hw01lab.py', wdir='/Users/davidyeung/Desktop')
>>> runfile('/Users/davidyeung/Desktop/hw01lab.py', wdir='/Users/davidyeung/Desktop')
>>> randomnessTest1(10)
[1, 0, 6, 1, 0, 0, 0, 0, 1, 1]
>>> randomnessTest1(20)
[1, 0, 0, 2, 4, 5, 5, 2, 1, 0]
>>> randomnessTest1(1000000)
[100244, 99356, 100860, 99615, 99848, 100451, 99779, 99761, 99572, 100514]
>>> 

"""





##(b)
def randomnessTest2(N):
    x = [0] * 2
    
    for i in range(0, N):
        (l,r) = (random.random(),random.random())## generate two list at one time and compare them
        if l < r:
            x[1] += 1
        if l > r:
            x[0] += 1
    return x

"""
test2 result:

>>> runfile('/Users/davidyeung/Desktop/hw01lab.py', wdir='/Users/davidyeung/Desktop')
>>> randomnessTest2(10)
[5, 5]
>>> randomnessTest2(1000000)
[500532, 499468]
>>> 

"""






## problem two: simulation of dice roll
## (a)
def dieRoll(N):
    
    x = [0] *6
    for i in range(0, N):
       die = random.randint(1,6)
       
       for j in range(0,6):
           if die-1 == j:
               x[j] += 1
    print("result from 1 to 6: ")
    result  = [r/N for r in x]
    return result

"""
rolling dice result:

>>>> runfile('/Users/davidyeung/Desktop/hw01lab.py', wdir='/Users/davidyeung/Desktop')
>>> dieRoll(10)
result from 1 to 6: 
[0.2, 0.1, 0.2, 0.2, 0.0, 0.3]
>>> dieRoll(1000)
result from 1 to 6: 
[0.146, 0.182, 0.168, 0.155, 0.17, 0.179]
>>> dieRoll(1000000)
result from 1 to 6: 
[0.16617, 0.166351, 0.166782, 0.167103, 0.166796, 0.166798]
>>> 

"""







## (b)
def twoDiceRoll(N):
    x = [0] * 12
    for i in range(0,N):
        twodice = random.randint(1,6) + random.randint(1,6)
        for j in range(0,12):
            if twodice-1 == j:
                x[j] += 1
    
    print("result from 2 to 12: ")
    result = [r/N for r in x[1:]]
    return result

"""
result of rolling two dice:

>>> twoDiceRoll(1000000)
result from 2 to 12: 
[0.027812, 0.055541, 0.083114, 0.111081, 0.138827, 0.166786, 0.138878, 0.11099, 0.083482, 0.055408, 0.028081]
>>> 

"""








## problem three: simulation of coin flips(fair and unfair)
## helper function which simulate the flip of a coin
def nextFlip(p):
    n = random.random()
    
    
    if n < p:
        return True
        
    else:
        return False

## (a)
def coinSimulation(p, N):
    x = [0] * 2
    for i in range(0,N):
        f = nextFlip(p)
        if f:
            x[0] += 1
        else:
            x[1] += 1
    print("Heads: ", x[0])
    print("Tails: ", x[1])

"""
resulte of flipping coins:

>>> coinSimulation(0.5,1000000)
Heads:  500106
Tails:  499894
>>> coinSimulation(0.7,1000000)
Heads:  700360
Tails:  299640
>>> 

"""








## (b)
def coinTrial(p):
    x = [0] * 2
    for i in range(0,4):
        f = nextFlip(p)
        if f:
            x[0] += 1
        else:
            x[1] += 1
    return x
    
def coinExperiment(p, N):
    x =[0] * 5
    for i in range(0,N):
        (h,t) = coinTrial(p)
        x[h] += 1
    result = [r/N for r in x]
    
    print("result for getting 0 to 4 heads: ")
    return result

"""
results of flipping four coins at a time:

>>> runfile('/Users/davidyeung/Desktop/hw01lab.py', wdir='/Users/davidyeung/Desktop')
>>> coinExperiment(0.5, 1000000)
result for getting 0 to 4 heads: 
[0.062746, 0.250171, 0.374573, 0.250201, 0.062309]
>>> coinExperiment(0.7, 1000000)
result for getting 0 to 4 heads: 
[0.00801, 0.075419, 0.265205, 0.411736, 0.23963]
>>> 

"""







## (c)
def firstHead(p, N):
    x = [0] * 21
    for i in range(0, N):
        counter = 0
        while True:
            counter += 1
            if counter > 20:
                counter = 0
                i -= 1
                break
            if nextFlip(p):
                break
            
        x[counter] += 1
    result = [r/N for r in x[1:]]
    print("result for 1 to 20 flips to get a head: ")
    return result

"""
results of the probability of how many flips can get  a head:

>>> firstHead(0.5,1000000)
result for 1 to 20 flips to get a head: 
[0.499134, 0.250382, 0.125118, 0.062713, 0.031286, 0.01568, 0.007796, 0.003974, 0.001946, 0.001013, 0.000485, 0.000232, 0.000129, 5.2e-05, 3.5e-05, 1.5e-05, 4e-06, 4e-06, 0.0, 0.0]
>>> firstHead(0.7,1000000)
result for 1 to 20 flips to get a head: 
[0.699833, 0.210117, 0.063311, 0.018736, 0.005516, 0.001749, 0.000515, 0.000166, 3.4e-05, 1.9e-05, 3e-06, 0.0, 1e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> 

"""









## problem four: let's gamble
def playRound(k):
    total = 0
    while True:
        die = random.randint(1,6)
        total += die
        
        if total > 21:
            
            return 0
        if total > k:
            return total

def playgame():
    x = [0] * 21
    for K in range(1,22):
        for i in range(0,1000000):
            x[K-1] += playRound(K)
        x[K-1] /= 1000000
    print("result for the average payoff for a game from K = 1 to 21: ")
    return x

"""

>>> runfile('/Users/davidyeung/Desktop/hw01lab.py', wdir='/Users/davidyeung/Desktop')
>>> playgame()
result for the average payoff for a game from K = 1 to 21: 
[4.082303, 4.763476, 5.558736, 6.486298, 7.565053, 8.824024, 9.714003, 10.652023, 11.633965, 12.64533, 13.670828, 14.687335, 15.66595, 16.660252, 17.66069, 17.612829, 16.480169, 14.198165, 10.702995, 6.000288, 0.0]
>>> 

"""




