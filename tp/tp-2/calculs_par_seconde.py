from time import time, sleep

def calculs(n):
    a, b = 60986.5150141834, 2831540.2372984355 # arbitraires
    for _ in range(n):
        c = a ** (-b)

K = 100_000
while True:
    t_i = time()
    calculs(int(K))
    sleep(1 - (time() - t_i))
