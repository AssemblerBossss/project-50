from gendiff.cli import parse_arguments
from gendiff.parser import parse_data, open_file
from gendiff.construction_diff import create_difference
from gendiff.formats import json_style_difference


def generate_diff1() -> str:
    arguments = parse_arguments()
    data1 = parse_data(*open_file(arguments.first_file))
    data2 = parse_data(*open_file(arguments.second_file))
    print(json_style_difference(create_difference(data1, data2)))
    # print(arguments)