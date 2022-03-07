n = int(input())
for _ in range(n):
    s = input()
    s = s.lower()

    if s == s[::-1]:
        print("Yes")
    else:
        print("No")