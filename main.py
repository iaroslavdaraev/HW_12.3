from config import OPERATIONS_PATH
from utils import get_operations_instances, get_all_operations


def main():
    all_operations = get_all_operations(OPERATIONS_PATH)
    operations_instances = get_operations_instances(all_operations)


if __name__ == '__main__':
    main()
