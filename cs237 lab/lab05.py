# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:25:04 2015

@author: Sailung Yeung
email: yeungls@bu.edu
"""
import pandas as pd
import matplotlib.pyplot as plt
labD = "/Users/davidyeung/Desktop/"

##Problem one
def E(X):
    (R,P) = X
    ls = []
    
    for j in range(len(R)):
        ls += [R[j] * P[j]]
    return sum(ls)

def Var(X):
    (R,P) = X
    ls = [(x - E(X))**2 for x in R]
    r = (ls, P)
    return E(r)
    
def stdev(X):
    return Var(X)**(0.5)

"""
result:
In [22]: X = ( [1, 3, 5, 7, 10], [0.23, 0.36, 0.09, 0.17, 0.15] )

In [23]: E(X)
Out[23]: 4.45

In [24]: Var(X)
Out[24]: 9.247499999999999

In [25]: stdev(X)
Out[25]: 3.040970239906993
"""

##Problem two
##(a)
def binomial(n,p,k):
    P = (p**k) * ((1-p)**(n-k)) * C(n,k)
    return P
    
    
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
    
"""
result for (a):

In [31]: binomial(10, 0.5, 5)
Out[31]: 0.24609375

In [32]: binomial(45, 0.3, 8)
Out[32]: 0.02625137057973889
"""
##(b)
def getBinomial(n,p):
    lsr = []
    lsp = []
    for i in range(n+1):
        lsp += [binomial(n,p,i)]
        lsr += [i]
    X = (lsr,lsp)
    return X
    
def drawBinomial(n,p):
    (R,P) = getBinomial(n,p)
    title = "B" + "(" + str(n) + "," + str(p)+ ")" + "PMF"
    drawDistribution(R,P, title)
    
    
def drawDistribution(X,P,title):
    bins = [x - 0.5 for x in range(min(X),max(X)+2)]
    plt.title(title)
    plt.title(title)
    plt.ylabel("Probabiltiy")
    plt.xlabel("Outcomes")
    plt.hist(X,bins, normed = True, weights = P)
    plt.show()
    
    
    
    
##Problem Three

    
def prob3():
    ##getting a datafram based on the data
    stud = pd.read_csv(labD + "gender.csv")
    
    ##Convert the (single column) dataframe into a list
    ls = stud['NumFemales'].tolist()
    
    ##getting the p for an arbitrary student to be a female student
    p = sum(ls)/ 5980
    
    ##getting the P for B(10,p)    
    (R,P) = getBinomial(10,p)    
    
    
    ##getting the binomial distribution B(10,p)
    
    bins = [r - 0.5 for r in range(min(R),max(R)+2)]
    plt.title("Comparing of the model and the Binomial distribution")
    plt.ylabel("Probability")
    plt.xlabel("Outcomes")
    plt.hist(R,bins,histtype = "stepfilled", weights = P, color = "b",label = "Binominal")
    stud["NumFemales"].hist(bins = bins,histtype = "stepfilled",normed = True,color = "r",alpha = 0.5,label = "Actual")
    plt.legend()
    
    
    
    
    
    
    
    
    
    
    