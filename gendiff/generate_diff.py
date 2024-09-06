from gendiff.parser import parse_data, open_file
from gendiff.construction_diff import create_difference
from gendiff.formats import json_style_difference


def generate_diff(first_argument: str, second_argument: str) -> str:
    """
    Функция генерирует разницу между двумя файлами JSON.
    :param: first_argument (str): путь к первому файлу JSON.
    :param: second_argument (str): путь ко второму файлу JSON.

    :return: разница между файлами в формате JSON (str).
    """

    data1 = parse_data(*open_file(first_argument))
    data2 = parse_data(*open_file(second_argument))
    list_of_differences = create_difference(data1, data2)
    return json_style_difference(list_of_differences)
