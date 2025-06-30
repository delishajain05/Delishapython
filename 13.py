n = int(input())
s = 0
temp = n
while temp:
    s += temp % 10
    temp //= 10
print("Yes" if n % s == 0 else "No")
