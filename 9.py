n = int(input())
rev = 0
temp = n
while temp:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Palindrome" if rev == n else "Not Palindrome")
