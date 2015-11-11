# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:55:39 2015

@author: Sailung Yeung
email:yeungsl@bu.edu
"""
import pandas as pd
import matplotlib.pyplot as plt
labD = "/Users/davidyeung/Desktop/"

##problem one

def Prob01():
    ##getting a datafram based on the data frist
    stud = pd.read_csv(labD + "studentdata.csv")
    
    ##1.print out the mean GPA for men.
    men = stud[stud["Gender"] == "M"]
    print(men["GPA"].mean())
    
    ##2.print out the mean GPA for seniors(U4)
    senior = stud[stud["ClassYear"] == "U4"]
    print(senior["GPA"].mean())
    
    ##3.Print out the 10 individuals with the largest number of credits earned, sorted in descending order by GPA;
    cred = stud.sort("CreditsEarned", ascending = False)[:10]
    print(cred.sort("GPA", ascending = False))
    
    ##4.Display a histogram of the GPA of all individuals, with bins for each letter grade, i.e., 0.0, 1.0, 2.0, 2.33, 2.67, 3.0, 3.33, 3.67, and 4.0.
    stud["GPA"].hist(bins = [0.0,1.0,2.0,2.33,2.67,3.0,3.33,3.67,4.0])
    
    

##problem two

def Prob02():
    ##getting a datafram based on the data
    stud = pd.read_csv(labD + "biometricdata.csv")
    
    ##1.Print out the maximum, minimum, mean, and (unbiased) standard deviation (all functions listed above) for the heights of all individuals
    print(stud["Height"].max())
    print(stud["Height"].min())
    print(stud["Height"].mean())
    print(stud["Height"].std())
    
    ##2.Print out the mean height for all individuals weighing more than 130 pounds;
    weight = stud[stud["Weight"] > 130]
    print(weight["Height"].mean())
    
    ##3.Print out how many individuals have a height >= 65 inches and <= 70 inches;
    cond = stud[(stud["Height"] >= 65) & (stud["Height"] <= 70)]
    print(cond["Height"].count())
    
    ##4.Display a histogram of the heights of all individuals from the minimum to the maximum, where each bin represents 1 inch.
    height = stud["Height"]
    #setting up bins
    bins = [x for x in range(int(min(height)),int(max(height)+4))]
    #setting up the figure size
    plt.figure(figsize = (8,7))
    #print the historgram
    height.hist(bins = bins)
    
    
    