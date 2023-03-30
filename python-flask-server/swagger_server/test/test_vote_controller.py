# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestVoteController(BaseTestCase):
    """VoteController integration test stubs"""

    def test_users_userid_questions_question_id_answers_answer_id_vote_vote_type_post(self):
        """Test case for users_userid_questions_question_id_answers_answer_id_vote_vote_type_post

        
        """
        response = self.client.open(
            '/api/users/{userid}/questions/{questionId}/answers/{answerId}/vote/{vote_type}'.format(vote_type=56, questionId=56, answerId=56, userid=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_userid_questions_question_id_vote_vote_type_post(self):
        """Test case for users_userid_questions_question_id_vote_vote_type_post

        
        """
        response = self.client.open(
            '/api/users/{userid}/questions/{questionId}/vote/{vote_type}'.format(vote_type=56, questionId=56, userid=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
