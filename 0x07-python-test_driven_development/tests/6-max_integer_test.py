#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_positive_integers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_integers(self):
        """Test with a list of mixed positive and negative integers"""
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5)

    def test_duplicate_max(self):
        """Test with a list where the maximum value is duplicated"""
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test with a list of floating-point numbers"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_mixed_floats_and_integers(self):
        """Test with a list of mixed integers and floating-point numbers"""
        self.assertEqual(max_integer([1.1, 2, 3]), 3)

    def test_non_integer_elements(self):
        """Test with a list containing non-integer elements, raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', '4', 5])


if __name__ == '__main__':
    unittest.main()
