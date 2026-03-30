"""
Mock responses for JSONPlaceholder API
"""
import json
from unittest.mock import MagicMock


def mock_urlopen_for_post(post_id):
    """
    Creates a mock urlopen context manager that returns post data
    """
    mock_response = MagicMock()
    post_data = {
        'userId': 1,
        'id': post_id,
        'title': f'Sample Post {post_id}',
        'body': f'This is the body of post {post_id}'
    }
    mock_response.read.return_value.decode.return_value = json.dumps(post_data)
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None
    return mock_response


def mock_urlopen_for_comments(post_id):
    """
    Creates a mock urlopen context manager that returns comments data
    """
    mock_response = MagicMock()
    comments_data = [
        {
            'postId': post_id,
            'id': 1,
            'name': 'Comment 1',
            'email': 'user1@example.com',
            'body': 'First comment'
        },
        {
            'postId': post_id,
            'id': 2,
            'name': 'Comment 2',
            'email': 'user2@example.com',
            'body': 'Second comment'
        }
    ]
    mock_response.read.return_value.decode.return_value = json.dumps(comments_data)
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None
    return mock_response
