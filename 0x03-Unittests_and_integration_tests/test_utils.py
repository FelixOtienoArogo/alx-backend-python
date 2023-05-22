#!/usr/bin/env python3
"""TestAccessNestedMap."""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


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
    def test_access_nested_map_exception(self, nested_map, path):
        """Make sure that the exception message is as expected."""
        with self.assertRaises(KeyError) as Error:
            access_nested_map(nested_map, path)
        self.assertEqual(Error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """Test the json."""
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("test_utils.get_json")
    def test_get_json(self, test_url, test_payload, mock_json):
        """Test that utils.get_json returns the expected result."""
        mock_json.return_value = test_payload
        json = get_json(test_url)
        self.assertEqual(json, test_payload)


class TestMemoize(unittest.TestCase):
    """Test that memoization works"""
    def test_memoize(self):
        """The method to test."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock_method.assert_called_once
