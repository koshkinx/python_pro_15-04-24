def even_or_odd(number):
    """
    Визначає, чи є число парним чи непарним.
    """
    if number % 2 == 0:
        return "Парне"
    else:
        return "Непарне"

number = 7
print("Число", number, "є", even_or_odd(number))


def even_numbers(numbers):
    """
    Приймає список чисел і повертає новий список, що містить тільки парні числа.
    """
    return [number for number in numbers if number % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Парні числа:", even_numbers(numbers))