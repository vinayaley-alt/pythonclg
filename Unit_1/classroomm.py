import math


a = int(input("Students in class 1 : "))
b = int(input("Students in class 2 : "))
c = int(input("Students in class 3 : "))

d1 = math.ceil(a/2)
d2 = math.ceil(b/2)
d3 = math.ceil(c/2)


T = d1 + d2 + d3

print(f"Minimum number of desks are {T}")