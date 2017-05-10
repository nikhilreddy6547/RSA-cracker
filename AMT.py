# -*- coding: utf-8 -*-
"""
Created on Sat May 06 16:02:39 2017

@author: Nikhil Reddy
"""
import factory as f

casework = [[], [], [2], [3], [2, 2]]
def factor(num, bound, m):
    result = []
    if(num < 5):
        result = casework[num]
        return result
    if(f.primeQ(num)):
        result.append(num)
        return result
    x = int(f.sqrt(num))
    if (x * x == num):
        result.extend(factor(x, bound, m))
        result.extend(factor(x, bound, m))
        return result
    fb = f.factorbase(num, bound) + [-1]
    interval = range(x - m, x + m + 1)
    Q = [i * i - num for i in interval]
    factors = [[0 for j in fb] for i in Q]
    for i in range(len(fb) - 1):
        for j in f.shanks(num, fb[i]):
            while j < len(Q):
                if (Q[j] % fb[i] == 0):
                    Q[j] = Q[j] / fb[i]
                    factors[j][i] = (factors[j][i] + 1) % 2
                else:
                    j = j + fb[i]
    j = 0
    while j < len(Q):
        if (Q[j] < 0):
            Q[j] = Q[j] / fb[-1]
            factors[j][-1] = (factors[j][-1] + 1) % 2
        else:
            j = j - fb[-1]
    print(Q)
    filtered = []
    for i in range(len(factors)):
        if Q[i] == 1:
            print(i)
            filtered.append(factors[i])
    print(filtered)
    if len(filtered) <= len(fb):
        print("m is too small")
        #return factor(num, bound, 2 * m)