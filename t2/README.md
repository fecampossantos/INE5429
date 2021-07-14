Assignment of pseudo-random number generation and prime-checking, for Computer Security course in Universidade Federal de Santa Catarina (UFSC).

For PRNG, I chose Lehmer's (aka Park-Miller's) and Blum Blum Shub's algorithms
For the prime-checking I chose Fermat's and Miller-Rabin's method.

To run the program on your computer, clone the repository, access the location via your terminal and enter the src folder

to test and generate pseudo-random numbers:
``````
py prgn_test.py
``````
this will create 3 files on your folder:
- blumBlumShub.txt has all the PR numbers created for each defined size using BlumBlumShub's algorithm
- parkMiller.txt has all the PR numbers created for each defined size using Park-Miller's algorithm
- results.csv has the time needed to generate those numbers

to test the prime-checking methods:
``````
py primes_test.py
``````
This test consists on checking prime and non-prime numbers, calculating the time for each one of them.

this will create 2 files on your folder:
- fermat_results.csv and miller_rabin_results.csv, with the times needed to check prime and non-prime numbers of different sizes.

to run the whole project (create pseudo-random numbers and test if they are prime):
``````
py generate_primes.py
``````
this will create 2 files on yout folder:
- generated_primes.csv with the times needed to generate PR prime numbers
- generated_primes.txt with the PR prime numbers generated


