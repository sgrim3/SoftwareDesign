# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: Susie Grimshaw
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import math

def build_random_function(min_depth, max_depth):
    ''' Generates a nested function
    
    min_depth= specifies the minimum amount of nesting for the function
    max_depth = specifies the maximum amount of nesting for the function
    
    '''
    
    if max_depth ==0:
        xory=randint (1,2)
        if xory ==1:
            return (['x'])
        else: return (['y'])
    if min_depth <= 0:
        gen = randint (1,7)
        if gen ==1:
            return ['prod', build_random_function (min_depth-1,max_depth-1), build_random_function (min_depth-1,max_depth-1)]
        elif gen ==2:
            return ['sin_pi', build_random_function (min_depth-1,max_depth-1)]
        elif gen ==3:
            return ['cos_pi', build_random_function (min_depth-1,max_depth-1)]
        elif gen ==4:
            return ['x']
        elif gen ==5:
            return ['y']
        elif gen==6:
            return ['average',build_random_function (min_depth-1,max_depth-1),build_random_function (min_depth-1,max_depth-1)]
        elif gen==7:
            return ['x3',build_random_function (min_depth-1,max_depth-1)]
    else: 
        gen = randint (1,5)
        if gen ==1:
            return ['prod', build_random_function (min_depth-1,max_depth-1), build_random_function (min_depth-1,max_depth-1)]
        elif gen ==2:
            return ['sin_pi', build_random_function (min_depth-1,max_depth-1)]
        elif gen ==3:
            return ['cos_pi', build_random_function (min_depth-1,max_depth-1)]
        elif gen==4:
            return ['average',build_random_function (min_depth-1,max_depth-1),build_random_function (min_depth-1,max_depth-1)]
        elif gen==5:
            return ['x3',build_random_function (min_depth-1,max_depth-1)]

        
#==============================================================================
# if __name__=='__main__':
#     print build_random_function (2,5)
#==============================================================================

def evaluate_random_function(f, x, y):
    ''' Evaluates the randomly generated function generated in build_random_function
     f=function to be evaluated
     x = value of x
     y=value of y
    '''
    if f[0]=='sin_pi':
        return (math.sin (math.pi * evaluate_random_function (f[1],x,y)))
    elif f[0]=='cos_pi':
        return (math.cos (math.pi * evaluate_random_function (f[1],x,y)))
    elif f[0]=='x':
        return (x)
    elif f[0]=='y':
        return y
    elif f[0]=='prod':
        return (evaluate_random_function (f[1],x,y)*evaluate_random_function (f[2],x,y))
    elif f[0]=='average':
        return ((evaluate_random_function (f[1],x,y))+(evaluate_random_function (f[1],x,y)))/2
    elif f[0]=='x3':
        return (evaluate_random_function (f[1],x,y))**3
    
#==============================================================================
# if __name__=='__main__':
#     print evaluate_random_function (build_random_function (2,5),2,3)
#     
#==============================================================================
     
     


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        val= value to be mapped
        input_interval_start = beginning of the original interval
        input_interval_end = end of the original interval
        output_interval_start = beginning of the desired interval
        output_interval_end = end of the desired interval
    """
    
    inputRange = input_interval_end - input_interval_start
    outputRange = output_interval_end - output_interval_start
    mappedVal = (((val - input_interval_start)*outputRange)/inputRange)+output_interval_start
    return(mappedVal)
        
    
def generate_picture (filename):
    '''Generates an image from the randomly generated equation
    
    filename=name of file (should end in .jpg)
    
    '''
    
    red=build_random_function (5,10)
    blue = build_random_function (10,12)
    green = build_random_function (8,10)
    
    im = Image.new('RGB',(1000,600))
    pixels = im.load()
    
    for x in range (0,999):
        new_x=float (remap_interval (x,0.,999.,-1.,1.))
        for y in range (0,599):
            new_y= float(remap_interval (y,0.,599.,-1.,1.))
            
            
            Red=evaluate_random_function (red,new_x,new_y)
            Blue=evaluate_random_function (blue,new_x,new_y)
            Green=evaluate_random_function (green,new_x,new_y)
            
            R=remap_interval (Red,-1,1,0,255)
            B=remap_interval (Blue,-1,1,0,255)
            G=remap_interval (Green,-1,1,0,255)
            
            pixels[x,y] = (int(R),int(G),int (B))
            
    im.save(filename)
    im.show ()
    
if __name__ == '__main__':
    generate_picture('image.jpg')