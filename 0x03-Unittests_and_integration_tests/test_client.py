#!/usr/bin/env python3
"""TestGithubOrgClient."""
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """Method to unit-test GithubOrgClient._public_repos_url."""
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))
