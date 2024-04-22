def average_of_list(numbers):
    """
    Обчислює середнє значення списку чисел.
    """
    total = sum(numbers)
    length = len(numbers)
    if length == 0:
        return 0
    return total / length


num_list = [5, 10, 15, 20, 25]
print("Середнє значення списку чисел:", average_of_list(num_list))


def common_elements(list1, list2):
    """
    Повертає список, що містить спільні елементи обох списків.
    """
    return list(set(list1) & set(list2))


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print("Спільні елементи списків:", common_elements(list1, list2))
