from hashlib import md5, sha1, sha256, sha512
import sys

def check(bool):
    if bool:
        print('Status: OK')
    else:
        print('Error: Hashes Mismatched')

if len(sys.argv) != 3:
    print('Usage: python verify.py [file] [hash]')
    exit()

filename = sys.argv[1]
hash = sys.argv[2].lower()

try:
    file = open(filename, 'rb')
    contents = file.read()
    file.close()
except FileNotFoundError:
    print('Error: File Not Found.')
    exit()

hl = len(hash)

if hl == 32:    # md5
    check(md5(contents).hexdigest().lower() == hash)
elif hl == 40:  # sha1
    check(sha1(contents).hexdigest().lower() == hash)
elif hl == 64:  # sha256
    check(sha256(contents).hexdigest().lower() == hash)
elif hl == 128: # sha512
    check(sha512(contents).hexdigest().lower() == hash)
else:
    print('Error: Unknown hash function.')
