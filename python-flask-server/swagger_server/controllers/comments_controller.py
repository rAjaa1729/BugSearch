import connexion
import six

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server import util


def questions_question_id_answers_answer_id_comments_comment_id_get(questionId, answerId, commentId):  # noqa: E501
    """Get a particular comment on an answer

     # noqa: E501

    :param questionId: ID of question to get answer for
    :type questionId: int
    :param answerId: ID of answer to get details for
    :type answerId: int
    :param commentId: ID of the comment to get details for
    :type commentId: int

    :rtype: Comment
    """
    return 'do some magic!'


def questions_question_id_answers_answer_id_comments_get(questionId, answerId):  # noqa: E501
    """Get all comments on an answer

     # noqa: E501

    :param questionId: ID of question to get answer for
    :type questionId: int
    :param answerId: ID of answer to get details for
    :type answerId: int

    :rtype: Comment
    """
    return 'do some magic!'


def questions_question_id_comments_comment_id_get(questionId, commentId):  # noqa: E501
    """Get a comment by comment ID

     # noqa: E501

    :param questionId: ID of the question to which the comment belongs
    :type questionId: int
    :param commentId: ID of the comment to get details for
    :type commentId: int

    :rtype: Comment
    """
    return 'do some magic!'


def user_userid_questions_question_id_answers_answer_id_comments_comment_id_delete(userid, questionId, answerId, commentId):  # noqa: E501
    """Delete a comment by comment ID

     # noqa: E501

    :param userid: ID of question to get answer for
    :type userid: int
    :param questionId: ID of question to get answer for
    :type questionId: int
    :param answerId: ID of answer to get details for
    :type answerId: int
    :param commentId: ID of the comment to get details for
    :type commentId: int

    :rtype: None
    """
    return 'do some magic!'


def user_userid_questions_question_id_comments_comment_id_delete(questionId, userid, commentId):  # noqa: E501
    """Delete a comment by comment ID

     # noqa: E501

    :param questionId: ID of the question to comment on
    :type questionId: int
    :param userid: ID of the user
    :type userid: int
    :param commentId: ID of the user
    :type commentId: int

    :rtype: None
    """
    return 'do some magic!'


def user_userid_questions_question_id_comments_post(questionId, userid):  # noqa: E501
    """Post a new comment on a question

     # noqa: E501

    :param questionId: ID of the question to comment on
    :type questionId: int
    :param userid: ID of the user
    :type userid: int

    :rtype: Comment
    """
    return 'do some magic!'
