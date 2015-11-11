# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:04:20 2015

@author: Sailung Yeung
email: yeungsl@bu.edu
"""
## problem 1: drawing histograms

## base code is provided

import matplotlib.pyplot as plt
import random
import math
    
    
## rewrite the code    
def drawHistogram(X, title = "Histogram", printValues = False):
    
    # bins is a list of numbers
    bins = [x -0.5 for x in range(min(X),max(X)+2)] ## to get rid of duplicated elements
    plt.title(title)
    plt.ylabel("Frequency")
    plt.xlabel("Outcomes")
    (a,b,_) = plt.hist(X,bins)
    plt.show()
    if printValues == True:
        
        print("Frequencies: " + str(a))
        print("Bin boundaries:" + str(b))


## problem 2: PMFs and CDFs

def drawDistribution(X,P,title = "Example Distribution", CDF = False):
    
    ##same as the in problem 1 bin need a value
    bins = [x - 0.5 for x in range(min(X),max(X)+2)]
    ## check if CDF is on, if it is no the perform CDF, not then PMF
    if CDF == False:
        plt.title(title)
        plt.ylabel("Probability")
        plt.xlabel("Outcomes")
        plt.hist(X, bins, normed = True, weights = P)
        plt.show()
    else:
        plt.title(title)
        plt.title(title)
        plt.ylabel("Probabiltiy")
        plt.xlabel("Cumulative Distribution")
        plt.hist(X,bins, normed = True, cumulative = True, weights = P)
        plt.show()
        

## problem 3:  

def doProb3(N):
    ##using the value provide in the last problem
    X = [2,3,4,5,6,7,8,9,10,11,12]
    
    ##creating bins including to X
    bins = [x - 0.5 for x in range(min(X),max(X)+2)]
    
    ##the given probability would be the analytical weight of the probability
    W = [0.0278, 0.0556,0.0833,0.1111,0.1389,0.1667,0.1389,0.1111,0.0833,0.0556,0.0278]
    
    ##creating a new list to gather data for experimental
    F = [0] * 11
    
    ##rolling dice for N times
    for i in range(N):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        sumr = r1 + r2
        F[sumr-2] += 1
    
    ##the weight for the experimental graph
    P = [p/N for p in F]
    ##drawing graph
    plt.title("Analytical/Experimental Distribution for Two Dice")
    plt.ylabel("Probability")
    plt.xlabel("Outcomes")
    plt.hist(X,bins,histtype = "stepfilled",normed = True, weights = W, color = "b",label = "Analytical")
    plt.hist(X,bins,histtype = "stepfilled",normed = True, weights = P, color = "r", alpha = 0.5,label = "Experimental")
    plt.legend()
    plt.show()



## problem 4:

def doProb4(N):
    ##using the value for the base
    K = [0,1,2,3,4,5]
    
    ##creating bins
    bins = [x - 0.5 for x in range(min(K),max(K)+2)]
    
    ##the mathematical probability would be the analytical weight of the probabilty
    ##calculating the probability one by one
    W = [math.pow((40/52),5), (12/52) * math.pow((40/52),4) * 5, (12/52) * (12/52) * math.pow((40/52),3) * 10, math.pow((12/52),3) * math.pow((40/52),2)*10, math.pow((12/52),4) * (40/52)*5, math.pow((12/52),5)]
    
    
    
    #creating a new list to gather data for experimental part
    F = [0] * 6
    for i in range(N):
        count = 0 ## count how many face cards
        for j in range(5): ##draw five cards at a time
            suit = random.randint(1,4)
            number = random.randint(1,13)
            card = [suit,number]
            if card[1] > 10:
                count += 1
        F[count] += 1
    
    ##getting the weight of experiment
    P = [p/N for p in F]
    
    ##drawing graph
    plt.title("Analytical/Experimental Distribution for drawing cards")
    plt.ylabel("Probability")
    plt.xlabel("Outcomes")
    plt.hist(K,bins,histtype = "stepfilled",normed = True, weights = W, color = "b",label = "Analytical")
    plt.hist(K,bins,histtype = "stepfilled",normed = True, weights = P, color = "r", alpha = 0.5,label = "Experimental")
    plt.legend()
    plt.show()

