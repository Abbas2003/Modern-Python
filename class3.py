a : int = 11
b : int = 3

print(a + b) # addtition
print(a - b) # subtraction
print(a * b)
print(a / b) # division
print(a % b) # Modulus
print(a ** b) # exponent
print(2 ** 2) # exponent
print(a // b) # floor division

a += 2
print(a)

a -= 2
print(a)

a *= 2
print(a)

# a /= b
# print(a)

x : int = 7
y : int = 10

print( x == y )
# x == y
# 7 == 10
# False

print( x != y )

a1 : int = 7
b1 : str = '7'

print(a1 == b1)
# a1 == b1
# 7 == 7
# True/ but Answer will be false

print(chr(65))
# A

print(ord('A'))
# 65

fname: str = 'Abbas'
print(not fname == 'Abbas')

m : str = "abc"
n : str = "abc"
print(id(m))
print(id(n))
print(m is n) # compares the backend code
print(m is not n) # compares the backend code

alphabets : list[str] = [chr(i) for i in range (65,91)]
print(alphabets)
print("D" in alphabets)
print("Pakistan" in alphabets)

# PEMDAS
print(3 + 2 - 2 * 4 /2 + 2)
#     3+2−2×4÷2+2
#     3 + 2 - 4 + 2
#      6    - 8

universe_age: int  = 14_000_000_000
print(universe_age)

import cgi
# unzip
#0  1    2     0        1   2
a2 , b2  , c2  = 'abbas', 7, 3.0

print(a2)
print(b2)
print(c2)

data = ('qasim', 7, 3.0)
print(data[0], data[1], data[2])

# Zindagi Asan
data = ('qasim', 7, 3.0)
print(*data)

2 * 2
"a" * 3


