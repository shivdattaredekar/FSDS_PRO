import numpy as np
import pandas as pd


##Writing data 
def write_data(path, data):
    """Write the contents of the file"""
    with open(path,'w') as file:
        file.write(data)

##Reading data 
def read_data(path):
    """Read and return the contents of the file"""
    with open(path, 'r') as file:
        return file.read()

##Appending data 
def append_data(path, data):
    """Append the contents of the file"""
    with open(path,'a') as file:
        file.write(data)
