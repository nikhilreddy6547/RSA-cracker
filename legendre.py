# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:48:40 2017

@author: Admin1
"""
import primetest

def factorbase(n, bound):
    result = []
    for i in range(2, bound + 1):
        if i != 4 and (i == 2 or i == 3 or primetest.primeQ(i)):
            if pow(n, (i - 1) / 2, i) == 1:
                result.append(i)
    return result