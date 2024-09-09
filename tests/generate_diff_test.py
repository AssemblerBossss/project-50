import os
import pytest
from gendiff.generate_diff import generate_diff


# __file__ — это специальная переменная в Python, которая содержит полный
# путь к файлу, где она используется. Необходима  для определения полного
# путя к папке fixtures относительно текущего местоположения файла.
FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


def read_fixture(file_path):
    with open(file_path) as f:
        return f.read()


def write_fixture(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)


file1_json = os.path.join(FIXTURES_PATH, 'test1_file1.json')
file2_json = os.path.join(FIXTURES_PATH, 'test1_file2.json')
file1_yaml = os.path.join(FIXTURES_PATH, 'test_file1.yaml')
file2_yaml = os.path.join(FIXTURES_PATH, 'test_file2.yaml')
json_res1 = os.path.join(FIXTURES_PATH, 'results/test1_result_stylish.txt')

file3_json = os.path.join(FIXTURES_PATH, 'test2_file1.json')
file4_json = os.path.join(FIXTURES_PATH, 'test2_file2.json')
json_res2 = os.path.join(FIXTURES_PATH, 'results/test2_result_stylish.txt')

file5_json = os.path.join(FIXTURES_PATH, 'test3_file1.json')
file6_json = os.path.join(FIXTURES_PATH, 'test3_file2.json')
json_res3 = os.path.join(FIXTURES_PATH, 'results/test3_result_stylish.txt')

file7_json = os.path.join(FIXTURES_PATH, 'test4_file1.json')
file8_json = os.path.join(FIXTURES_PATH, 'test4_file2.json')
file7_yaml = os.path.join(FIXTURES_PATH, 'test4_file1.yaml')
file8_yaml = os.path.join(FIXTURES_PATH, 'test4_file2.yaml')
json_res4 = os.path.join(FIXTURES_PATH, 'results/test4_result_stylish.txt')


test_cases = [
    (generate_diff, file1_json, file2_json, json_res1, 'stylish'),
    (generate_diff, file1_yaml, file2_yaml, json_res1, 'stylish'),
    (generate_diff, file3_json, file4_json, json_res2, 'stylish'),
    (generate_diff, file5_json, file6_json, json_res3, 'stylish'),
    (generate_diff, file7_json, file8_json, json_res4, 'stylish'),
    (generate_diff, file7_yaml, file8_yaml, json_res4, 'stylish')
    # (generate_diff, file1_yaml, file2_yaml, 'plain', plain_res),
    # (generate_diff, file1_yaml, file2_yaml, 'json', json_res)
]


@pytest.mark.parametrize(
    "generate_diff_func, file1, file2, expected_file, format_", test_cases
)
def test_generate_diff(
        generate_diff_func,
        file1,
        file2,
        expected_file,
        format_
):
    expected = read_fixture(expected_file)
    actual = generate_diff_func(str(file1), str(file2),format_)

    assert actual == expected
