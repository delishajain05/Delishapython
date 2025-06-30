n = int(input())
s = 0
temp = n
while temp:
    d = temp % 10
    s += d ** 3
    temp //= 10
print("Armstrong" if s == n else "Not Armstrong")
