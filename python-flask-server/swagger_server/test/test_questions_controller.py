# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestQuestionsController(BaseTestCase):
    """QuestionsController integration test stubs"""

    def test_questions_get(self):
        """Test case for questions_get

        Get a list of all questions
        """
        query_string = [('sortByUpvotes', true),
                        ('sortByCreationDate', false)]
        response = self.client.open(
            '/api/questions',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_questions_post(self):
        """Test case for questions_post

        Create a new question
        """
        query_string = [('body', 'body_example'),
                        ('title', 'title_example'),
                        ('tags', 'tags_example')]
        response = self.client.open(
            '/api/questions',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_questions_question_id_get(self):
        """Test case for questions_question_id_get

        Get details of a specific question by ID
        """
        response = self.client.open(
            '/api/questions/{questionId}'.format(questionId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_userid_questions_question_id_delete(self):
        """Test case for users_userid_questions_question_id_delete

        Delete a question by ID
        """
        response = self.client.open(
            '/api/users/{userid}/questions/{questionId}'.format(questionId=56, userid=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
