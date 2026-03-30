"""
Mocks for JSONPlaceholder API requests
"""
import json
from unittest.mock import Mock


def mock_post_response(post_id):
    """Creates a mock response for a post request"""
    mock_response = Mock()
    post_data = {
        'userId': 1,
        'id': post_id,
        'title': f'Test Post {post_id}',
        'body': f'This is the body of test post {post_id}'
    }
    mock_response.read.return_value = json.dumps(post_data).encode('utf-8')
    mock_response.__enter__ = Mock(return_value=mock_response)
    mock_response.__exit__ = Mock(return_value=False)
    return mock_response


def mock_comments_response(post_id, num_comments=3):
    """Creates a mock response for comments request"""
    mock_response = Mock()
    comments_data = []
    for i in range(1, num_comments + 1):
        comments_data.append({
            'postId': post_id,
            'id': i,
            'name': f'Comment {i}',
            'email': f'commenter{i}@example.com',
            'body': f'This is comment {i} body'
        })
    mock_response.read.return_value = json.dumps(comments_data).encode('utf-8')
    mock_response.__enter__ = Mock(return_value=mock_response)
    mock_response.__exit__ = Mock(return_value=False)
    return mock_response
