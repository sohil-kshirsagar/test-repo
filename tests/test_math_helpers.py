"""Tests for math helper utilities."""

import pytest

from utils.math_helpers import (
    check_non_negative,
    check_positive,
    normalize_scores,
    percentage_change,
    weighted_average,
)


class TestCheckPositive:
    """Tests for check_positive function."""

    def test_check_positive_valid_int(self):
        """Test with valid positive integer."""
        assert check_positive(5) == 5

    def test_check_positive_valid_float(self):
        """Test with valid positive float."""
        assert check_positive(3.14) == 3.14

    def test_check_positive_zero_should_raise(self):
        """Test that zero raises ValueError (boundary case)."""
        with pytest.raises(ValueError, match="Value must be positive"):
            check_positive(0)

    def test_check_positive_negative_should_raise(self):
        """Test that negative value raises ValueError."""
        with pytest.raises(ValueError, match="Value must be positive"):
            check_positive(-5)

    def test_check_positive_string_should_raise(self):
        """Test that string raises TypeError."""
        with pytest.raises(TypeError, match="Expected number, got str"):
            check_positive("5")

    def test_check_positive_none_should_raise(self):
        """Test that None raises TypeError."""
        with pytest.raises(TypeError, match="Expected number, got NoneType"):
            check_positive(None)

    def test_check_positive_very_small_positive(self):
        """Test with very small positive number."""
        assert check_positive(1e-10) == 1e-10


class TestCheckNonNegative:
    """Tests for check_non_negative function."""

    def test_check_non_negative_valid_positive(self):
        """Test with valid positive value."""
        assert check_non_negative(5) == 5

    def test_check_non_negative_zero(self):
        """Test that zero is allowed (boundary case)."""
        assert check_non_negative(0) == 0

    def test_check_non_negative_negative_should_raise(self):
        """Test that negative value raises ValueError."""
        with pytest.raises(ValueError, match="Value must be non-negative"):
            check_non_negative(-1)

    def test_check_non_negative_string_should_raise(self):
        """Test that string raises TypeError."""
        with pytest.raises(TypeError, match="Expected number, got str"):
            check_non_negative("0")

    def test_check_non_negative_none_should_raise(self):
        """Test that None raises TypeError."""
        with pytest.raises(TypeError, match="Expected number, got NoneType"):
            check_non_negative(None)


class TestWeightedAverage:
    """Tests for weighted_average function."""

    def test_weighted_average_simple(self):
        """Test basic weighted average calculation."""
        result = weighted_average([10, 20, 30], [1, 1, 1])
        assert result == 20.0

    def test_weighted_average_different_weights(self):
        """Test weighted average with different weights."""
        result = weighted_average([10, 20], [1, 3])
        assert result == 17.5

    def test_weighted_average_empty_values(self):
        """Test that empty values raises ValueError."""
        match_str = "Values and weights cannot be empty"
        with pytest.raises(ValueError, match=match_str):
            weighted_average([], [1, 2])

    def test_weighted_average_empty_weights(self):
        """Test that empty weights raises ValueError."""
        match_str = "Values and weights cannot be empty"
        with pytest.raises(ValueError, match=match_str):
            weighted_average([1, 2], [])

    def test_weighted_average_length_mismatch(self):
        """Test that mismatched lengths raises ValueError."""
        with pytest.raises(ValueError, match="must have same length"):
            weighted_average([1, 2, 3], [1, 2])

    def test_weighted_average_zero_weight_should_raise(self):
        """Test that zero weight raises ValueError (calls check_positive)."""
        with pytest.raises(ValueError, match="Value must be positive"):
            weighted_average([10, 20], [1, 0])

    def test_weighted_average_negative_weight_should_raise(self):
        """Test that negative weight raises ValueError."""
        with pytest.raises(ValueError, match="Value must be positive"):
            weighted_average([10, 20], [1, -1])

    def test_weighted_average_invalid_weight_type(self):
        """Test that invalid weight type raises TypeError."""
        with pytest.raises(TypeError, match="Expected number"):
            weighted_average([10, 20], [1, "2"])

    def test_weighted_average_single_value(self):
        """Test with single value and weight."""
        result = weighted_average([42], [5])
        assert result == 42

    def test_weighted_average_with_negative_values(self):
        """Test that negative values are allowed."""
        result = weighted_average([-10, 10], [1, 1])
        assert result == 0.0


class TestPercentageChange:
    """Tests for percentage_change function."""

    def test_percentage_change_increase(self):
        """Test basic percentage increase."""
        result = percentage_change(100, 150)
        assert result == 0.5

    def test_percentage_change_decrease(self):
        """Test percentage decrease."""
        result = percentage_change(100, 50)
        assert result == -0.5

    def test_percentage_change_no_change(self):
        """Test no change (new_value equals old_value)."""
        result = percentage_change(100, 100)
        assert result == 0.0

    def test_percentage_change_to_zero(self):
        """Test change to zero (100% decrease)."""
        result = percentage_change(100, 0)
        assert result == -1.0

    def test_percentage_change_old_value_zero_should_raise(self):
        """Test that zero old_value raises ValueError."""
        with pytest.raises(ValueError, match="Value must be positive"):
            percentage_change(0, 100)

    def test_percentage_change_old_value_negative_should_raise(self):
        """Test that negative old_value raises ValueError."""
        with pytest.raises(ValueError, match="Value must be positive"):
            percentage_change(-100, 50)

    def test_percentage_change_new_value_negative_should_raise(self):
        """Test that negative new_value raises ValueError."""
        with pytest.raises(ValueError, match="Value must be non-negative"):
            percentage_change(100, -50)

    def test_percentage_change_old_value_invalid_type(self):
        """Test that invalid old_value type raises TypeError."""
        with pytest.raises(TypeError, match="Expected number"):
            percentage_change("100", 50)

    def test_percentage_change_new_value_invalid_type(self):
        """Test that invalid new_value type raises TypeError."""
        with pytest.raises(TypeError, match="Expected number"):
            percentage_change(100, "50")


class TestNormalizeScores:
    """Tests for normalize_scores function."""

    def test_normalize_scores_basic(self):
        """Test basic normalization to [0, 1]."""
        result = normalize_scores([0, 50, 100])
        assert result == [0.0, 0.5, 1.0]

    def test_normalize_scores_custom_range(self):
        """Test normalization to custom range."""
        result = normalize_scores([0, 50, 100], target_min=10, target_max=20)
        assert result == [10.0, 15.0, 20.0]

    def test_normalize_scores_all_same(self):
        """Test with all identical scores (boundary case)."""
        result = normalize_scores([5, 5, 5])
        assert result == [0.5, 0.5, 0.5]

    def test_normalize_scores_all_same_custom_range(self):
        """Test with all identical scores in custom range."""
        result = normalize_scores([10, 10, 10], target_min=0, target_max=100)
        assert result == [50.0, 50.0, 50.0]

    def test_normalize_scores_single_score(self):
        """Test with single score."""
        result = normalize_scores([42])
        assert result == [0.5]

    def test_normalize_scores_empty_should_raise(self):
        """Test that empty scores raises ValueError."""
        with pytest.raises(ValueError, match="Scores cannot be empty"):
            normalize_scores([])

    def test_normalize_scores_target_min_equals_max_should_raise(self):
        """Test that target_min == target_max raises ValueError."""
        match_str = "target_min must be less than target_max"
        with pytest.raises(ValueError, match=match_str):
            normalize_scores([1, 2, 3], target_min=5, target_max=5)

    def test_normalize_scores_target_min_greater_than_max_should_raise(self):
        """Test that target_min > target_max raises ValueError."""
        match_str = "target_min must be less than target_max"
        with pytest.raises(ValueError, match=match_str):
            normalize_scores([1, 2, 3], target_min=10, target_max=5)

    def test_normalize_scores_negative_scores(self):
        """Test with negative scores."""
        result = normalize_scores([-10, 0, 10])
        assert result == [0.0, 0.5, 1.0]

    def test_normalize_scores_two_values(self):
        """Test with exactly two values (boundary case)."""
        result = normalize_scores([10, 20])
        assert result == [0.0, 1.0]
