# -*- coding: utf-8 -*-
"""

#@author: AMT
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
    #print(Q)
    filtered = []
    xi = []
    for i in range(len(factors)):
        if Q[i] == 1:
            #print(i)
            filtered.append(factors[i])
            xi.append(i - m)
    print(filtered)
    if len(filtered) <= len(fb):
        print("m is too small")
        return factor(num, bound, 2 * m)
    else:
        for i in range(len(filtered)):
            tup = [(filtered[w], xi[w]) for w in range(len(xi))]
            tup = f.sample(tup[:i] + tup[(i + 1):], len(fb))
            try:
                #print(len([v[0] for v in tup]))
                #print(len([v[0] for v in tup][0]))
                #print(len(filtered[i]))
                y = f.sparse([v[0] for v in tup], filtered[i])
                x = f.array([v[0] for v in tup])
                #print(x.shape, y.shape)
                if f.array_equal(f.dot(x, y), filtered[i]):
                    prod = 1
                    qprod = f.array([0] * len(fb))
                    truexi = [v[1] for v in tup]
                    b = [v[0] for v in tup]
                    for i in range(len(truexi)):
                        prod *= (y[i][0] * truexi[i]) if y[i][0] else 1
                        qprod += y[i][0] * b[i]
                    qprod /= 2
                    iu = 1
                    print("Works")
                    for i in range(len(qprod)):
                        iu *= fb[i] ** qprod[i]
                    gcd1 = f.abs(f.gcd(iu - prod, num))
                    gcd2 = f.abs(f.gcd(iu + prod, num))
                    if gcd1 != 1:
                        result.extend(factor(gcd1, bound, m))
                        result.extend(factor(num / gcd1, bound, m))
                        return result
                    if gcd2 != 1:
                        result.extend(factor(gcd2, bound, m))
                        result.extend(factor(num / gcd2, bound, m))
                        return result
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(e)
                continue
    print("did not work, trying again")        
    factor(num, bound, 2 * m)