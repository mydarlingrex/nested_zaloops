# n < m
# calculates a number with the biggest sum of divisors and their sum. prints the number and the sum of divisors.

n, m = int(input()), int(input())
sum_divisors = 0
x = 0
max_num = 0

for i in range(n, m + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_divisors += j
            if sum_divisors >= x:
                x = sum_divisors
                max_num = i
    sum_divisors = 0 # I need more 000000000000000000
print(max_num, x)
