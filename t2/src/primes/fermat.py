import random
# https://en.wikipedia.org/wiki/Fermat_primality_test

""" :returns true if n is probably prime, false otherwise
:param n -> number to be tested
:param k -> number of repetitions to be made (more repetitions = more accuracy)
"""
def fermat(n, k=100):
    #  if number is 1,2 or 3, is prime
    if n <= 3:
        return True

    # if number is even, is not prime
    if n % 2 == 0:
        return False

    # Now, following wikipedia's pseudocode:

    # Repeat k times:
    for _ in range(k):
    # Pick 'a' randomly in the range[2, n − 2]
        a = random.randrange(2, n - 2)
    # If a^(n - 1) % n != 1, then return 'composite'
        if pow(a, n - 1, n) != 1:
            return False
    # If composite is never returned, return 'probably prime'
    return True