import os
import json
from gendiff.generate_diff import generate_diff


# __file__ — это специальная переменная в Python, которая содержит полный
# путь к файлу, где она используется. Необходима  для определения полного
# путя к папке fixtures относительно текущего местоположения файла.
FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


def read_fixture(file_path):
    with open(file_path) as f:
        return f.read()


def test_flat_diff_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'test_file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'test_file2.json')
    expected_result = json.loads(read_fixture(os.path.join(FIXTURES_PATH, 'test_result.json')))
    result = generate_diff(file_path1, file_path2)
    assert result == expected_result
