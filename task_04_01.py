# 1. Вычислить число c заданной точностью d

# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

from decimal import Decimal
 
input_number = Decimal(input("Enter a real number: "))
number_accuracy = input("Enter the required accuracy '0.0001': ")
print(input_number.quantize(Decimal(number_accuracy)))

# Простите, но что тут можно вынести в функцию я не понял.