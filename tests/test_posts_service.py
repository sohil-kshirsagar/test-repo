"""
Unit tests for posts_service module
"""
import pytest
from unittest.mock import patch

from utils.posts_service import get_post_with_comments
from tests.mocks.jsonplaceholder_mocks import (
    mock_urlopen_for_post,
    get_sample_post,
    get_sample_comments
)


class TestGetPostWithComments:
    """Tests for get_post_with_comments function"""

    def test_get_post_with_comments_success(self):
        """Test successful fetch of post with comments"""
        post_id = 1
        post_data = get_sample_post(post_id)
        comments_data = get_sample_comments(post_id, count=5)

        with patch('urllib.request.urlopen', side_effect=mock_urlopen_for_post(post_id, post_data, comments_data)):
            result = get_post_with_comments(post_id)

        assert result['post'] == post_data
        assert result['comments'] == comments_data
        assert result['comment_count'] == 5

    def test_get_post_with_comments_no_comments(self):
        """Test fetch when post has no comments"""
        post_id = 2
        post_data = get_sample_post(post_id)
        comments_data = []

        with patch('urllib.request.urlopen', side_effect=mock_urlopen_for_post(post_id, post_data, comments_data)):
            result = get_post_with_comments(post_id)

        assert result['post'] == post_data
        assert result['comments'] == []
        assert result['comment_count'] == 0

    def test_get_post_with_comments_invalid_post_id_negative(self):
        """Test that negative post_id raises ValueError"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(-1)

    def test_get_post_with_comments_invalid_post_id_zero(self):
        """Test that zero post_id raises ValueError"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments(0)

    def test_get_post_with_comments_invalid_post_id_string(self):
        """Test that string post_id raises ValueError"""
        with pytest.raises(ValueError, match="post_id must be a positive integer"):
            get_post_with_comments("1")
