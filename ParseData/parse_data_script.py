# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:53:24 2019

@author: Dylan Souvage

"""
import re
import os
import glob

root_dir = '.'

file_counter = 1

#build file list for every file in the directory of the
#python script, loop through each file and turn output results
#into csvs
for directory, subdirectories, files in os.walk(root_dir):
    for curr_file in files:
        if ".stat" in curr_file:
            
            list_to_regex = []
            
            with open(curr_file, "r") as ifile:
                for line in ifile:
                    list_to_regex.append(line)
            	
            fitness = []
            
            counter = 0
            
            switcher = 0
            
            #first 13 lines are ECJ text output
            for line in list_to_regex:
                #ignore first 13 lines
                if counter > 13: 
                    #grab every other line ( fitness is every other line )
                    #only grab the last 19 characters of the string
                    #ensure numerical output or '.'
                    if switcher == 1:
                        switcher = 0
                    elif switcher == 0:
                        fitness.append(re.sub("[^1234567890.]", "", line[-19:]) + "\n")
                        switcher = 1
                counter = counter + 1
            
            counter = 0
            
            f= open("csv_out_"+str(file_counter)+".csv","w+")
            
            parameter = "Parameter " + str(file_counter)
            
            #f.write(parameter + "\n")
            
            f.flush()
            
            for fit in fitness:
                if counter >  5:
                    print("Generation " + str(counter-5))
                    print(fit)
                    
                    string_gen = str(counter-5) + ','
                    string_fit = str(fit)
                    
                    f.write(parameter + "," + string_gen + string_fit)
                    
                    f.flush()
    
                counter = counter + 1
                
            
            
            f.close
            
            file_counter = file_counter + 1


#concatenate everything into one big csv
for f in glob.glob("*.csv"):
    os.system("type *.csv > concat.csv")





