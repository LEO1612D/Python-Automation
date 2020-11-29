from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    
    def test_basic(self):
        testcase = "Sparrow, Jack"
        expected = "Jack Sparrow"
        self.assertEqual(rearrange_name(testcase),expected)

    #Edge cases
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)

    def test_double_name(self):
        testcase = "Canedy, John F."
        expected = "John F. Canedy"
        self.assertEqual(rearrange_name(testcase),expected)

    #Edge Case
    def test_one_name(self):
        testcase = "Nikunj"
        expected = "Nikunj"
        self.assertEqual(rearrange_name(testcase),expected)


unittest.main()

