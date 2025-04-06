l1 = [1, 3, 5]
l2 = l1

l1[0] = 44


print(l1) # [44, 3, 5]
print(l2) # [44, 3, 5]

# 2nd Example
myListOne = [1 ,2, 3, 4]

myListTwo = myListOne

myListOne = 'Pramod'

print(myListOne)
print(myListTwo)

myListOne = [1 ,2, 3, 4]

myListOne[0] = 33

print(myListOne)
print(myListTwo)


p1 = ['a', 'b', 'c']
p2 = p1
p2 = ['a', 'b', 'c']
p1[0] = ['ad']

print(p1)
print(p2)



p3 = ['a', 'b', 'c']
p4 = p3
p3[0] = ['ad']

print(p3)
print(p4)

h1 = [1, 2, 3, [4,[4, [5, 6]]]]
h2 = h1[:] # Here we are making a copy. Not referencing.

h1[0] = 333

print(h1)
print(h2)

import copy
h3 = copy.copy(h1)
print(h3)

n = [1, 2, 3]
m = n

print(m == n)
print(m is n) # it is same object inside memory as we . True

m = [1, 2, 3]
print(m == n)
print(m is n) # it is different in the memory.