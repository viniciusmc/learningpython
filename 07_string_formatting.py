#!/usr/bin/python3

n = 11
f = 1.2345678
s = "computer"

print("My number is {:d}".format(n))
print("My number is {:b}".format(n))

print("{:.3f}".format(f))
print("{:11.3f}".format(f))
print("{:011.3f}".format(f))
print("{0} {1} {2}".format(n, f, s))

print("{name} own(s) {amount} of {object}".format(
    name="Vinicius",
    amount=5,
    object="mangos"
))
