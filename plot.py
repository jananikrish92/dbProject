#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 09:09:16 2017

@author: bhuvana
"""
import matplotlib.pyplot as plt

def LineGraph():
    cvvalues =[0.07352146220938077, 0.7365495524443777, 0.07352146220938077, 1.1749196420074441, 0.21785902950678723]
    #trvalues=[0.07352146220938077, 0.7365495524443777, 0.07352146220938077, 1.1749196420074441, 0.21785902950678723]
    lab=range(1,6)
    ticks= ['Nobel laureates from 1900-1909', 'names and origin information of Nobel laureates', 'Nobel laureates from 1910-1919', 'Employee information', 'names and category information of Nobel laureates']
    
    labels =["Scores"]

    #Plot a line graph
    plt.figure(10, figsize=(15, 8))  #6x4 is the aspect ratio for the plot
    #plt.plot(inds,cvvalues,'or-', linewidth=3) #Plot the first series in red with circle marker
    plt.plot(lab,cvvalues,'sb-', linewidth=3) #Plot the first series in blue with square marker

    #This plots the data
    plt.grid(True) #Turn the grid on
    plt.ylabel("Score") #Y-axis label
    #plt.xlabel("Table Names") #X-axis label
    plt.title("Entity Complement Scoring") #Plot title
    plt.xticks(lab, ticks)
    #set x axis range
    plt.ylim(-0.1, 1.3) #Set yaxis range
    plt.legend(labels,loc="best")

    #Make sure labels and titles are inside plot area
    plt.tight_layout()

    #Save the chart
    plt.savefig("/Users/bhuvana/Documents/DB/LinePlot.pdf")

    #Displays the plots.
    #You must close the plot window for the code following each show()
    #to continue to run
    plt.show()
    return
    
LineGraph()