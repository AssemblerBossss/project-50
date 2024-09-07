def create_difference(data_1: dict, data_2: dict) -> list[dict]:
    """
    Compares two dictionaries and returns a list of differences.

    :param: data_1: First dictionary to compare.
    :param: data_2: Second dictionary to compare.

    :return:
        list: A list of dictionaries containing information about
        the differences between the two input dictionaries.
        Each dictionary in the list contains the
        following keys: 'key', 'value', 'old_value' (optional),
        'children' (optional), 'new_value' (optional) and 'status'.
        The 'status' key can have one of the following values: 'removed',
        'added', 'unchanged','changed' or nested.
    :rtype: list[dict]
    """

    list_of_differences: list[dict] = []
    keys: list = sorted(data_1.keys() | data_2.keys())

    for key in keys:
        if key in data_1 and key not in data_2:
            node = {'key': key, 'value': data_1[key], 'status': 'removed'}
        elif key not in data_1 and key in data_2:
            node = {'key': key, 'value': data_2[key], 'status': 'added'}
        elif data_1[key] == data_2[key]:
            node = {'key': key, 'value': data_1[key], 'status': 'unchanged'}
        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            children = create_difference(data_1[key], data_2[key])
            node = {'key': key, 'status': 'nested', 'children': children}
        else:
            node = {'key': key, 'old_value': data_1[key],
                    'new_value': data_2[key], 'status': 'changed'}

        list_of_differences.append(node)

    return list_of_differences
