# https://en.wikipedia.org/wiki/Lehmer_random_number_generator
# aka Park-Miller

"""
taken from
https://en.wikipedia.org/wiki/Primitive_root_modulo_n#Table_of_primitive_roots
n = 47
primitive roots modulo n = 5, 10, 11, 13, 15, 19, 20, 22, 23, 26, 29, 30, 31, 33, 35, 38, 39, 40, **41**, 43, 44, 45
order = 46
"""

# primarily chosen by the author, not good enough
# _PRIMITIVE_ROOT = 41
# _MOD = 47


# Parameters in common use, according to wikipedia
_PRIMITIVE_ROOT = 48271
_MOD = 2147483647

""" Lehmer class (aka as Park-Miller)"""
class Lehmer:
    """ :returns Lehmer object
    :param seed - seed number
    :param size - number of bits
    :param a - element of high multiplicative order modulo m (e.g., a primitive root modulo n)
    :param m - a big prime number or power of prime number

    num is the generated number (initiated as seed)
    """
    def __init__(self, seed, size, a=_PRIMITIVE_ROOT, m=_MOD):
        self.seed = seed
        self.size = size
        self.m = m
        self.a = a
        self.num = seed
        self.time = 0
        self.result = ''

    """ :returns result from the formula
    X(k+1) = a * X(k) mod m
    """
    def algorithm(self):
        self.num = (self.a * self.num) % self.m
        return self.num

    """
    runs the algorithm (size - 1) times, each time it runs using 
    the last seed (saved in num), receives the result and appends
    the least significant digit to the result, creating
    a binary result of the desired size.
    It starts with 1 in the beginning (this will make sure
    that the number has 'size' bits)
    
    This method of making sure of the size is based in the implementation
    of Blum-Blum-Shub from Jeremy Kun
    https://jeremykun.com/2016/07/11/the-blum-blum-shub-pseudorandom-generator/
    """
    def calculate(self):
        result = "1"
        for _ in range(self.size - 1):
            rnd = self.algorithm()
            b = rnd % 2
            result += str(b)
        self.num = int(result, 2)
        self.result = result
        return result
