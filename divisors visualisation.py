#prints n ordered numbers with the "+" next to each one. the number of "+" equals to the number of divisors

n = int(input())
devisor_num = 0 

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            devisor_num += 1
    print(j, devisor_num * "+", sep="")
    devisor_num = 0
