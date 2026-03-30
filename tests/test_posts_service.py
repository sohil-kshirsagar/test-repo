import pytest
from unittest.mock import patch
from utils.posts_service import format_post_header, get_post_with_comments
from tests.mocks.jsonplaceholder_mocks import (
    mock_urlopen_for_post,
    mock_urlopen_for_comments
)


class TestFormatPostHeader:
    """Tests for format_post_header function"""

    def test_format_post_header_basic(self):
        """Test basic formatting of post header"""
        post = {
            'userId': 1,
            'id': 42,
            'title': 'My Great Post',
            'body': 'This is the body'
        }
        assert format_post_header(post) == "My Great Post (42)"


class TestGetPostWithComments:
    """Tests for get_post_with_comments function"""

    def test_get_post_with_comments_valid_id(self):
        """Test fetching post with valid ID"""
        with patch('urllib.request.urlopen') as mock_urlopen:
            # Set up mock to return post then comments
            mock_urlopen.side_effect = [
                mock_urlopen_for_post(1),
                mock_urlopen_for_comments(1)
            ]

            result = get_post_with_comments(1)

            # Verify structure and content
            assert 'post' in result
            assert 'comments' in result
            assert 'comment_count' in result
            assert result['post']['id'] == 1
            assert result['post']['title'] == 'Sample Post 1'
            assert len(result['comments']) == 2
            assert result['comment_count'] == 2

    def test_get_post_with_comments_invalid_id_negative(self):
        """Test that negative post_id raises ValueError per docstring"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(-1)

    def test_get_post_with_comments_invalid_id_zero(self):
        """Test that zero post_id raises ValueError per docstring"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(0)

    def test_get_post_with_comments_invalid_id_string(self):
        """Test that string post_id raises ValueError per docstring"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments("1")
