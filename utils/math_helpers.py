"""Math helper utilities with private validation."""


def _check_positive(value):
    """Private: ensure value is a positive number."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected number, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"Value must be positive, got {value}")
    return value


def _check_non_negative(value):
    """Private: ensure value is non-negative."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected number, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"Value must be non-negative, got {value}")
    return value


def weighted_average(values, weights):
    """Calculate weighted average of values.

    Args:
        values: List of numeric values
        weights: List of weights (must be positive, same length as values)

    Returns:
        The weighted average

    Raises:
        ValueError: If inputs are invalid
        TypeError: If inputs have wrong types
    """
    if not values or not weights:
        raise ValueError("Values and weights cannot be empty")
    if len(values) != len(weights):
        raise ValueError(
            f"Values and weights must have same length: {len(values)} vs {len(weights)}"
        )

    validated_weights = [_check_positive(w) for w in weights]
    total_weight = sum(validated_weights)
    return sum(v * w for v, w in zip(values, validated_weights)) / total_weight


def percentage_change(old_value, new_value):
    """Calculate percentage change between two values.

    Args:
        old_value: Original value (must be positive)
        new_value: New value (must be non-negative)

    Returns:
        Percentage change as a float (e.g. 0.5 for 50% increase)
    """
    _check_positive(old_value)
    _check_non_negative(new_value)
    return (new_value - old_value) / old_value


def normalize_scores(scores, target_min=0.0, target_max=1.0):
    """Normalize a list of scores to a target range.

    Args:
        scores: List of numeric scores
        target_min: Minimum of target range (default 0.0)
        target_max: Maximum of target range (default 1.0)

    Returns:
        List of normalized scores
    """
    if not scores:
        raise ValueError("Scores cannot be empty")
    if target_min >= target_max:
        raise ValueError(
            f"target_min must be less than target_max: {target_min} >= {target_max}"
        )

    min_score = min(scores)
    max_score = max(scores)

    if min_score == max_score:
        mid = (target_min + target_max) / 2
        return [mid] * len(scores)

    return [
        target_min + (s - min_score) * (target_max - target_min) / (max_score - min_score)
        for s in scores
    ]
