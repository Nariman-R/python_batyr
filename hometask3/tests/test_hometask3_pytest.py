import pytest

from hometask3.task3 import get_digits, get_file_extension


@pytest.mark.parametrize("file_extension, expected_result", [
    ('test_file.jpg', 'jpg'),
    ('test_file.tst', 'tst'),
    ('test_file.exe',  'exe'),
    ('test_file', ''),
])
def test_get_file_extension(file_extension, expected_result):
    assert get_file_extension(file_extension) == expected_result


@pytest.mark.parametrize("text_string, expected_result", [
    ('dasd123412gdfg456', '123412456'),
    ('gfddsfgsdfg45645ghfgh76867', '4564576867'),
    ('123123554fgd56',  '12312355456'),
    ('test_file', ''),
])
def test_get_digits(text_string, expected_result):
    assert get_digits(text_string) == expected_result
