"""
Mocks for JSONPlaceholder API
"""
from unittest.mock import Mock
import json


def mock_urlopen_for_post(post_id, post_data, comments_data):
    """
    Creates a mock for urllib.request.urlopen that returns post and comments data.

    Args:
        post_id: The post ID to mock
        post_data: The post data to return
        comments_data: The comments data to return

    Returns:
        A mock function that can be used to patch urllib.request.urlopen
    """
    def urlopen_side_effect(url, timeout=None):
        mock_response = Mock()

        if f'/posts/{post_id}' in url and not url.endswith('/comments'):
            # Return post data
            mock_response.read.return_value = json.dumps(post_data).encode('utf-8')
        elif f'/posts/{post_id}/comments' in url:
            # Return comments data
            mock_response.read.return_value = json.dumps(comments_data).encode('utf-8')
        else:
            raise Exception(f"Unexpected URL: {url}")

        mock_response.__enter__ = Mock(return_value=mock_response)
        mock_response.__exit__ = Mock(return_value=False)

        return mock_response

    return urlopen_side_effect


def get_sample_post(post_id=1):
    """Returns sample post data"""
    return {
        'userId': 1,
        'id': post_id,
        'title': 'Sample Post Title',
        'body': 'This is the body of the sample post.'
    }


def get_sample_comments(post_id=1, count=3):
    """Returns sample comments data"""
    return [
        {
            'postId': post_id,
            'id': i,
            'name': f'Comment {i}',
            'email': f'user{i}@example.com',
            'body': f'This is comment {i}'
        }
        for i in range(1, count + 1)
    ]
