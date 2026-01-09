"""
Mocks for JSONPlaceholder API
"""
import json
from unittest.mock import Mock


def create_mock_post(post_id=1, user_id=1, title="Test Post", body="Test body"):
    """Create a mock post response"""
    return {
        'userId': user_id,
        'id': post_id,
        'title': title,
        'body': body
    }


def create_mock_comments(post_id=1, count=3):
    """Create mock comments response"""
    comments = []
    for i in range(1, count + 1):
        comments.append({
            'postId': post_id,
            'id': i,
            'name': f'Comment {i}',
            'email': f'user{i}@example.com',
            'body': f'This is comment {i}'
        })
    return comments


def mock_urlopen(url, timeout=None):
    """Mock urllib.request.urlopen for JSONPlaceholder API calls"""
    mock_response = Mock()

    if '/posts/' in url and '/comments' in url:
        # Comments endpoint
        post_id = int(url.split('/posts/')[1].split('/comments')[0])
        comments = create_mock_comments(post_id=post_id)
        mock_response.read.return_value = json.dumps(comments).encode('utf-8')
    elif '/posts/' in url:
        # Post endpoint
        post_id = int(url.split('/posts/')[1])
        post = create_mock_post(post_id=post_id)
        mock_response.read.return_value = json.dumps(post).encode('utf-8')

    mock_response.__enter__ = Mock(return_value=mock_response)
    mock_response.__exit__ = Mock(return_value=False)

    return mock_response
