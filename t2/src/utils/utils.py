import time

"""
This function calls the received algorithm 'reps' times and calculate the
time to run.
"""
def generate(alg, reps):
    start = time.time()
    for _ in range(reps):
        alg.calculate()
    end = time.time()
    alg.time = (end-start)
    return alg.result, alg.time

