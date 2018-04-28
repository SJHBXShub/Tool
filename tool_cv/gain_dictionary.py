# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:50:06 2018

@author: jieyang
"""
import os
import time
import re
num_string = {}
f = open(r'./tr.txt',"r")  
line = f.readline()
dictionary = ''  
normal_dic = ' "!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]_`abcdefghijklmnopqrstuvwxyz~'
i = 0
while line:  
    i = i + 1
    contant_line = str(line)
    string_line = contant_line.split(',')[1]
    if string_line[0] == '|':
        string_line = contant_line.split('|')[1]
    if contant_line.split(',')[0] == "1177212":
        print("I am sentance:",string_line)
    for em in string_line:
        if em not in normal_dic:
            if i == 1:
                normal_dic = normal_dic + em
        if em in dictionary:
            continue
        else:
       	    dictionary = dictionary + em
    line = f.readline()  
f.close()
dictionary = "".join((lambda x:(x.sort(),x)[1])(list(dictionary)))
print(dictionary)
