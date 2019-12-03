from argparse import Namespace
import unittest

from utils.args_parser import create_parser

class CommandLineTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parser = create_parser()
        cls.parser = parser


class ConverterTestCase(CommandLineTestCase):
    def test_with_empty_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--input_file', '--window_size'])

    def test_with_two_args_wrong_window_type_float(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--input_file', 'input.json', '--window_size', '10.0'])

    def test_with_two_args_wrong_window_type_str(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--input_file', 'input.json', '--window_size', 'abc'])

    def test_with_two_args_all_ok(self):
        self.assertEqual(self.parser.parse_args(['--input_file', 'input.json', '--window_size', '10']),
                         Namespace(input_file='input.json', window_size=10))


if __name__ == '__main__':
    unittest.main()
