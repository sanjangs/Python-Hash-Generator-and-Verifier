from hashlib import md5
import sys

if len(sys.argv) != 2:
    print('Usage: python md5sum.py [file]')
    exit()

filename = sys.argv[1]

try:
    file = open(filename, 'rb')
    contents = file.read()
    file.close()
except FileNotFoundError:
    print('Error: File not found.')
    exit()

print(md5(contents).hexdigest().lower())
