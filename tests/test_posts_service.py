from utils.posts_service import format_post_header


class TestFormatPostHeader:
    """Tests for format_post_header function"""

    def test_format_post_header_basic(self):
        """Test basic post header formatting"""
        post = {
            'userId': 1,
            'id': 123,
            'title': 'My Test Post',
            'body': 'Post body content'
        }

        result = format_post_header(post)
        assert result == "My Test Post (123)"

    def test_format_post_header_with_special_characters(self):
        """Test post header formatting with special characters in title"""
        post = {
            'userId': 1,
            'id': 456,
            'title': 'Post with "quotes" and (parentheses)',
            'body': 'Post body'
        }

        result = format_post_header(post)
        assert result == 'Post with "quotes" and (parentheses) (456)'

    def test_format_post_header_empty_title(self):
        """Test post header formatting with empty title"""
        post = {
            'userId': 1,
            'id': 789,
            'title': '',
            'body': 'Post body'
        }

        result = format_post_header(post)
        assert result == " (789)"
