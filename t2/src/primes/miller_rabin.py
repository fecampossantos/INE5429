# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

import random

""" :returns true if n is prime, false otherwise
:param n -> number to be tested
:param k -> number of repetitions to be made (more repetitions = more accuracy)
"""
def miller_rabin(n, k=100):
    #  if number is 1,2 or 3, is prime
    if n <= 3:
        return True

    # if number is even, is not prime
    if n % 2 == 0:
        return False

    # Now, following wikipedia's pseudocode:

    # Write n as 2^r·d + 1 with d odd (by factoring out powers of 2 from n − 1)
    r,d = 0, n-1
    while d % 2 == 0:
        r += 1
        d //= 2
    # WitnessLoop: repeat k times:
    for _ in range(k):
        # Pick a random integer a in the range [2, n − 2]
        a = random.randrange(2, n - 2)
        # x ← a^d mod n
        x = pow(a, d, n)
        # if x = 1 or x = n − 1 then continue WitnessLoop
        if x == 1 or x == n-1:
            continue
        # repeat r − 1 times:
        for _ in range(r - 1):
            # x = x^2 mod n
            x = pow(x, 2, n)
            # if x = n − 1 then continue WitnessLoop
            if x == n - 1:
                # goes back to WitnessLoop
                break
        else:
            return False
    return True

