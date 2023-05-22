#!/usr/bin/env python3
"""TestGithubOrgClient."""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test value by GithubOrgClient."""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, get):
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org)
        test_return = client.org
        self.assertEqual(test_return, get.return_value)
        get.assert_called_once
