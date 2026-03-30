"""
Mocks for JSONPlaceholder API responses
"""
import json
from unittest.mock import MagicMock


def mock_urlopen_for_post_with_comments(post_id, post_data=None, comments_data=None):
    """
    Creates a mock for urllib.request.urlopen that returns appropriate responses
    for the get_post_with_comments function.

    Args:
        post_id: The post ID to mock
        post_data: Optional custom post data dict
        comments_data: Optional custom comments data list

    Returns:
        A mock function that can be used to patch urllib.request.urlopen
    """
    if post_data is None:
        post_data = {
            'userId': 1,
            'id': post_id,
            'title': f'Test Post {post_id}',
            'body': 'Test post body'
        }

    if comments_data is None:
        comments_data = [
            {
                'postId': post_id,
                'id': 1,
                'name': 'Test Comment 1',
                'email': 'test1@example.com',
                'body': 'Comment body 1'
            },
            {
                'postId': post_id,
                'id': 2,
                'name': 'Test Comment 2',
                'email': 'test2@example.com',
                'body': 'Comment body 2'
            }
        ]

    def mock_urlopen(url, timeout=None):
        """Mock urlopen that returns appropriate data based on URL"""
        mock_response = MagicMock()

        if url.endswith(f'/posts/{post_id}'):
            # Return post data
            mock_response.read.return_value = json.dumps(post_data).encode('utf-8')
        elif url.endswith(f'/posts/{post_id}/comments'):
            # Return comments data
            mock_response.read.return_value = json.dumps(comments_data).encode('utf-8')
        else:
            raise ValueError(f"Unexpected URL: {url}")

        mock_response.__enter__ = lambda self: self
        mock_response.__exit__ = lambda self, *args: None

        return mock_response

    return mock_urlopen
