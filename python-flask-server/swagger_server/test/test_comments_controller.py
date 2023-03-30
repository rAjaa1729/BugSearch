# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCommentsController(BaseTestCase):
    """CommentsController integration test stubs"""

    def test_questions_question_id_answers_answer_id_comments_comment_id_get(self):
        """Test case for questions_question_id_answers_answer_id_comments_comment_id_get

        Get a particular comment on an answer
        """
        response = self.client.open(
            '/api/questions/{questionId}/answers/{answerId}/comments/{commentId}'.format(questionId=56, answerId=56, commentId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_questions_question_id_answers_answer_id_comments_get(self):
        """Test case for questions_question_id_answers_answer_id_comments_get

        Get all comments on an answer
        """
        response = self.client.open(
            '/api/questions/{questionId}/answers/{answerId}/comments'.format(questionId=56, answerId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_questions_question_id_comments_comment_id_get(self):
        """Test case for questions_question_id_comments_comment_id_get

        Get a comment by comment ID
        """
        response = self.client.open(
            '/api/questions/{questionId}/comments/{commentId}'.format(questionId=56, commentId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_userid_questions_question_id_answers_answer_id_comments_comment_id_delete(self):
        """Test case for user_userid_questions_question_id_answers_answer_id_comments_comment_id_delete

        Delete a comment by comment ID
        """
        response = self.client.open(
            '/api/user/{userid}//questions/{questionId}/answers/{answerId}/comments/{commentId}'.format(userid=56, questionId=56, answerId=56, commentId=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_userid_questions_question_id_comments_comment_id_delete(self):
        """Test case for user_userid_questions_question_id_comments_comment_id_delete

        Delete a comment by comment ID
        """
        response = self.client.open(
            '/api/user/{userid}/questions/{questionId}/comments/{commentId}'.format(questionId=56, userid=56, commentId=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_userid_questions_question_id_comments_post(self):
        """Test case for user_userid_questions_question_id_comments_post

        Post a new comment on a question
        """
        response = self.client.open(
            '/api/user/{userid}/questions/{questionId}/comments'.format(questionId=56, userid=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
