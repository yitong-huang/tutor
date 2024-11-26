a = 5
b = 3

print("+", a + b)
print("-", a - b)
print("*", a * b)
print("/", a / b)
print("%", a % b)
print("**", a ** b)
print("//", a // b)
print("//", -5 // 3)


print("==", a == b)
print("!=", a != b)
#print("<>", a <> b)
print(">", a > b)

a += b
print("+=", a)

c = 60           # 60 = 0011 1100
d = 13           # 13 = 0000 1101

e = c & d
print("&", e)    # 12 = 0000 1100
e = c | d
print("|", e)    # 61 = 0011 1101
e = c ^ d
print("^", e)    # 49 = 0011 0001
e = ~c
print("~", e)    # -61= 1100 0011
e = c << 2
print("<<2", e)  # 240= 1111 0000
e = c >> 2
print(">>2", e)  # 15 = 0000 1111

f = 3
g = 4
simple_list = [1, 2, 3]
print(f in simple_list)
print(g in simple_list)
print(f not in simple_list)
print(g not in simple_list)

h = 'h'
first_name = 'huang'
last_name = 'yitong'
print(h in first_name)
print(h in last_name)

