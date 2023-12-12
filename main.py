from config import OPERATIONS_PATH
from utils import get_operations_instances, get_all_operations, sort_date


def main():
    all_operations = get_all_operations(OPERATIONS_PATH)
    operations_instances = get_operations_instances(all_operations)
    sort_operations = sort_date(operations_instances)
    for operation in sort_operations[:5]:
        print(operation)


if __name__ == '__main__':
    main()
