n = int(input())
pos = int(input())
for i in range(pos - 1):
    n //= 10
print(n % 10)
