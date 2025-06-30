n = int(input())
prev = 10
flag = True
while n:
    d = n % 10
    if d >= prev:
        flag = False
        break
    prev = d
    n //= 10
print("Yes" if flag else "No")
