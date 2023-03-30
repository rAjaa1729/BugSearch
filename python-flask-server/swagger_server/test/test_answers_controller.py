# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnswersController(BaseTestCase):
    """AnswersController integration test stubs"""

    def test_questions_question_id_answers_answer_id_get(self):
        """Test case for questions_question_id_answers_answer_id_get

        Get details of a specific answer to a specific question by ID
        """
        response = self.client.open(
            '/api/questions/{questionId}/answers/{answerId}'.format(questionId=56, answerId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_questions_question_id_answers_get(self):
        """Test case for questions_question_id_answers_get

        Get a list of all answers to a specific question by ID
        """
        query_string = [('sortByUpvotes', true),
                        ('sortByCreationDate', false)]
        response = self.client.open(
            '/api/questions/{questionId}/answers'.format(questionId=56),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_userid_questions_question_id_answers_answer_id_delete(self):
        """Test case for user_userid_questions_question_id_answers_answer_id_delete

        Delete an answer to a specific question by ID
        """
        response = self.client.open(
            '/api/user/{userid}/questions/{questionId}/answers/{answerId}'.format(questionId=56, answerId=56, userid=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_userid_questions_question_id_answers_post(self):
        """Test case for users_userid_questions_question_id_answers_post

        Post a new answer to a specific question
        """
        query_string = [('body', 'body_example')]
        response = self.client.open(
            '/api/users/{userid}/questions/{questionId}/answers'.format(questionId=56, userid=56),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
