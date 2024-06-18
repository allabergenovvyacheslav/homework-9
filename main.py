numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers: # При помощи цикла for переберите список numbers
    is_prime = True # Отметить простоту числа можно переменной is_prime = True перед проверкой
    if i == 1: # число 1 не является ни простым, ни составным числом, оно отсутствует в списках.
        continue
    for j in range(2, i): # ещё один цикл for (вложенный), где будут подбираться делители
        if i % j == 0: # выбранное число не делиться ни на что в диапазоне от 2 до этого числа
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes: ', primes)
print('Not_primes: ', not_primes)
