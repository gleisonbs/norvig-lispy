import unittest

from lis import tokenize, parse, eval

class TestTokenizer(unittest.TestCase):
    def test_tokenizer(self):
        """
        Test that it tokenizes correctly
        """

        input_data = '(begin (define r 10) (* pi (* r r)))'
        expected_data = ['(', 'begin', '(', 'define', 'r', '10', ')', '(', '*', 'pi', '(', '*', 'r', 'r', ')', ')', ')']
        actual_data = tokenize(input_data)
        self.assertEqual(expected_data, actual_data)

    def test_parser(self):
        """
        Test that it parses correctly
        """

        input_data = '(begin (define r 10) (* pi (* r r)))'
        expected_data = ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]
        actual_data = parse(input_data)
        self.assertEqual(expected_data, actual_data)

    def test_eval(self):
        """
        Test that it evals correctly
        """

        input_data = "(begin (define r 10) (* pi (* r r)))"
        expected_data = 314.1592653589793
        actual_data = eval(parse(input_data))

if __name__ == '__main__':
    unittest.main()