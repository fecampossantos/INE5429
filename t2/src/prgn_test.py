import csv
import time

from PRNG.blumblum import BBS
from PRNG.lehmer import Lehmer
from utils.utils import generate

_REPS = 100
_BITS = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

_SEED = int(time.time())

_RESULTS_BBS = []
_RESULTS_LEH = []



def main():

    for size in _BITS:
        bbs = BBS(_SEED, size)
        rst,time = generate(bbs, _REPS)
        _RESULTS_BBS.append(bbs)

        leh = Lehmer(_SEED, size)
        rst, time = generate(leh, _REPS)
        _RESULTS_LEH.append(leh)

    csv_file = open('results.csv', 'w+', newline='')
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    txt_file = open('blumBlumShub.txt', 'w+')
    writer.writerow(['Blum Blum Shub'])
    for bbs in _RESULTS_BBS:
        writer.writerow([bbs.size, bbs.time])
        txt_file.write(str(bbs.size) + "\n")
        txt_file.write(bbs.result + "\n\n")


    txt_file.close()

    txt_file = open('parkMiller.txt', 'w+')
    writer.writerow(['Park-Miller'])
    for leh in _RESULTS_LEH:
        writer.writerow([leh.size, leh.time])
        txt_file.write(str(leh.size) + "\n")
        txt_file.write(leh.result + "\n\n")

    txt_file.close()

    csv_file.close()

if __name__ == '__main__':
    main()

