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


def line_format(key: str, value:  any, depth: int, char: str) -> str:
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



def format_dict(dictionary: dict, depth: int):
    pass


def format_value(value: any):
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
