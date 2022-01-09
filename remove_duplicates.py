"""
Created on Mon May 03 10:56:39 2021

@author: christoarmani
"""
import os

directory = r'add filepath here'
folders = os.listdir(directory)

for name in folders:
    for i in range(100):
        if "(" + str(i) + ")" in name:
            os.remove(directory + "/" + name)