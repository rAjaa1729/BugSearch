import connexion
import six

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server import util


def questions_question_id_answers_answer_id_get(questionId, answerId):  # noqa: E501
    """Get details of a specific answer to a specific question by ID

     # noqa: E501

    :param questionId: ID of question to get answer for
    :type questionId: int
    :param answerId: ID of answer to get details for
    :type answerId: int

    :rtype: Answer
    """
    return 'do some magic!'


def questions_question_id_answers_get(questionId, sortByUpvotes=None, sortByCreationDate=None):  # noqa: E501
    """Get a list of all answers to a specific question by ID

     # noqa: E501

    :param questionId: ID of question to get answers for
    :type questionId: int
    :param sortByUpvotes: Sort the questions by upvotes
    :type sortByUpvotes: bool
    :param sortByCreationDate: Sort the questions by upvotes
    :type sortByCreationDate: bool

    :rtype: Answer
    """
    return 'do some magic!'


def user_userid_questions_question_id_answers_answer_id_delete(questionId, answerId, userid):  # noqa: E501
    """Delete an answer to a specific question by ID

     # noqa: E501

    :param questionId: ID of question to get answer for
    :type questionId: int
    :param answerId: ID of answer to get details for
    :type answerId: int
    :param userid: ID of userid
    :type userid: int

    :rtype: None
    """
    return 'do some magic!'


def users_userid_questions_question_id_answers_post(questionId, userid, body=None):  # noqa: E501
    """Post a new answer to a specific question

     # noqa: E501

    :param questionId: ID of question to get answers for
    :type questionId: int
    :param userid: ID of userid
    :type userid: int
    :param body: Question object that needs to be created
    :type body: str

    :rtype: Answer
    """
    return 'do some magic!'
