# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:05:57 2015

@author: Sailung Yeung
email: yeungsl@bu.edu
"""
##cs 237 lab2

## Problem One

##(a)

def P(N,K):
    i = 1  
    r = N-K+1  
    while (N >= r): ## N will keep decreasing by and will be timed into the product of the previous numbers
        i *= N      ## stop the while loop if the N is smaller than the N-K+1 which should stop including to the formula
        N -= 1
    return i

"""
the result of P(14,5), P(300,100), and P(300,200):

>>> P(14,5)
240240
>>> P(300,100)
388073871930164836456833719241672754395800230088084344989365493081608402429819987
183923915365749209227783809215424452868912469966624757740910578635227970820611937
899469540337072285732213325595760757119468974039367680000000000000000000000000
>>> P(300,200)
3279437730980019186281705623806830644845013039006085173981251378493899701212168518
42356184685712825632014264627117755632402345611746842669512470914001200904928134
714415837392622354400568340396297551130259875864371286738821821734751391938425380
405054844783183834887733584127846679520819537945049903902962831618186851330195682
974549249883451789905767522387567180014514916250014858077229587277512630516465008
6400000000000000000000000000000000000000000000000000
>>> 

"""

##(b)

def C(N,K):
    if (K < N/2):
        K = N-K
    row = [1] * (K+1)
    nrow = N-K
    for i in range(1, nrow+1):
        
        above = row
        row[i-1] = above[i]
        for c in range(i, K+1):
            
            row[c] = above[c] + row[c-1]
    
    return row[-1]
        
"""
the result of C(300,100) and C(300,200):

>>> C(300,100)
4158251463258564744783383526326405580280466005743648708663033657304756328324008620
>>> C(300,200)
4158251463258564744783383526326405580280466005743648708663033657304756328324008620
>>> 

"""

## Problem Two

##(a)
## just listing out the ways as in the home work
## using P(N,K) as calculator
def problem4():
    ra = (2*P(4,4)*P(6,6))/(P(10,10))
    
    rb = (P(6,6)*P(7,4))/(P(10,10))
    
    return("(a): ", ra , "(b): ", rb)
    
"""
>>> problem4()
('(a): ', 0.009523809523809525, '(b): ', 0.16666666666666666)
>>> 
"""      
    
##(b)
## using C(N,K) as calculator
def problem7():
    ra = C(11,5)/C(25,5)
    rb = (C(11,5)+C(8,5)+C(6,5))/C(25,5)
    rcf = (C(8,3)*C(11,2))+(C(11,3)*C(8,2))
    rcs = (C(8,3)*C(6,2))+(C(6,3)*C(8,2))
    rct = (C(11,3)*C(6,2))+(C(6,3)*C(11,2))
    rc = (rcf+rcs+rct)/C(25,5)
    return("(a): ", ra, "(b): ", rb, "(c): ", rc)

"""
>>> problem7()
('(a): ', 0.008695652173913044, '(b): ', 0.009862601166948993, '(c): ', 0.2385657820440429)
>>> 
"""

## Problem Three

##(a)

letter = ['A', 'B', 'C', 'D', 'E', 'F']
    
def permute(N,L):
    X = [0]*L
    permuteAux(N,X,0)
    
def permuteAux(N,X,I):
    if(I >= len(X)):
        print(X)
        
    else:
        for j in range(N):
            if I == 0:      ### by resetting the x back to empty array to add next letter in it
                X = [0,0,0]
            if I == 1:     ### by reseetting the last element in to zero to add next letter
                X[-1] = 0
            
            if letter[j] not in X:  ## adding a if statment to see if the letter is in X
                                    ## if it is not in X the print it, else pass it and keep going
                X[I] = letter[j]
                permuteAux(N,X,I+1)
                
"""
>>> permute(4,3)
['A', 'B', 'C']
['A', 'B', 'D']
['A', 'C', 'B']
['A', 'C', 'D']
['A', 'D', 'B']
['A', 'D', 'C']
['B', 'A', 'C']
['B', 'A', 'D']
['B', 'C', 'A']
['B', 'C', 'D']
['B', 'D', 'A']
['B', 'D', 'C']
['C', 'A', 'B']
['C', 'A', 'D']
['C', 'B', 'A']
['C', 'B', 'D']
['C', 'D', 'A']
['C', 'D', 'B']
['D', 'A', 'B']
['D', 'A', 'C']
['D', 'B', 'A']
['D', 'B', 'C']
['D', 'C', 'A']
['D', 'C', 'B']
>>> 

"""

##(b)
   
def combinate(N,L):
    X = [0]*L
    combinateAux(N,X,0)
    
def combinateAux(N,X,I):
    
    if(I >= len(X)):
        print(X)
        
    else:
        for j in range(N):
            s = 0
            if I == 0:
                
                X = [0,0,0]
            if I == 1:
                X[-1] = 0
                
            if not X[I-1] == 0:
                
                s = ord(X[I-1])  ## have a numbered value for the element in the array
                                ## if the letter -s >= 0 then the inputting letter[j] is after s in alphabetical order
            if letter[j] not in X and ord (letter[j]) - s >= 0: ##Just adding one more condition compare to the permute
                                            ## put the letter into X if the letter comes after the letter in the X
                X[I] = letter[j]
                combinateAux(N,X,I+1)

"""
>>> combinate(4,3)
['A', 'B', 'C']
['A', 'B', 'D']
['A', 'C', 'D']
['B', 'C', 'D']
>>>
"""  

## Problem Four


## Simulation for 10
import random

## helper function which draw two cards and record both of them into a 2-D array
def carddrawer(N):
    cardf = [[0 for x in range(13)] for x in range(4)]
    cards = [[0 for x in range(13)] for x in range(4)]    
    for i in range(N):
        (r0,c0)=(random.randint(1,4) , random.randint(1,13))  ## draw two cards N times
        (r1,c1)=(random.randint(1,4) , random.randint(1,13))
        while (not r1 == r0 and not c1 == c0):                  ## make sure it is without replcement
            (r1,c1) = (random.randint(1,4) , random.randint(1,13)) ## if the second one equals the frist one redo the second one untill it gets different cards
        cardf[r0-1][c0-1] += 1     ## put their value into a 2-D array
        cards[r1-1][c1-1] += 1
    return (cardf, cards)
    
## for different problem from (a) to (d), give different if statment to make sure the condition is right
def simulation(char,N):
    (f,s) = carddrawer(N)    
    countf = 0
    counts = 0
    if char == "a": ### The first card is not a ten of clubs([3][9]) or an ace([0-3][0]);
        f[3][9] = 0 ### setting the number of card get into zero since we do not need to count the number in there
        f[0][0] = 0 ### this is for  four aces
        f[1][0] = 0
        f[2][0] = 0
        f[3][0] = 0
        for j in range(4):
            for k in range(13):
                countf += f[j][k]
        
        print("result for the simulation of (a) is: ")
        return countf/N
    if char == "b": ###The first card is an ace([0-3][0]), but the second is not([0-3][0]);
        
        for j in range(4):
            countf += f[j][0] ### only counts for the ones that are ace for first card set
            for k in range(1,13):
                counts += s[j][k] ### only counts for the ones that are not ace for second card set
        
        
        print("result for the simulation of (b) is: ")
        result = (countf/N) * (counts/N)
        return result
        
        
        
    if char == "c": ###At least one card is a diamond;
    ## first calculate the probability of no diamond
        f[2] = [0]*13 ## canceling all the diamond count
        s[2] = [0]*13
        
        for i in range(4):
            for j in range(13):
                countf += f[i][j]
                counts += s[i][j]
        result  = (countf/N) * (counts/N)
        print("result for the simulation of (c) is: ")
        return 1- result ## to get the compliment probability of no diamond, whihc should be the probability of at least one diamond
        
    if char == "d": ###Not more than 1 card is a picture card (jack, queen, king);
    ## three conditions
    ## first: possibility of no picture cards for two drawn card
    
        for j in range(4):
            for k in range(10): ## not counting the counts of the picture cards 
                countf += f[j][k]
                counts += s[j][j]
        resultf =  (countf/N) * (counts/N)
        
    ## second: possibility of one picture cards for the first drawn card
        n_countf = 0  ## since only the first drawn card will have a picture, we only have a new variable for counter the first one
        for j in range(4):
            for k in range(10,13):
                n_countf += f[j][k]
        results = (n_countf/N) * (counts/N)
    
    ## third: possibility of one picture cards for the second drawn card
        n_counts = 0 ## samething above with counting the second drawn card
        for j in range(4):
            for k in range(10,13):
                n_counts += f[j][k]
        resultt = (countf/N) * (n_counts/N)
        
        return(resultf + results + resultt)
    
"""
>>> simulation("a",1000000)
result for the simulation of (a) is: 
0.903846
>>> simulation("b",1000000)
result for the simulation of (b) is: 
0.070815022362
>>> simulation("c",1000000)
result for the simulation of (c) is: 
0.43774074570199994
>>> simulation("d",1000000)
0.946088697791
>>> 



"""  
    
    
    
    
    
    
    