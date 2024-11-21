# Tyler Hegy
# UWYO COSC 1010
# Submission Date: 11/21/2024
# Lab 10
# Lab Section: 12
# Sources, people worked with, help given to: N/A
# Comments: Wasn't sure what to do with the rockyou file when we first opened the txt file

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."
# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.
try:
    path1 = Path('rockyou.txt')
    rock = path1.read_text()
    hashed = get_hash(rock)
except FileNotFoundError:
    print('File Not Found')
    hashed = False

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.
try:
    path = Path('hash')
    hash = path.read_text().strip()
except FileNotFoundError:
    print('File Not Found')
    hash = False


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
try:
    path1 = Path('rockyou.txt')
    rock = path1.read_text()
    lines= rock.splitlines()
except FileNotFoundError:
    print('File Not Found')
else:
    for password in lines:
        password = password.strip()
        pass_hash = get_hash(password)
        if pass_hash == hash:
            print(f'Password is {password}')
            break
        else:
            continue
