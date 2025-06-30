n = int(input())
even = odd = 0
while n:
    d = n % 10
    if d % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print("Even:", even, "Odd:", odd)
