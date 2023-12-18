from datetime import datetime

from operation import Operation
from utils import get_operations_instances, get_date, sort_date


def test_get_operations_instances(operations):
    operations_instances = get_operations_instances(operations)
    assert isinstance(operations_instances, list)
    assert isinstance(operations_instances[0], Operation)
    assert operations_instances[1].pk == operations[1]['id']
    assert len(operations_instances) == len(operations) - 1

    operations_instances = get_operations_instances([{}])
    assert operations_instances == []

    operations_instances = get_operations_instances([])
    assert operations_instances == []


def test_get_date():
    operations_instances = Operation(
        pk=0,
        date="2019-08-26T10:50:58.294041",
        state="EXECUTED",
        operation_amount=["31957.58", "руб."],
        description="Перевод организации",
        from_="Maestro 1596837868705199",
        to="Счет 64686473678894779589")
    assert get_date(operations_instances) == datetime(2019, 8, 26, 10, 50, 58, 294041)
