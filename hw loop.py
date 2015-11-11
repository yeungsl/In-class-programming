# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:46:35 2015

@author: davidyeung
"""
import math
exec(open('lab05.py').read())
exec(open('lab06.py').read())

def problem3():
    r = 0
    for i in range(1,5):
        r += binomial(5,0.5,i)
        print(i)
    return r
    
def problem8():
    r = 0
    for i in range(5, 15):
        r += C(i-1, 4) * (1/2)**(i-5) * (1/2)**(5)
        print(r)
    return r
    
def Nphi(e, u, x):
    return (0.5 *(1 + math.erf((x - e)/(math.sqrt(u) * math.sqrt(2)))))
    
def Ephi(lamb, t):
    return(1- (math.e**(-1 * lamb * t)))
