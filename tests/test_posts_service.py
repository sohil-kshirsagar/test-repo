import pytest
from unittest.mock import patch
from utils.posts_service import format_post_header, get_post_with_comments
from tests.mocks.jsonplaceholder_mocks import mock_urlopen_for_post_with_comments


class TestFormatPostHeader:
    """Tests for format_post_header function"""

    def test_format_post_header_normal_post(self):
        """Test formatting a normal post with all required fields"""
        post = {
            'userId': 1,
            'id': 42,
            'title': 'Test Post Title',
            'body': 'Test post body'
        }
        assert format_post_header(post) == "Test Post Title (42)"

    def test_format_post_header_with_special_characters(self):
        """Test formatting a post title with special characters"""
        post = {
            'userId': 1,
            'id': 1,
            'title': 'Post with "quotes" and & symbols!',
            'body': 'Body text'
        }
        assert format_post_header(post) == 'Post with "quotes" and & symbols! (1)'

    def test_format_post_header_with_unicode(self):
        """Test formatting a post title with unicode characters"""
        post = {
            'userId': 1,
            'id': 5,
            'title': 'Post with émojis 🎉 and ünïcödé',
            'body': 'Body text'
        }
        assert format_post_header(post) == 'Post with émojis 🎉 and ünïcödé (5)'


class TestGetPostWithComments:
    """Tests for get_post_with_comments function"""

    @patch('urllib.request.urlopen')
    def test_get_post_with_comments_valid_id(self, mock_urlopen):
        """Test fetching post with comments for a valid post ID"""
        post_id = 1
        mock_urlopen.side_effect = mock_urlopen_for_post_with_comments(post_id)

        result = get_post_with_comments(post_id)

        assert 'post' in result
        assert 'comments' in result
        assert 'comment_count' in result
        assert result['post']['id'] == post_id
        assert result['comment_count'] == len(result['comments'])
        assert result['comment_count'] == 2

    @patch('urllib.request.urlopen')
    def test_get_post_with_comments_no_comments(self, mock_urlopen):
        """Test fetching post that has no comments"""
        post_id = 99
        mock_urlopen.side_effect = mock_urlopen_for_post_with_comments(
            post_id,
            comments_data=[]
        )

        result = get_post_with_comments(post_id)

        assert result['comment_count'] == 0
        assert result['comments'] == []

    def test_get_post_with_comments_invalid_id_string(self):
        """Test that string post_id raises ValueError"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments("1")

    def test_get_post_with_comments_invalid_id_zero(self):
        """Test that post_id of 0 raises ValueError"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(0)

    def test_get_post_with_comments_invalid_id_negative(self):
        """Test that negative post_id raises ValueError"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(-1)
