from Models.operation import Operation
from utils import get_operations_instances, get_date


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
