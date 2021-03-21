import pandas as pd
import numpy as numy
import random
import scrapeasy

class fibb:
 def __init__(fib,n):
    fib.a,fib.b = 0,1
    while fib.a< n:
        print(fib.a, end= ' ')
        fib.a, fib.b = fib.b, fib.a +fib.b
    print()
 
 
 def fib2(fib,n):
	result = []
	fib.a,fib.b = 0,1
	while fib.a<n:
		result.append(fib.a)
		fib.a,fib.b = fib.b, fib.a+fib.b
	return result
