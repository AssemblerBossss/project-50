import json
import yaml


def open_file(filename_1: str) -> tuple[str, str]:
    """
    Opens a file and returns its content and format.

    :param filename_1: Path to the file.
    :return: A tuple containing the content of the file
            and its format. The format can be either 'json' or 'yaml'.
    :rtype: tuple[str, str]:
    :raise: FileNotFoundError: If the specified file does not exist.
    """

    with open(filename_1, encoding='utf-8') as file:
        text = file.read()
        if filename_1.endswith('.json'):
            data_format = 'json'
        if filename_1.endswith('.yaml') or filename_1.endswith('yml'):
            data_format = 'yaml'
    return text, data_format


def parse_data(data: str, data_format: str) -> dict:
    """
    Parsing data from JSON or YAML into a dictionary.

    This function accepts data as a string and the name
    of the format to which this data belongs.
    Depending on the name of the format, JSON or YAML
    data is converted into a dictionary. The data is returned.

    :param data: Text data
    :param data_format: Format
    :return: Parsed data
    :rtype: dict
    """

    if data_format == 'yaml':
        return yaml.load(data, yaml.Loader)
    if data_format == 'json':
        return json.loads(data)
