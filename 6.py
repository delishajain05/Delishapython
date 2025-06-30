n = int(input())
max_d = 0
while n:
    d = n % 10
    if d > max_d:
        max_d = d
    n //= 10
print(max_d)
