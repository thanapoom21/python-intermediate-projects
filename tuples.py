import sys
import timeit
# Tuple: ordered, immutable, allows duplicate elements
mytuple = tuple(["Thanapoom", 32, "Las Vegas"])
print(mytuple)

item = mytuple[1]

for x in mytuple:
    print(x)

if "Thanapoom" in mytuple:
    print("Yes")
else:
    print("No")

tu = (1, 2, 3, 4, 5, 6, 7, 8, 9)

ple = tu[3:8]
ple2 = tu[::-1]
ple3 = tu[::2]
# print(ple)
# print(ple2)
# print(ple3)

numbers_in_tuple = (2, 4, 6, 8, 10)
# (*) with a variable will combine elements in between and put in a list.
n1, *n2, n3 = numbers_in_tuple
# print(n1)
# print(n2)
# print(n3)

# One advantage of using a tuple is its size is smaller compared to a list with the same elements.
a_list = [0, 1, 2, 3, "google", True]
a_tuple = (0, 1, 2, 3, "google", True)

print(sys.getsizeof(a_list), "bytes")
print(sys.getsizeof(a_tuple), "bytes")

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
