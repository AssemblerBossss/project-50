from gendiff.formats.templates import (TEMPLATE_PLAIN_ADDED, TEMPLATE_PLAIN_UPDATED, TEMPLATE_PLAIN_REMOVED,
                                       TEMPLATE_PLAIN_PATH)


def diff_plain_format(data: list) -> str:
    """
    Recursively format the difference tree into a "plain" formatted string.

    This function iterates through the difference tree nodes and returns a
    string representation of the differences in the "plain" format.

    :param data: Difference tree node or subtree as a list of dictionaries.
    :return: String representation of the difference in "stylish" format.
    """

    lines = [line for node in data for line in format_node(node, node['key'])]
    return '\n'.join(lines)


def format_node(data: dict, path: str) -> list:
    """
   Format the node in a "stylish" format.

    This function formats the node representing the difference and returns
    a list of strings representing the difference lines for a node in
    "plain" format.

   :param data: Node representing a difference.
   :param path: The path to the current node
   :return: List of strings representing the difference lines for the node
            in "plain" format.
   """

    line = []
    if data['status'] == 'added':
        line.append(
            TEMPLATE_PLAIN_ADDED.format(
                path,
                format_value(data['value'])
            )
        )

    elif data['status'] == 'removed':
        line.append(
            TEMPLATE_PLAIN_REMOVED.format(
                path
            )
        )

    elif data['status'] == 'changed':
        line.append(
            TEMPLATE_PLAIN_UPDATED.format(
                path,
                format_value(data['old_value']),
                format_value(data['new_value'])
            )
        )

    elif data['status'] == 'nested':
        for child in data['children']:
            nested_path = TEMPLATE_PLAIN_PATH.format(path, child['key'])
            line.extend(format_node(child, nested_path))

    return line


def format_value(value: any) -> any:

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, dict):
        return '[complex value]'

    if value is None:
        return 'null'

    elif isinstance(value, str):
        return "'{}'".format(value)

    elif isinstance(value, int):
        return str(value)
