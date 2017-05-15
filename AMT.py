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
    print(fb)
    print(Q)
    factors = [[0 for j in fb] for i in Q]
    for i in range(len(fb) - 1):
        for j in f.shanks(num, fb[i]):
            j = (j - x + m) % fb[i]
            while j < len(Q):
                if (Q[j] % fb[i] == 0):
                    Q[j] = Q[j] / fb[i]
                    factors[j][i] += 1
                else:
                    j = j + fb[i]
    for j in range(len(Q)):
        if (Q[j] < 0):
            Q[j] = Q[j] / fb[-1]
            factors[j][-1] += 1
    factorsBin = [[j % 2 for j in i] for i in factors]
    filteredFactors = []
    filtered = []
    xi = []
    for i in range(len(factorsBin)):
        if Q[i] == 1:
            #print(i)
            filtered.append(factorsBin[i])
            filteredFactors.append(factors[i])
            xi.append(i - m + x)
    print(filtered)
    it = 0
    while(it < len(fb)):
        numb = 0
        for i in range(len(filtered)):
            numb += filtered[i][it]
        if numb == 0:
            for i in range(len(filtered)):
                del filteredFactors[i][it]
                del filtered[i][it]
            del fb[it]
        else:
            it += 1
    it = 0
    while(it < len(filtered)):
        if f.sum(filtered[it]) == 0:
            del filteredFactors[it]
            del filtered[it]
            del xi[it]
        else:
            it += 1
    print(filtered)
    if len(filtered) <= len(fb):
        print("m is too small")
        #return factor(num, bound, 2 * m)
    else:
        for i in range(len(filtered)):
            largeMatrix = [(filtered[j], xi[j], filteredFactors[j]) for j in range(len(xi))]
            tup = f.sample(largeMatrix[:i] + largeMatrix[(i + 1):], len(fb))
            try:
                matrix = f.array([j[0] for j in tup]).T
                vector = f.array([filtered[i]]).T
                sparse = f.sparse(matrix, vector)
                print(matrix, sparse, vector)
                if f.array_equal(f.dot(matrix, sparse) % 2, vector):
                    prod = 1
                    print("Works")
                    print(tup)
                    qprod = f.array([0] * len(fb))
                    print([j[1] for j in tup])
                    for j in range(len(tup)):
                        prod *= tup[j][1] if sparse[j][0] else 1
                        prod %= num
                        qprod += sparse[j][0] * f.array(tup[j][2])
                    qprod += f.array(largeMatrix[i][2])
                    prod *= largeMatrix[i][1]
                    prod %= num
                    print(prod, qprod)
                    qprod /= 2
                    iu = 1
                    for j in range(len(qprod)):
                        iu *= fb[j] ** qprod[j]
                        iu %= num
                    print(iu)
                    assert((prod * prod - iu * iu) % num == 0)
                    print("yo what")
                    gcd1 = int(abs(f.gcd(iu - prod, num)))
                    gcd2 = int(abs(f.gcd(iu + prod, num)))
                    if gcd1 != 1 and gcd1 != num:
                        print("I found something", gcd1)
                        result.extend(factor(gcd1, bound, m))
                        result.extend(factor(num / gcd1, bound, m))
                        return result
                    if gcd2 != 1 and gcd2 != num:
                        print("I found something", gcd2)
                        result.extend(factor(gcd2, bound, m))
                        result.extend(factor(num / gcd2, bound, m))
                        return result
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(e)
                continue
        print("did not work, trying again")        
        return factor(num, bound, m)