import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: None
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def users_get(sortByUpvotes=None, sortByCreationDate=None):  # noqa: E501
    """Get a list of all Users

     # noqa: E501

    :param sortByUpvotes: Sort the questions by upvotes
    :type sortByUpvotes: bool
    :param sortByCreationDate: Sort the questions by upvotes
    :type sortByCreationDate: bool

    :rtype: None
    """
    return 'do some magic!'


def users_post(username, password, email):  # noqa: E501
    """Create a new user account

     # noqa: E501

    :param username: Username of the User
    :type username: str
    :param password: password of the User
    :type password: str
    :param email: email of the User
    :type email: str

    :rtype: User
    """
    return 'do some magic!'


def users_userid_follower_get(userid):  # noqa: E501
    """All the follower of the User

     # noqa: E501

    :param userid: username of user to get details for
    :type userid: int

    :rtype: List[str]
    """
    return 'do some magic!'


def users_userid_following_get(userid):  # noqa: E501
    """All the users whom the user is following

     # noqa: E501

    :param userid: username of user to get details for
    :type userid: int

    :rtype: List[str]
    """
    return 'do some magic!'


def users_userid_get(userid):  # noqa: E501
    """Get user details by user ID

     # noqa: E501

    :param userid: username of user to get details for
    :type userid: int

    :rtype: User
    """
    return 'do some magic!'


def users_userid_put(userid, username=None, password=None, about=None, emailid=None, imageurl=None):  # noqa: E501
    """Update user details by user ID

     # noqa: E501

    :param userid: username of user to get details for
    :type userid: int
    :param username: User object that needs to be updated
    :type username: str
    :param password: User object that needs to be updated
    :type password: str
    :param about: User object that needs to be updated
    :type about: str
    :param emailid: User object that needs to be updated
    :type emailid: str
    :param imageurl: User object that needs to be updated
    :type imageurl: str

    :rtype: User
    """
    return 'do some magic!'


def usrs_forgotpassword_post(username, email):  # noqa: E501
    """in case user forgot password

     # noqa: E501

    :param username: Username of the User
    :type username: str
    :param email: email of the User
    :type email: str

    :rtype: User
    """
    return 'do some magic!'
