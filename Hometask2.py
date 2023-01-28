# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Input any three digit number: "))
print(n)

sum = n % 10 + n // 10 % 10 + n // 100
print(sum)