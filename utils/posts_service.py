"""
Posts service uses JSONPlaceholder API.
"""
import urllib.request
import json


def get_post_with_comments(post_id):
    """
    Fetches a post and its comments from JSONPlaceholder API.

    Args:
        post_id: The ID of the post to fetch

    Returns:
        dict: Contains 'post' and 'comments' keys with the fetched data

    Raises:
        ValueError: If post_id is invalid
        urllib.error.URLError: If the API request fails

    If writing tests, make sure to create a mock in `tests/mocks/jsonplaceholder.py` to mock:
    - https://jsonplaceholder.typicode.com/posts/{post_id}
    - https://jsonplaceholder.typicode.com/posts/{post_id}/comments

    This mock should be used in unit tests when testing the `get_post_with_comments` function.
    """
    if not isinstance(post_id, int) or post_id < 1:
        raise ValueError("post_id must be a positive integer")

    # Fetch the post
    post_url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    with urllib.request.urlopen(post_url, timeout=5) as response:
        post_data = json.loads(response.read().decode('utf-8'))

    # Fetch the comments for this post
    comments_url = f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments'
    with urllib.request.urlopen(comments_url, timeout=5) as response:
        comments_data = json.loads(response.read().decode('utf-8'))

    return {
        'post': post_data,
        'comments': comments_data,
        'comment_count': len(comments_data)
    }

def format_post_header(post: dict):
    """
    Formats header of a post, {title} ({id})

    Post data is a dictionary with the following keys:
    - userId: int
    - id: int
    - title: str
    - body: str
    """
    return f"{post['title']} ({post['id']})"

