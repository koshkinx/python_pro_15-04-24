def length_of_string(s):
    """
    Повертає довжину рядка.
    """
    return len(s)


string = "I love python"
print("Довжина рядка:", length_of_string(string))


def concatenate_strings(str1, str2):
    """
    Об'єднує два рядки.
    """
    return str1 + str2


string1 = "I love "
string2 = "python!"
print("Об'єднаний рядок:", concatenate_strings(string1, string2))
