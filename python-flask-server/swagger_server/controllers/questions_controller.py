import connexion
import six

from swagger_server import util


def questions_get(sortByUpvotes=None, sortByCreationDate=None):  # noqa: E501
    """Get a list of all questions

     # noqa: E501

    :param sortByUpvotes: Sort the questions by upvotes
    :type sortByUpvotes: bool
    :param sortByCreationDate: Sort the questions by upvotes
    :type sortByCreationDate: bool

    :rtype: None
    """
    return 'do some magic!'


def questions_post(body, title, tags):  # noqa: E501
    """Create a new question

     # noqa: E501

    :param body: Question object that needs to be created
    :type body: str
    :param title: Question object that needs to be created
    :type title: str
    :param tags: Question object that needs to be created
    :type tags: str

    :rtype: None
    """
    return 'do some magic!'


def questions_question_id_get(questionId):  # noqa: E501
    """Get details of a specific question by ID

     # noqa: E501

    :param questionId: ID of question to get details for
    :type questionId: int

    :rtype: None
    """
    return 'do some magic!'


def users_userid_questions_question_id_delete(questionId, userid):  # noqa: E501
    """Delete a question by ID

     # noqa: E501

    :param questionId: ID of question to get details for
    :type questionId: int
    :param userid: ID of userid
    :type userid: int

    :rtype: None
    """
    return 'do some magic!'
