# START
# A
numbers1_100: list[int] = []
for i in range(1, 101):
    numbers1_100.append(i)
print(numbers1_100)
# B
print(numbers1_100[0])
# C
print(numbers1_100[-1])
# D
print(len(numbers1_100))
# E
print(numbers1_100[2:12])
# F
print(numbers1_100[79:])
# G
print(numbers1_100[:17])
# H
print(numbers1_100[::-1])
# I
print(numbers1_100[1:100:2])
# J
print(numbers1_100[2:100:3])
# K
print(numbers1_100[6:100:7])
# L
print(numbers1_100[9:100:10])
# M
print(numbers1_100[98:64:-3])
# N
numbers1_100.insert(49, 999)
print(numbers1_100)
# O
numbers1_100.pop(100)
print(numbers1_100)
# STOP
