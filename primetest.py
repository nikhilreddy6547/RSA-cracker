import random

class RVal(object):
    def __init__(self, k, m):
        self.k = k
        self.m = m
def first(n):
    m = n - 1
    k = 0
    while m % 2 == 0:
        m = m // 2
        k += 1
    return RVal(k, m)
def primeQ(n, prob = 128):
    m = first(n).m
    k = first(n).k
    for i in range(prob):
        a = random.randrange(2, n - 2)
        b = pow(a, m, n)
        c = 1
        if b == 1 or b == n - 1:
            continue
        for g in range(k - 1):
            b = pow(b, 2, n)
            c *= 2
            if b == 1:
                return False
            if b == n - 1:
                break 
        else:
            return False
    return True