#!/usr/bin/python3
#
#
__author__ = 'bofh'

import random, string

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	print()
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('\nHow many characters in your password? '))))
print()
