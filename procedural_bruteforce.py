import hashlib
from string import ascii_lowercase
import itertools
import time

#incremental brute force attack

def brute_force_attack():
    #hash of the password
    hash = "453e41d218e071ccfb2d1c99ce23906a"
    #alphabet used to generate the password
    alphabet = ascii_lowercase
    #length of the password
    length = 1
    #generate all the possible passwords
    while True:
        for guess in itertools.product(alphabet, repeat=length):
            guess = ''.join(guess)
            if hashlib.md5(guess.encode('utf-8')).hexdigest() == hash:
                return guess
            #print(guess)
        length += 1


def main():
    start = time.time()
    print("STARTING...")
    print("Correct password: " + brute_force_attack())
    end = time.time()
    print("Time: " + str(end - start))
main()
