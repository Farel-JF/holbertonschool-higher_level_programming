#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 7, 3]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -7, -3]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_identical_elements(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([-7, -7, -7, -7]), -7)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)
        self.assertEqual(max_integer([7, 1, 5, 2]), 7)

    def test_unmodified_list(self):
        test_list = [873, 5654, 465, -389, 0]
        test_copy = list(test_list)
        self.assertTrue(len(test_copy) == len(test_list))
        for i in range(len(test_copy)):
            self.assertTrue(test_copy[i] == test_list[i])
