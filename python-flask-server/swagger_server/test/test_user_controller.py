# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_login_user(self):
        """Test case for login_user

        Logs user into the system
        """
        query_string = [('username', 'username_example'),
                        ('password', 'password_example')]
        response = self.client.open(
            '/api/users/login',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_user(self):
        """Test case for logout_user

        Logs out current logged in user session
        """
        response = self.client.open(
            '/api/users/logout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        Get a list of all Users
        """
        query_string = [('sortByUpvotes', true),
                        ('sortByCreationDate', false)]
        response = self.client.open(
            '/api/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Create a new user account
        """
        query_string = [('username', 'username_example'),
                        ('password', 'password_example'),
                        ('email', 'email_example')]
        response = self.client.open(
            '/api/users',
            method='POST',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_userid_follower_get(self):
        """Test case for users_userid_follower_get

        All the follower of the User
        """
        response = self.client.open(
            '/api/users/{userid}/follower'.format(userid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_userid_following_get(self):
        """Test case for users_userid_following_get

        All the users whom the user is following
        """
        response = self.client.open(
            '/api/users/{userid}/following'.format(userid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_userid_get(self):
        """Test case for users_userid_get

        Get user details by user ID
        """
        response = self.client.open(
            '/api/users/{userid}'.format(userid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_userid_put(self):
        """Test case for users_userid_put

        Update user details by user ID
        """
        query_string = [('username', 'username_example'),
                        ('password', 'password_example'),
                        ('about', 'about_example'),
                        ('emailid', 'emailid_example'),
                        ('imageurl', 'imageurl_example')]
        response = self.client.open(
            '/api/users/{userid}'.format(userid=56),
            method='PUT',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usrs_forgotpassword_post(self):
        """Test case for usrs_forgotpassword_post

        in case user forgot password
        """
        query_string = [('username', 'username_example'),
                        ('email', 'email_example')]
        response = self.client.open(
            '/api/usrs/forgotpassword',
            method='POST',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
