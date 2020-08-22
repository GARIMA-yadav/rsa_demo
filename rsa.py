from sys import stderr
from math import gcd
import random
import time

MIN_VALUE = 1000
MAX_VALUE = 10000
MIN_ENCRYPTION_KEY = 3

primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 61, 73]

def is_odd(num):
    if (num % 2 == 0):
        return False
    else:
        return True

def get_k(num):
    counter = 0
    while (num % 2 == 0):
        counter += 1
        num = num // 2
    return counter, num

def is_prime(num):
    # finding out 'k' and 'm'
    k, m = get_k(num - 1)

    for a in primes_list:
        b = (a**m) % num
        if b == 1 or b == (num - 1):
            continue
        for i in range(1,k):
            b = (b**2) % num
            if b == (num - 1):
                break
        if b != (num - 1):
            return False
    return True


def get_prime():
    # randomizer
    while True:
        #epoch_time = int(time.time())
        #random.seed(10007)
        random_num = random.randrange(MIN_VALUE, MAX_VALUE)

        if is_odd(random_num):
            if is_prime(random_num):
                return random_num
            else:
                continue
        else:
            continue

def get_coprime(num):
    i = MIN_ENCRYPTION_KEY
    while (i < num):
        if gcd(num, i) == 1:
            return i
        i += 1
    stderr.write("error finding co-prime\n")

def get_decryption_key(e, totient):
    i = 1
    while ((totient * i + 1) % e):
        i += 1
        print(i)
    return ((totient * i + 1) // e)

def encrypt(data, e, n):
    cipher = ((data ** e) % n)
    return cipher

def decrypt(cipher, d, n):
    data = ((cipher ** d) % n)
    return data

p = get_prime()
q = get_prime()
n = p * q
phi_n = ((p - 1) * (q - 1))
e = get_coprime(phi_n)

message = int(input("Enter the data: "))

# encrypt
cipher = encrypt(message, e, n)

# decrypt
d = get_decryption_key(e, phi_n)
data = decrypt(cipher, d, n)

print(cipher, p, q, e, data)
