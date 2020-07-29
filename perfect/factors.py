from numpy import sum

def factorization(n):
    def fac_rec(i, factors=[], limit=n):
        if i >= limit:
            return factors
        elif n%i == 0:
            return fac_rec(i+1, factors + [i, int(n/i)], n/i)
        else:
            return fac_rec(i+1, factors, n/i)
    return fac_rec(1)

def aliquot_sum(n):
    return sum(factorization(n)) - n
