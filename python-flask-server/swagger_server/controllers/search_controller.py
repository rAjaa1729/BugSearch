import connexion
import six

from swagger_server.models.question import Question  # noqa: E501
from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def search_questions_get(keyword, sortByUovote=None):  # noqa: E501
    """Search for questions by keyword

     # noqa: E501

    :param keyword: Keyword to search for
    :type keyword: str
    :param sortByUovote: Sort the questions by upvotes
    :type sortByUovote: bool

    :rtype: List[Question]
    """
    return 'do some magic!'


def search_tags_get(keyword):  # noqa: E501
    """Search for tags by keyword

     # noqa: E501

    :param keyword: Keyword to search for
    :type keyword: str

    :rtype: List[Tag]
    """
    return 'do some magic!'


def search_users_get(keyword, sortByCreationDate=None):  # noqa: E501
    """Search for users by keyword

     # noqa: E501

    :param keyword: Keyword to search for
    :type keyword: str
    :param sortByCreationDate: Sort the questions by upvotes
    :type sortByCreationDate: bool

    :rtype: List[User]
    """
    return 'do some magic!'
