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

# read description in encrypt.py
# try using the wrong key - it won't work!
def decrypt_string(s, key=SECRET_KEY):
    random.seed(key)
    return "".join([chr(ord(c) - random.randint(0, 100)) for c in s])


with open(path[:-4] + "_decrypted", "w+") as ff:
    ff.write(decrypt_string(string))
    ff.close()

print("decrypted")