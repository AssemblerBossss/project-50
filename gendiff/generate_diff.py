from gendiff.cli import parse_arguments
from gendiff.parser import parse_data, open_file
from gendiff.construction_diff import create_difference
from gendiff.formats import json_style_difference


def generate_diff() -> str:
    """
    Generate a difference report between two files.

    This function takes two file paths as input and compares the content of the
    files to generate a difference report. It loads the data from the files,
    finds the difference between the data
    """
    arguments = parse_arguments()
    data1 = parse_data(*open_file(arguments.first_file))
    data2 = parse_data(*open_file(arguments.second_file))
    list_of_differences = create_difference(data1, data2)
    return json_style_difference(list_of_differences)
