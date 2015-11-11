# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:18:36 2015

@author: Sailung Yeung
email: yeungsl@bu.edu
"""
import math
import random
import matplotlib.pyplot as plt

## problem one
## (a)

##helper function
def facproductls(L):
    p = 1
    for i in range(len(L)):
        p *= math.factorial(L[i])
    return p

def multinomial(X, L):
# Given a random variable X = (R,P) and a list L = [x1, ...., xk] of multiplicities of the outcomes,
# return the probability that P(X1=x1, X2=x2, ..., Xk=xk) as in the definition.
    (R, P) = X
    N = sum (L)
    multiconstant = math.factorial(N)/facproductls(L)
    r = 1
    for i in range(len(L)):
        r *= P[i]**L[i]
    r *= multiconstant 
    return r

"""
result:
In [34]: X = ([1,2,3,4,5,6] , [1/6,1/6,1/6,1/6,1/6,1/6])

In [35]: L = [1,1,1,1,2,2]

In [36]: multinomial(X,L)
Out[36]: 0.00600137174211248
    
"""
## (b)

##helper function
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

    
def hypergeometrical(N,K,n,k):
# Return the probability that in n draws without replacement from an urn with N ball, 
# of which K are red, you get k red ball
    upper = C(K,k) * C((N-K),(n-k))
    lower = C(N,n)
    
    return(upper / lower)
"""
In [47]: hypergeometrical(52, 13, 5, 3)
Out[47]: 0.0815426170468187

"""

def getH(N,K,n):
# Return a list of the probabilty of the hypergeometrical distribution
# required by problem three
    R = [0] * (n+1)
    P = [0] * (n+1)
    for i in range(n+1):
        R[i] = i
        P[i] = hypergeometrical(N,K,n,i)
        
    X = (R,P)
    return X



##(c)
def poisson(lamb, k):
#  return P(X=k)
    upper = (lamb ** k) * (math.e ** (-1 * lamb))
    lower = math.factorial(k)
    
    return(upper / lower)

"""
In [86]: poisson(7,2)
Out[86]: 0.02234110815608565

"""


## problem two
## (a)
def nextBernoulli(p):
    ran = random.random()
    
    if ran < p:
        return True
    if ran > p:
        return False
        
## (b)
        
def nextBinomial(n,p):
    
    counter = 0 
    for x in range(n):
       r = nextBernoulli(p)
       if r == True:
           counter += 1
           
    return counter

##(c)

def B(n, p):
    c = 1000000
    ls = [0]*(n+1)
    for x in range(c + 1):
        numofT = nextBinomial(n,p)
        ls[numofT] += 1
    return [r/c for r in ls]
        


def getBinomial(n,p):
    lsr = []
    lsp = []
    for i in range(n+1):
        lsp += [binomial(n,p,i)]
        lsr += [i]
    X = (lsr,lsp)
    return X

def binomial(n,p,k):
    P = (p**k) * ((1-p)**(n-k)) * C(n,k)
    return P
    
def compare(n,p):
    (R,P) = getBinomial(n,p)
    A = B(n,p)    
    
    bins = [r - 0.5 for r in range(min(R),max(R)+2)]
    plt.title("Comparing of the model and the Binomial distribution")
    plt.ylabel("Probability")
    plt.xlabel("Outcomes")
    plt.hist(R,bins,histtype = "stepfilled", weights = P, color = "b",label = "Binominal")
    plt.hist(R,bins,histtype = "stepfilled",normed = True,weights = A,color = "r",alpha = 0.5,label = "Actual")
    plt.legend()
    

"""
In [246]: B(20, 0.7)
Out[246]: 
[0.0,
 0.0,
 0.0,
 0.0,
 1.1e-05,
 3.5e-05,
 0.000225,
 0.001026,
 0.003839,
 0.012003,
 0.030782,
 0.065199,
 0.114367,
 0.16476,
 0.192034,
 0.178865,
 0.129985,
 0.071252,
 0.027972,
 0.006889,
 0.000757]
 
In [247]: getBinomial(20,0.7)
Out[247]: 
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
 [3.4867844010000104e-11,
  1.6271660538000045e-09,
  3.606884752590009e-08,
  5.049638653626012e-07,
  5.00755833151246e-06,
  3.738976887529303e-05,
  0.00021810698510587597,
  0.0010178325971607542,
  0.003859281930901192,
  0.012006654896137042,
  0.030817080900085062,
  0.06536956554563497,
  0.11439673970486117,
  0.16426198521723653,
  0.1916389827534426,
  0.17886305056987972,
  0.1304209743738706,
  0.07160367220526227,
  0.02784587252426865,
  0.006839337111223879,
  0.0007979226629761189]
  
  
In [251]: compare(20,0.7)
  
"""

## problem Three
## (a)
def nextHypergeometrical(N,K,n):
# returns a number in {0,1,...,min(K,n)} with probability as stated
    counter = 0
    ls = [i for i in range(N)]
    random.shuffle(ls)
    for i in range(n):
        if ls[i] < K:
            counter += 1
    
    return counter


def H(N,K,n):
# just to get the Hypergeometrical distribution by the data
    c = 1000000
    ls = [0]*(n+1)
    for x in range(c + 1):
        numofT = nextHypergeometrical(N,K,n)
        ls[numofT] += 1
    return [r/c for r in ls]


def compareH(N,K,n):
    (R,P) = getH(N,K,n)
    A = H(N,K,n)    
    
    bins = [r - 0.5 for r in range(min(R),max(R)+2)]
    plt.title("Comparing of the model and the Binomial distribution")
    plt.ylabel("Probability")
    plt.xlabel("Outcomes")
    plt.hist(R,bins,histtype = "stepfilled", weights = P, color = "b",label = "Binominal")
    plt.hist(R,bins,histtype = "stepfilled",normed = True,weights = A,color = "r",alpha = 0.5,label = "Actual")
    plt.legend()


"""
In [259]: H(20,12,8)
Out[259]: 
[1.1e-05,
 0.000717,
 0.014647,
 0.097917,
 0.274273,
 0.352754,
 0.20567,
 0.050286,
 0.003726]
 
 In [260]: getH(20,12,8)
Out[260]: 
([0, 1, 2, 3, 4, 5, 6, 7, 8],
 [7.938398031277288e-06,
  0.0007620862110026197,
  0.01467015956180043,
  0.09780106374533619,
  0.27506549178375805,
  0.35208382948321026,
  0.205382233865206,
  0.050297689926172895,
  0.003929507025482257]
  
 """





