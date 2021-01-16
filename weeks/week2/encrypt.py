import sys
import random

args = sys.argv[1:]

if len(args) == 0:
    print("Please provide a path and (optionally) a secret key!")
    sys.exit(1)
else:
    path = sys.argv[1]  # pass in the path as a command line arg
    ff = open(path, "r")
    string = ff.read()
    ff.close()

SECRET_KEY = 20

if len(args) > 1:
    SECRET_KEY = args[-1]

# we will use a simple encryption scheme: add a random number to each char
# decrpytion requires knowing the "secret key", which is in this case used as
# the seed for the random generator
# ord(s) => numeric code for char s,
# chr(n) => char corresponding to number n. It's either utf-8 or ASCII
# this will fail if we try to encrypt a string that is one of the last unicode chars,
# but it's easy to fix this by using modulo
def encrypt_string(s, key=SECRET_KEY):
    random.seed(key)
    return "".join([chr(ord(c) + random.randint(0, 100)) for c in s])


with open(path + "_enc", "w+") as ff:
    ff.write(encrypt_string(string))
    ff.close()

print("encrypted")
