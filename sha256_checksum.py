import os
import hashlib

while True:
    file = input('\n Enter file path: ')
    if not os.path.exists(file):
        print('File not found')
        exit()

    with open(file, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    print(f'SHA256 hash found: {h}')

    provided_h = input('Enter hash to compare: ')

    if provided_h == h:
        print('\033[32mMatch found! File integrity check successful.\033[0m')
    else:
        print('\033[91mNo match found! File integrity check failed.\033[0m')

    exit = input('\n Try again? [Y/N]: ')

    if exit != 'y':
        print('Goodbye!..')
        break
