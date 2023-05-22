#!/usr/bin/env python3
"""TestAccessNestedMap."""
import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """The first unit test for utils.access_nested_map."""
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Method to test that the method returns what it is supposed to."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exceptions(self, nested_map, path):
        """Make sure that the exception message is as expected."""
        with self.assertRaises(KeyError) as Error:
            access_nested_map(nested_map, path)
        self.assertEqual(Error.exception.args[0], path[-1])
