from hashlib import sha256
import sys

if len(sys.argv) != 2:
    print('Usage: python sha256sum.py [file]')
    exit()

filename = sys.argv[1]

try:
    file = open(filename, 'rb')
    contents = file.read()
    file.close()
except FileNotFoundError:
    print('Error: File not found.')
    exit()

print(sha256(contents).hexdigest().lower())
