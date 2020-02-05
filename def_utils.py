#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:02:42 2020
Defining utility functions for 'Eval_coon.py'
Uname: aetienne
github name: aetienne93 
@author: Aaron Etienne 
"""

import numpy as np

'''pull header elements from '2008Male0006.txt' file'''
def pullHead(cutLines):
	# remove white space from all elements 
    return [i.strip() for i in cutLines[0].split(",")], cutLines[-1], cutLines[1:-1]

'''determine list mean'''
def calcMean(coonInput):
	return np.mean(coonInput)

'''determine list cumulative sum'''
def cumSum(coonInput):
	return list(np.cumsum(coonInput))

'''determine euclidian distance between points'''
def euclidDist(A, B):
	return np.sqrt((A[0] - A[1])**2 + (B[0] - B[1])**2) 

'''determine coordinate distance'''
def cordDist(X, Y):
	dist = [0]
	for i in range(len(X)-1):
		dist.append(euclidDist( (X[i],X[i+1]) , (Y[i],Y[i+1]) ))
	return dist