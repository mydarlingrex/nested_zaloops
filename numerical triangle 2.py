"""
creates a triangle with a side equal to n that goes like this:

1
121
12321
1234321
"""

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(j - 1, 0, -1):
        print(k, end="")
    print()
