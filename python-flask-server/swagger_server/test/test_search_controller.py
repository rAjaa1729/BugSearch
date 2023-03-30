# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.question import Question  # noqa: E501
from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchController(BaseTestCase):
    """SearchController integration test stubs"""

    def test_search_questions_get(self):
        """Test case for search_questions_get

        Search for questions by keyword
        """
        query_string = [('keyword', 'keyword_example'),
                        ('sortByUovote', false)]
        response = self.client.open(
            '/api/search/questions',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_tags_get(self):
        """Test case for search_tags_get

        Search for tags by keyword
        """
        query_string = [('keyword', 'keyword_example')]
        response = self.client.open(
            '/api/search/tags',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_users_get(self):
        """Test case for search_users_get

        Search for users by keyword
        """
        query_string = [('keyword', 'keyword_example'),
                        ('sortByCreationDate', true)]
        response = self.client.open(
            '/api/search/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
