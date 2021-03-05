import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
from sympy.functions import *
import math


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

"""Funcion de taylor"""
def taylor(Func,c,n):
    i = 0
    Solu = 0
    while i <= n:
        Solu = Solu + (Func.diff(x,i).subs(x,c))/(factorial(i))*(x-c)**i
        i+=1
    return Solu

"""Funcion para el numero de cifras signficativas"""
def significativo(x, cifras=9):
    if x == 0 or not math.isfinite(x):
        return x
    cifras = cifras - math.ceil(math.log10(abs(x)))
    return round(x, cifras)


if __name__ == '__main__':

    x = sy.Symbol('x')
    
    f = exp(0.999999999) * cos(2*0.999999999)# Reemplazar por x=0.005, x= 0.0001, x= 0.999999999

    func = taylor(f,-1,1)
   # print(" f(x) = ",end="")
   # print(func)

    y = 1
    print("En el punto x =",y,":",significativo(func.subs(x,y),9))

    
    

