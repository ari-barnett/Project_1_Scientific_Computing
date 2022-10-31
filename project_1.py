import numpy as np

def function(x):
    return 1 / (1 + x**2) #Definition of Function to be interpolated

def xnj(n):
    line_space = np.arange(0,n,1) #Returns line space of n_points for evaluations 
    return -1 + (2*line_space / line_space[-1]) #Returns array of xnj points for evaluation in f(x)

def ynj(n):
    line_space = np.arange(0,n,1) #Returns line space of n_points for evaluations 
    return np.cos((((2*line_space) + 1) / ((2*line_space[-1]) + 2))*np.pi) #Returns array of ynj points for evaluation in f(x)

