
import sys
a = range(100)
print(a)
print(type(a))

b = list(a)
c =  tuple(a)
d = set(a)


print('range: ', sys.getsizeof(a))
print('list: ', sys.getsizeof(b))
print('tuple: ', sys.getsizeof(c))
print('set: ', sys.getsizeof(d))


