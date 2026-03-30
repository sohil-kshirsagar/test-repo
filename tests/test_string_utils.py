from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_none():
    """Test None value - docstring says should return empty string"""
    # According to docstring: "If string is None, return empty string"
    # This test will FAIL because the implementation doesn't handle None
    # This is a BUG in the implementation
    assert capitalize_first_letter(None) == ""
