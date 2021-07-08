import time
import csv
import random

from primes.fermat import fermat
from PRNG.lehmer import Lehmer

_REPS = 100
_BITS = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]


def main():
    print('starting generating prime numbers')
    txtf = open('generated_primes.txt', 'w+')
    csvf = open('generated_primes.csv', 'w+', newline='')
    wcsvf = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for size in _BITS:
        _SEED = int(time.time())
        print('prime of size ', size, 'bits')
        rounds = 0
        isPrime = False
        start = time.time()
        while not isPrime:
            _SEED = random.randint(0, int(time.time()))
            rounds += 1
            leh = Lehmer(_SEED, size)
            leh.calculate()
            isPrime = fermat(leh.num)
            if rounds % 10000 == 0:
                print('...')
        total = time.time() - start
        print('it took ', rounds,' rounds and ',total,'s to find a prime number of size ', size)
        print('number generated:')
        print(leh.num)

        txtf.write('--------------------------------------------------\n')
        size_txt = 'size: ' + str(size)+' bits\n'
        time_txt = 'time: ' + str(total)+'s\n'
        rounds_txt = 'rounds: ' + str(rounds)+'\n'
        gen_txt = 'generated: ' + str(leh.num)+'\n'
        txtf.write(size_txt)
        txtf.write(time_txt)
        txtf.write(rounds_txt)
        txtf.write(gen_txt)

        wcsvf.writerow(['--------', '--------'])
        wcsvf.writerow(["size (bits)", size])
        wcsvf.writerow(["time (s)", total])
        wcsvf.writerow(["rounds", rounds])

    txtf.close()
    csvf.close()


if __name__ == "__main__":
    main()