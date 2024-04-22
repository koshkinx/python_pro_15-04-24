def print_keys(dictionary):
    """
    Виводить всі ключі словника.
    """
    for key in dictionary:
        print(key)

dictionary = {"a": 1, "b": 2, "c": 3}
print("Ключі словника:")
print_keys(dictionary)



def merge_dictionaries(dict1, dict2):
    """
    Повертає новий словник, який є об'єднанням обох вхідних словників.
    """
    return {**dict1, **dict2}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = merge_dictionaries(dict1, dict2)
print("Об'єднаний словник:", merged_dict)