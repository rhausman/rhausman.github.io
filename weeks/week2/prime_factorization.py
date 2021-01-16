from primes import primes


def prime_factorization(n):
    pri = primes(int(n / 2))
    if len(pri) == 0:
        return [n]  # base case - if there are no primes less than the number
    i = 0
    for p in pri:
        if n % p == 0:
            # if divisible, recursively find the factorization
            return [p] + prime_factorization(int(n / p))
    # if no primes fit the bill, another base case - this number is prime
    return [n]