def json_style_difference(list_of_differences: list[dict]) -> str:
    str_diff: str = ""
    for dct in list_of_differences:
        if dct['status'] == 'unchanged':
            str_diff += f"  {dct['key']}: {dct['value']}\n"
        if dct['status'] == 'added':
            str_diff += f"+ {dct['key']}: {dct['value']}\n"
        if dct['status'] == 'removed':
            str_diff += f"- {dct['key']}: {dct['value']}\n"
        if dct['status'] == 'changed':
            str_diff += f"- {dct['key']}: {dct['old_value']}\n+ {dct['key']}: {dct['new_value']}\n"
    return str_diff
