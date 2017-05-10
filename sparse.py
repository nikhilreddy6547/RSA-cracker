# -*- coding: utf-8 -*-

import numpy as np
import bm

def sparse(matrix, vector):
    matrix = np.array(matrix).T
    vector = np.array([vector]).T
    print(vector)
    func = matrix.dot
    n = len(matrix)
    powers = [vector]
    while len(powers) < 2 * n:
        powers.append(func(powers[-1]))
    powers = np.remainder(powers, 2)
    print(powers)
    k = 0
    g = np.poly1d([1])
    while g.order < n and k < n:
        u = [0] * n
        u[k] = 1
        u = np.array(u)
        print("g", g)
        products = [np.mod(np.dot(u, i), 2) for i in powers]
        values = g(products) % 2
        poly = bm.Berlekamp_Massey_algorithm(values)
        print(poly)
        l = list(poly)
        vec = [0] * (max(l) + 1)
        for i in l:
            vec[max(l) - i] = 1
        newPoly = np.poly1d(vec)
        print (newPoly.order)
        g *= newPoly
        g = np.remainder(g, 2)
        g = np.poly1d(g)
        print(g)
        print(g.order)
        print(g(matrix))
        k += 1
    x = [g(i + 1) * powers[i] % 2 for i in range(g.order)]
    print(x)
    x = -sum(x)
    x = np.array([i % 2 for i in x])
    return(x)