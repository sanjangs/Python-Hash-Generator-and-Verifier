from hashlib import sha512
import sys

if len(sys.argv) != 2:
    print('Usage: python sha512sum.py [file]')
    exit()

filename = sys.argv[1]

try:
    file = open(filename, 'rb')
    contents = file.read()
    file.close()
except FileNotFoundError:
    print('Error: File not found.')
    exit()

print(sha512(contents).hexdigest().lower())
