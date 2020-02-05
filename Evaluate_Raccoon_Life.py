#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:31:14 2020
This script was created to read in data from the '2008male0006.txt' file, store data elements in a dictionary, convert elemenets to 
correct data type, and compute average, sum, euclidean distance between coordiante points of fictional raccoon 'George'
uname: aetienne 
github name: aetienne93 
@author: Aaron Etienne
"""


"""Libraries have been imported using utility function script"""

"""import utility function"""
import def_utils as dut



def readIn(coon08):
    """
    Read in file- coon 
    Coon08 calls the name of the file to be read
    use function to split end of line character 
    """

    coon = open(coon08,"r") 
    cutLines= coon.read().splitlines() 
    """this removes end of line characters"""
    coon.close() 
    return cutLines

def catHead(coon08):
    """define the header block categories"""  
    coon = open(coon08,"w")
    coon.write("Raccoon name: {0}\n".format(name))
    coon.write("Average location: {0:.2f}, {1:.2f}\n".format(avg_X, avg_Y))
    coon.write("Distance traveled: {0:.2f}\n".format(total_dist))
    coon.write("Average energy level: {0:.2f}\n".format(avg_energy))
    coon.write("Raccoon end state: {0}\n\n".format(last_line))
    coon.close() 
    
    
    """ the next step is to write the data to a new file""" 
    

def createFile(coon08, cutLines):
    """create file in which data is written to specififed format 
    coon08: takes over name of the new coon data file
    """
    
    coon = open(coon08,"a") 
    
    coon.write("Date,Time,X,Y,Asleep,Behavior Mode,Distance\n")
    for i in range(len(cutLines["Day"])):
        coon.write("{0},{1},{2},{3},{4},{5},{6}\n".format(cutLines["Day"][i],
                   cutLines["Time"][i],cutLines["X"][i],cutLines["Y"][i],
                   cutLines["Asleep"][i],cutLines["Behavior Mode"][i],cutLines["Distance"][i]))
    coon.close() 

def cnumType(coonInput):
    """Convert datatype of each element
    in coonInput, the input list file 
    
    cnumType: specify correct number types 
    """

    numType = [int, float, complex, str]
    for i in numType:
        try:
            return i(coonInput) 
        except ValueError:
            pass

def dictList(cutLines, keyWord):
    """ use a keyword to deinfe data dictionary
    cutLines: list of lines
    keys: keys from dictionary
    """

    dataDict = {} 
    """This initiates an empty string"""
    for i, keyWord in enumerate(keyWord):
        indCol = [j.split(",")[i] for j in cutLines]
        """This reads each individual column"""
        dataDict[keyWord] = [cnumType(x) for x in indCol]   
        """change the data type wrt each element"""
    return dataDict 


"""Raccoon data file (Input) needs to be read in"""
cutLines = readIn("2008Male00006.txt")
header, last_line, cutLines = y=dut.pullHead(cutLines)

"""This makes a data dictionary for the input file"""
cutLines = dictList(cutLines, header)
cutLines["Distance"] = dut.cumSum(dut.cordDist(cutLines["X"], cutLines["Y"]))

"""This creates the header column"""
name = last_line.split()[0]
avg_energy = dut.calcMean(cutLines["Energy Level"])
avg_X = dut.calcMean(cutLines["X"])
avg_Y = dut.calcMean(cutLines["Y"])
total_dist = cutLines["Distance"][-1]
catHead('Georges_life.txt')

"""This creates Geroge's life file from the cutLines in dataDict"""
createFile('Georges_life.txt', cutLines)

        