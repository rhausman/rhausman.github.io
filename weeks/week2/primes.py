def primes(n):
    to_remove = []
    for i in range(2, int(n / 2)):
        # omit first occurance
        to_remove += list(range(i * 2, n + 1, i))
    to_remove = set(to_remove)
    return [i for i in list(range(2, n + 1)) if i not in to_remove]
