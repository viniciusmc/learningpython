#!/usr/bin/python3

alpha = ["a", "b", "c", "d"]
alpha = alpha + ["e", "f"]

print(alpha)
d_index = alpha.index("d")
print("d_index: " + str(d_index))
del alpha[d_index]
print(alpha)

alpha.remove("c")
print(alpha)
