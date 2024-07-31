print("welcome")
# int
print("----------")
a = -10
print(f"{a}")
a = 10
print(f"{a}")
b = type(a)
print(f"{b}")
print("----------")

#float
a = 1.1
print(f"{a}")
b = type(a)
print(f"{b}")
print("----------")

#complex
a=2+2j
print(a)
b=type(a)
print(b)
print("----------")

#boolean
a = True
b = False
print(a)
print(b)
print(type(a))
print(type(b))
print("----------")

#string
a,b="hello","hi"
print(a)
print(b)
print(f'{type(a)}\n{type(b)}')
print("----------")

#float -> int
a = 1.9
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))
print("----------")

#str -> int
a = "31"
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))
print("----------")