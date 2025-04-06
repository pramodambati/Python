print(40 + int(2.3))
print(float(40))
print('chai' + 'code')
# print('chai' - 'code') This won't happen.

x = 1
y = 2
z = 3

print(x, y, z)

# x, y, z = 1, 2, 3
print(x + 1, y + 2, z)

# In python shell why it is coming as tuple ??

# >>> x = 1
# >>> y = 2
# >>> z = 3
# >>> x, y, z
# (1, 2, 3)

# print(2 ** 100)
# print(2 ** 1000)
# print(2 ** 10000)


result = 1/3
# print(result)

# print(repr('chai'))
# print(str('chai'))
# print('chai')


print(3 == 3.0)
print(4 != 5)

x = 1 == 2 < 3
y = 1 == 2 and 2 < 3

print(x)
print(y)

import math

# floor takes you to the lowest number.
print(math.floor(3.5))
print(math.floor(3.98))
print(math.floor(-3.5))

# trunc takes you towards the 0
print(math.trunc(2.8))
print(math.trunc(-2.8))

print(99999999999999999999999999999 + 1)
print(99999999999999999999999999999 + 1.2)
print(2 * 10)
print(2 + 1j) # iota numbers
print((2 + 1j) * 3)

# octal base. 0o
print(0o20)

# hexal base. 0x
print(0xFF)

# binary base. 0b
print(0b1000)

print(oct(64))
print(bin(64))
print(hex(64))

print(int(3.14))
print(int('64', 8))
print(int('1000', 2))
# print(int('64', 2)) ValueError: invalid literal for int() with base 2: '64'



import random
print(random.random())
print(random.randint(1, 10))
print(random.choice(['lemon tea', 'masala tea', 'ginger tea', 'mint tea']))

l1 = ['lemon tea', 'masala tea', 'ginger tea', 'mint tea']
print(random.shuffle(l1))
print(random.shuffle(['lemon tea', 'masala tea', 'ginger tea', 'mint tea']))
# print(random.shuffle(1, 10, 9, 8, 3))

print(0.1 + 0.1 + 0.4) # why
print(0.1 + 0.1 + 0.5)
print(0.1 + 0.1 + 0.1 - 0.3)
print((0.1 + 0.1 + 0.1) - 0.3)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1')  + Decimal('0.1') )
print(Decimal('0.1') + Decimal('0.1')  + Decimal('0.1') - Decimal('0.3') )

from fractions import Fraction
myFra = Fraction(2, 7)
print(myFra)

# Sets

setone = {1, 2, 3}
print(setone)
print(setone & {1, 2}) #intersection
print(setone | {1, 5}) #union
print(setone - {1, 2, 3}) # set() Empty set.
print(type({}))
print(type(True))
print(True == 1)
print(True is 1) # False Both are different in memory. Values are same internally
print(False == 0)
print(True + 2)

# Assignment
# 1) what is the format of 64 in 16 form
# 2) what is the format of 8 in 2 form
