"""
creates a triangle that goes like this:
1
2 3
4 5 6
7 8 9 10
"""

n = int(input())
x = 1

for i in range(1, n + 1):
    for j in range(i):
        print(x, end=" ")
        x += 1
    print()
