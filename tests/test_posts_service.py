"""
Tests for posts_service module
"""
import pytest
from unittest.mock import patch, Mock
from utils.posts_service import format_post_header, get_post_with_comments
from tests.mocks.jsonplaceholder_mocks import mock_urlopen, create_mock_post, create_mock_comments


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
        result = format_post_header(post)
        assert result == "Test Post Title (42)"

    def test_format_post_header_with_special_characters(self):
        """Test post header with special characters in title"""
        post = {
            'userId': 1,
            'id': 100,
            'title': 'Post with "quotes" & symbols!',
            'body': 'Body'
        }
        result = format_post_header(post)
        assert result == 'Post with "quotes" & symbols! (100)'

    def test_format_post_header_missing_title(self):
        """Test post with missing title key"""
        post = {
            'userId': 1,
            'id': 5,
            'body': 'Body'
        }
        # Should raise KeyError since title is required per docstring
        with pytest.raises(KeyError):
            format_post_header(post)

    def test_format_post_header_missing_id(self):
        """Test post with missing id key"""
        post = {
            'userId': 1,
            'title': 'Title',
            'body': 'Body'
        }
        # Should raise KeyError since id is required per docstring
        with pytest.raises(KeyError):
            format_post_header(post)

    def test_format_post_header_empty_title(self):
        """Test post with empty title"""
        post = {
            'userId': 1,
            'id': 7,
            'title': '',
            'body': 'Body'
        }
        result = format_post_header(post)
        assert result == " (7)"


class TestGetPostWithComments:
    """Tests for get_post_with_comments function"""

    @patch('urllib.request.urlopen', side_effect=mock_urlopen)
    def test_get_post_with_comments_valid_id(self, mock_url):
        """Test fetching post with comments for valid post_id"""
        result = get_post_with_comments(1)

        assert 'post' in result
        assert 'comments' in result
        assert 'comment_count' in result
        assert result['post']['id'] == 1
        assert result['comment_count'] == len(result['comments'])

    @patch('urllib.request.urlopen', side_effect=mock_urlopen)
    def test_get_post_with_comments_different_id(self, mock_url):
        """Test fetching different post IDs"""
        result = get_post_with_comments(5)

        assert result['post']['id'] == 5
        assert isinstance(result['comments'], list)
        assert result['comment_count'] == len(result['comments'])

    def test_get_post_with_comments_invalid_id_zero(self):
        """Test with post_id of 0 (invalid per docstring)"""
        # Per docstring: "Raises ValueError: If post_id is invalid"
        # post_id must be a positive integer
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(0)

    def test_get_post_with_comments_invalid_id_negative(self):
        """Test with negative post_id (invalid per docstring)"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(-1)

    def test_get_post_with_comments_invalid_id_string(self):
        """Test with string post_id (invalid per docstring)"""
        # Per docstring: post_id must be a positive integer
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments("1")

    def test_get_post_with_comments_invalid_id_float(self):
        """Test with float post_id (invalid per docstring)"""
        # Per docstring: post_id must be an integer
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(1.5)

    def test_get_post_with_comments_invalid_id_none(self):
        """Test with None post_id (invalid per docstring)"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(None)
