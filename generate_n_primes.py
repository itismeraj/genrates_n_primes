#!/usr/bin/python

def generate_n_primes(N):
    primes  = []
    checkthis = 2
    while len(primes) < N:
        ptest    = [checkthis for i in primes if checkthis%i == 0]
        primes  += [] if ptest else [checkthis]
        checkthis += 1
    return primes


if __name__ == "__main__":
    val = int(input("Enter Number: "))    
    print(generate_n_primes(val))
