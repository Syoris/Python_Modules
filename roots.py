# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:05:27 2018

@author: charl
"""
import math


def quadroots(a,b,c,show = False):
    d = b**2-4*a*c # discriminant

    if d < 0:
        if show:
            print ("This equation has no real solution")
        return (0,0,False)
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        if(show):
            print ("This equation has one solutions: "), x
        return (x,x,True)
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        if show:
            print ("This equation has two solutions: ", x1, " or", x2)
        return (x1,x2,True)
    
