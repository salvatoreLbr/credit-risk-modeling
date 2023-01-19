import math as mt

def get_binomial_coefficient(N: int, k: int) -> int:
    return mt.factorial(N)/(mt.factorial(N-k)*mt.factorial(k))
