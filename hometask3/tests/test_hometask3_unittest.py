import unittest

from hometask3.task3 import get_digits, get_file_extension

class TestStrings(unittest.TestCase):

    def test_get_file_extension(self):
        self.assertEqual(get_file_extension('test_file.jpg'), 'jpg')

    def test_get_digits(self):
        self.assertEqual(get_digits('dasd123412gdfg456'), '123412456')


if __name__ == '__main__':
    unittest.main()

