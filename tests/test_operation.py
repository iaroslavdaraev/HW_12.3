import operation
from operation import Operation
from tests.conftest import operations


def test_convert_payment(operation_instances):
    """Тест функции маскировки карты и счета"""
    operation = operation_instances[0]
    assert operation.convert_payment('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    operation = operation_instances[4]
    assert operation.convert_payment('Visa Platinum 1246377376343588') == 'Visa Platinum 1246 37** **** 3588'
    operation = operation_instances[3]
    assert operation.convert_payment('Счет 64686473678894779589') == 'Счет **9589'


def test_convert_date(operations):
    assert operation.datetime


def test_str(operation_instances):
    operation = Operation
    assert operation.__str__(operation_instances[0])
