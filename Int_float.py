def square_number(x):
    """
    Повертає квадрат числа.
    """
    return x ** 2

x = 5
print("Квадрат числа", x, "дорівнює", square_number(x))


def sum_of_two_numbers(a, b):
    """
    Повертає суму двох чисел.
    """
    return a + b

a = 10
b = 20
print("Сума чисел", a, "і", b, "дорівнює",
      sum_of_two_numbers(a, b))


def divide_with_remainder(a, b):
    """
    Виконує операцію ділення та повертає цілу частину і залишок.
    """
    quotient = a // b  # Ціла частина
    remainder = a % b  # Залишок від ділення
    return (quotient, remainder)


dividend = 10
divisor = 3
result = divide_with_remainder(dividend, divisor)
print(f"Ціла частина від ділення {dividend} на {divisor} дорівнює {result[0]}")
print(f"Залишок від ділення {dividend} на {divisor} дорівнює {result[1]}")
