# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:34:43 2022

@author: Hritik
"""
import os
import sys
user_input = "C:\\Users\\prati\\Downloads\\LogProcessing\\SAMPLEWork\\A2DP"
directory = os.listdir(user_input)
searchString = "Final Verdict:INCONC"

for fname in directory: #change directory as needed
    if searchString in fname:
        f = open(fname,'r')
        print('found string in file %s') %fname
    else:
        print('string not found')