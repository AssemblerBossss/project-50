from gendiff.parser import parse_data, open_file
from gendiff.construction_diff import create_difference
from gendiff.formats import diff_stylish_format


def generate_diff(first_argument: str, second_argument: str, format_name: str) -> str:
    """
    Функция генерирует разницу между двумя файлами JSON.
    :param: first_argument (str): путь к первому файлу JSON.
    :param: second_argument (str): путь ко второму файлу JSON.

    :return: разница между файлами в формате JSON (str).
    """

    data1 = parse_data(*open_file(first_argument))
    data2 = parse_data(*open_file(second_argument))
    list_of_differences = create_difference(data1, data2)
    diff = select_format(list_of_differences, format_name)
    return diff


def select_format(data: list, format_name: str) -> str:
    """
    Sets the diff report output format based on the given argument

    :param data: Difference tree.
    :param format_name: Stylish, plain or json.
    :return: Formatted output.
    """
    if format_name == 'stylish':
        return diff_stylish_format(data)
    # elif form == 'plain':
    #     return diff_plain_format(data)
    #
    # elif form == 'json':
    #     return get_json(data)
