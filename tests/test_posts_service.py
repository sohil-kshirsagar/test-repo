import pytest
from unittest.mock import patch, Mock
import urllib.error
from utils.posts_service import get_post_with_comments, format_post_header
from tests.mocks.jsonplaceholder_mocks import mock_post_response, mock_comments_response


class TestGetPostWithComments:
    """Tests for get_post_with_comments function"""

    @patch('urllib.request.urlopen')
    def test_get_post_with_comments_valid_post(self, mock_urlopen):
        """Test fetching a post with comments successfully"""
        post_id = 1

        # Setup mock to return post data first, then comments data
        mock_urlopen.side_effect = [
            mock_post_response(post_id),
            mock_comments_response(post_id, num_comments=3)
        ]

        result = get_post_with_comments(post_id)

        # According to docstring, should return dict with 'post' and 'comments' keys
        assert 'post' in result
        assert 'comments' in result
        assert result['post']['id'] == post_id
        assert result['post']['title'] == f'Test Post {post_id}'
        assert len(result['comments']) == 3
        assert result['comment_count'] == 3

    @patch('urllib.request.urlopen')
    def test_get_post_with_comments_no_comments(self, mock_urlopen):
        """Test fetching a post with no comments"""
        post_id = 5

        mock_urlopen.side_effect = [
            mock_post_response(post_id),
            mock_comments_response(post_id, num_comments=0)
        ]

        result = get_post_with_comments(post_id)

        assert result['post']['id'] == post_id
        assert len(result['comments']) == 0
        assert result['comment_count'] == 0


class TestFormatPostHeader:
    """Tests for format_post_header function"""

    def test_format_post_header_basic(self):
        """Test basic post header formatting"""
        post = {
            'userId': 1,
            'id': 42,
            'title': 'Test Post Title',
            'body': 'Post body content'
        }

        # According to docstring: "Formats header of a post, {title} ({id})"
        result = format_post_header(post)
        assert result == "Test Post Title (42)"

    def test_format_post_header_special_characters(self):
        """Test post header with special characters in title"""
        post = {
            'userId': 1,
            'id': 10,
            'title': 'Post with "quotes" & special chars!',
            'body': 'Body'
        }

        result = format_post_header(post)
        assert result == 'Post with "quotes" & special chars! (10)'
