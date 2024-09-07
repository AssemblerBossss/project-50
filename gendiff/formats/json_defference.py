from itertools import chain

INDENT_CHAR = '    '
STEP = 2


def diff_stylish_format(data: list, depth: int = 0) -> str:
    """
    Recursively format the difference tree into a "stylish" formatted string.

    This function iterates through the difference tree nodes and returns a
    string representation of the differences in the "stylish" format. It uses
    indentation to represent nested structures.

    :param data: Difference tree node or subtree as a list of dictionaries.
    :param depth: Current depth level for indentation (optional).
    :return: String representation of the difference in "stylish" format.
    """
    indent: str = INDENT_CHAR * depth
    lines = [line for node in data for line in format_node(node, depth)]
    result = chain('{', lines, [indent + '}'])
    return '\n'.join(result)


def format_node(data: dict, depth: int) -> list[str]:
    pass


def json_style_difference(list_of_differences: list[dict]) -> str:
    str_diff: str = "{"
    for dct in list_of_differences:
        if dct['status'] == 'unchanged':
            str_diff += f"\n    {dct['key']}: {dct['value']}"
        if dct['status'] == 'added':
            str_diff += f"\n  + {dct['key']}: {dct['value']}"
        if dct['status'] == 'removed':
            str_diff += f"\n  - {dct['key']}: {dct['value']}"
        if dct['status'] == 'changed':
            str_diff += (f"\n  - {dct['key']}: {dct['old_value']}\n"
                         f"  + {dct['key']}: {dct['new_value']}")
        if dct['status'] == 'nested':
            nested_string: str = f"\n    {dct['key']}: {json_style_difference(dct['children'])}"
            str_diff += nested_string
    str_diff += '\n}'
    return str_diff
