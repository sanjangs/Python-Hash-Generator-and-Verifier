from hashlib import sha1
import sys

if len(sys.argv) != 2:
    print('Usage: python sha1sum.py [file]')
    exit()

filename = sys.argv[1]

try:
    file = open(filename, 'rb')
    contents = file.read()
    file.close()
except FileNotFoundError:
    print('Error: File not found.')
    exit()

print(sha1(contents).hexdigest().lower())
