# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]

def find_number_primes(number):
    list_prime = []
    current_prime = 2
    while number != 1:
        if number % current_prime == 0:
            list_prime.append(current_prime)
            number //= current_prime
        else:
            current_prime += 1
    return (list_prime)


number = int(input('Введите положительное число > 1 ---> '))
print(find_number_primes(number))
