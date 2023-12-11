import json

from Models.operation import Operation


def get_all_operations(path):
    """
    Функция получает операции из файла
    :param path: путь к файлу
    :return: json с операциями
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_operations_instances(operations):
    """
    Получает экземпляры классы
    :param operations: pk, date, state, operation_amount, description, from_, to
    :return: dict operation_instances
    """
    operations_instances = []
    for operation in operations:
        if operation:
            operations_instance = Operation(
                pk=operation['id'],
                date=operation['date'],
                state=operation['state'],
                operation_amount=operation['operationAmount'],
                description=operation['description'],
                from_=operation.get('from', ''),
                to=operation['to'],
            )
            operations_instances.append(operations_instance)
    return operations_instances
