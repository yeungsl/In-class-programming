# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:53:59 2015

@author: Sailung Yeung
email: yeungsl@bu.edu
"""
import random
import math
import matplotlib.pyplot as plt
## problem one
## (a)

def nextPoisson(lamb):
    d = random.random()
    sumr = 0.0
    ## controling k in 0- 20, since we long focus on the p in Rng[0...20]
    for k in range(21):
        sumr += ((lamb ** k) * (math.e ** (-1 * lamb)))/(math.factorial(k))
        if (sumr > d):
            return k
        if k == 20:
            return k
# c is the times of trials of getting the simulated poisson distribution
def Poi(lamb, c):
    
    count = [0] * 21
    for i in range(c + 1):
        num = nextPoisson(lamb) 
        count[num] += 1
    lsr = [i / c for i in count]
    return lsr
    
## (b)
    
def poisson(lamb, k):
#  return P(X=k)
    upper = (lamb ** k) * (math.e ** (-1 * lamb))
    lower = math.factorial(k)
    
    return(upper / lower)    
    
    
# c is the times of trials of getting the simulated poisson distribution
def comparePoi(lamb, c):
    ## controling k in 0- 20, since we long focus on the p in Rng[0...20]
    R = [0] * 21
    P = [0] * 21
    for k in range(21):
        R[k] = k
        P[k] = poisson(lamb, k)
    
    Ps = Poi(lamb, c)
    
    bins = [r - 0.5 for r in range(min(R),max(R)+2)]
    plt.title("Comparing of the simulated and the theoretical Poisson distribution")
    plt.ylabel("Probability")
    plt.xlabel("Outcomes")
    plt.hist(R,bins,histtype = "stepfilled", weights = P, color = "b",label = "Poisson")
    plt.hist(R,bins,histtype = "stepfilled",normed = True,weights = Ps, color = "r",alpha = 0.5,label = "Actual")
    plt.legend()
    
    
## Problem Two
## (a)

def nextGeometrical(p):
    d = random.random()
    sumr = 0.0
    ## controling k in 0- 20, since we long focus on the p in Rng[0...20]
    for k in range(21):
        sumr += (((1-p) ** k) * p)
        if (sumr > d):
            return k
        if k == 20:
            return k
# c is the times of trials of getting the simulated poisson distribution         
def Geo(p, c):
    count = [0] * 21
    for i in range(c + 1):
        num = nextGeometrical(p) 
        count[num] += 1
    lsr = [i / c for i in count]
    return lsr
    
## (b)
    
def G(p, k):
#  return P(X=k)
    r = ((1-p) ** k) * p
    
    return r
    
# c is the times of trials of getting the simulated poisson distribution
def compareG(p, c):
    ## controling k in 0- 20, since we long focus on the p in Rng[0...20]
    R = [0] * 21
    P = [0] * 21
    for k in range(21):
        R[k] = k
        P[k] = G(p, k)
    
    Ps = Geo(p, c)
    
    bins = [r - 0.5 for r in range(min(R),max(R)+2)]
    plt.title("Comparing of the simulated and the theoretical Geometrical distribution")
    plt.ylabel("Probability")
    plt.xlabel("Outcomes")
    plt.hist(R,bins,histtype = "stepfilled", weights = P, color = "b",label = "Geometrical")
    plt.hist(R,bins,histtype = "stepfilled",normed = True,weights = Ps, color = "r",alpha = 0.5,label = "Actual")
    plt.legend()
    
## Problem Three
    
def ChiSquared(Obs,Exp):                  
# takes two histograms (lists of frequency counts) Obs and Exp and returns X2 statistic
    X2 = (Obs - Exp) ** 2 / (Exp)
    return X2
    
## helper function
## a function used to calculate the Choosing K number from N
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
    
def binomial(n,p,k):
    P = (p**k) * ((1-p)**(n-k)) * C(n,k)
    return P

def getBinomial(n,p):
    lsr = []
    lsp = []
    for i in range(n+1):
        lsp += [binomial(n,p,i)]
        lsr += [i]
    X = (lsr,lsp)
    return X   
    
def prob3(N, p):
    ##(1)
    (r, Pb) = getBinomial(N,p)
    Pp = []
    for n in range(N+1):
        Pp += [poisson(N*p,n)]
        
    ##(2)
    O = Pp
    E = Pb
    ##(3)
    r = 0.0
    for i in range(N+1):
        r += ChiSquared(O[i],E[i])
    return r
    
    
## Problem Four
def prob4(lamb, C):
    E = [0] * 21
    for k in range(21):
        E[k] = poisson(lamb, k)
    
    O = Poi(lamb, C)
    r = 0.0
    for i in range(21):
        r += ChiSquared(O[i], E[i])
    return r