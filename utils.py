import json


def get_all_operations(path):
    """
    Функция получает операции из файла
    :param path: путь к файлу
    :return: json с операциями
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)
