

def open_file(filename_1: str) -> tuple[str, str]:
    """
    Opens a file and returns its content and format.

    Args:
        filename_1 (str): Path to the file.

    Returns:
        tuple[str, str]: A tuple containing the content of the file and its format. The format can be either 'json' or 'yaml'.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """

    with open(filename_1, encoding='utf-8') as file:
        text = file.read()
        if filename_1.endswith('.json'):
            data_format = 'json'
        if filename_1.endswith('.yaml') or filename_1.endswith('yml'):
            data_format = 'yaml'
    return text, data_format
