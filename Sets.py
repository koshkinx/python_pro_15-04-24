def union_of_sets(set1, set2):
    """
    Повертає об'єднання двох множин.
    """
    return set1 | set2

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Об'єднання множин:", union_of_sets(set1, set2))


def is_subset(set_1, set_2):
    """
    Перевіряє, чи є одна множина підмножиною іншої.
    """
    return set_1.issubset(set_2)

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
print("Чи є set1 підмножиною set2:", is_subset(set_1, set_2))