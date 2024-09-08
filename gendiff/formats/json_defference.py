from itertools import chain
import templates


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


def format_node(data: dict, depth: int) -> list:
    """
   Format the node in a "stylish" format.

    This function formats the node representing the difference and returns
    a list of strings representing the difference lines for a node in
    "stylish" format.

   :param data: Node representing a difference.
   :param depth: Current depth level.
   :return: List of strings representing the difference lines for the node
            in "stylish" format.
   """

    line = []
    if data['status'] == 'added':
        line.append(line_format(
            data['key'], data['value'], depth, '+ ')
        )

    elif data['status'] == 'removed':
        line.append(
            line_format(data['key'], data['value'], depth, '- ')
        )

    elif data['status'] == 'changed':
        line.append(
            line_format(data['key'], data['old_value'], depth, '- ')
        )
        line.append(
            line_format(data['key'], data['new_value'], depth, '+ ')
        )

    elif data['status'] == 'unchanged':
        line.append(
            line_format(data['key'], data['value'], depth, '  ')
        )

    elif data['status'] == 'nested':

        nest_indent = INDENT_CHAR * (depth + STEP)

        nested_lines = [
            line
            for child in data['children']
            for line in format_node(child, depth + STEP)
        ]

        nested_block = '\n'.join(nested_lines)
        line.append(
            f'{nest_indent}{data["key"]}: {{\n{nested_block}\n{nest_indent}}}'
        )

    return line


def line_format(key: str, value: any, depth: int, char: str) -> str:
    """
    Format a line in the "stylish" format.

    This function formats a line representing a difference and returns a
    string representation for the line in "stylish" format.

    :param key: Key representing the difference.
    :param value: Value associated with the key.
    :param depth: Current depth level.
    :param char: Symbol representing the type of difference.
    :return: String representation of the line in "stylish" format.
    """

    indent = INDENT_CHAR * depth
    line = []
    if isinstance(value, dict):
        line.append(templates.TEMPLATE_STYLISH.format(
            indent, char, key, format_dict(value, depth + STEP)))

    else:
        line.append(templates.TEMPLATE_STYLISH.format(
            indent, char, key, format_value(value)
        ))

    return '\n'.join(line)


def format_dict(data: dict, depth: int) -> str:
    """
    Format a dictionary in the "stylish" format.

    This function formats a dictionary representing a nested structure and
    returns a string representation for the dictionary in "stylish" format.

    :param data: Dictionary representing the nested structure.
    :param depth: Current depth level.
    :return: String representation of the dictionary in "stylish" format.
    """
    indent = INDENT_CHAR * depth
    line = []
    for key, value in data.items():
        line.append(line_format(key, value, depth, '  '))

    result = chain('{', line, [indent + '}'])

    return '\n'.join(result)


def format_value(value: any) -> any:
    """
    This function takes values in dictionaries
    and converts it to a string representation other than integer.
    Dictionaries and their values are processed recursively.
    :param value: The value to be converted to a string.
    :return: A string representation of a value or a dictionary.
    """

    nested_dict = {}

    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    elif isinstance(value, dict):
        for key in value:
            nested_dict[key] = format_value(value[key])
    else:
        return value
    return nested_dict
