# -*- coding: utf-8 -*-
"""
Created on Sat May 06 21:02:25 2017

@author: Admin1
"""
def legendre(n, p):
    result = pow(n, (p - 1) / 2, p)
    if result == p - 1:
        return -1
    return result
def shanks(a, p):
    if a == 0:
        return [0]
    if p == 2:
        return [a % p]
    if legendre(a, p) != 1:
        return []
    if p % 4 == 3:
        x = pow(a, (p + 1)/4, p)
        return [x, p-x]
    q, s = p - 1, 0
    while q % 2 == 0:
        s += 1
        q //= 2
    z = 1
    while legendre(z, p) != -1:
        z += 1
    c = pow(z, q, p)
    x = pow(a, (q + 1)/2, p)
    t = pow(a, q, p)
    m = s
    while t != 1:
        i, e = 0, 2
        for i in xrange(1, m):
            if pow(t, e, p) == 1:
                break
            e *= 2
        b = pow(c, 2**(m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

    return [x, p-x]