from datetime import datetime
import os
from pathlib import Path
import unittest

from utils.process_input import check_file_path, get_duration_from_string, get_timestamp_from_string


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name = os.path.dirname(os.path.abspath(__file__)) + '/test_file'
        cls.csv_path = 'test.json'

    def tearDown(self):
        if Path(self.file_name + '_' + datetime.today().strftime('%Y_%m_%d_%H_%M_%S') + '.csv').is_file():
            os.remove(self.file_name + '_' + datetime.today().strftime('%Y_%m_%d_%H_%M_%S') + '.csv')
        if Path(self.csv_path).is_file():
            os.remove(self.csv_path)

    def make_file(self, file_path, data):
        with open(file_path, 'w') as file:
            for line in data:
                file.write(line + '\n')

    def test_check_file_path_no_file(self):
        path = self.csv_path
        self.assertFalse(check_file_path(path))

    def test_check_file_path_file(self):
        path = self.csv_path
        data = ['{1: 2, 3: 4}', '{5: 6, 7: 8}']
        self.make_file(path, data)
        self.assertTrue(check_file_path(path))

    def test_get_duration_from_float(self):
        self.assertEqual(get_duration_from_string('10.0'), (True, 10.0))

    def test_get_duration_from_int(self):
        self.assertEqual(get_duration_from_string('10'), (True, 10.0))

    def test_get_duration_from_none(self):
        self.assertEqual(get_duration_from_string(None), (False, None))

    def test_get_duration_from_empty_string(self):
        self.assertEqual(get_duration_from_string(''), (False, None))

    def test_get_duration_from_string(self):
        self.assertEqual(get_duration_from_string('abc10'), (False, None))

    def test_get_timestamp_from_bad_string(self):
        self.assertEqual(get_timestamp_from_string('abc10'), (False, None))

    def test_get_timestamp_from_good_timestamp(self):
        self.assertEqual(get_timestamp_from_string('2018-12-26 18:11:08.509654'),
                         (True, datetime(2018, 12, 26, 18, 11, 8, 509654)))

    def test_get_timestamp_from_bad_timestamp(self):
        self.assertEqual(get_timestamp_from_string('2018-12-26 18:11:08'), (False, None))

    def test_get_timestamp_from_none(self):
        self.assertEqual(get_timestamp_from_string(None), (False, None))


if __name__ == '__main__':
    unittest.main()

