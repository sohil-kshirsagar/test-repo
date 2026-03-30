"""Text formatting utilities with private helpers."""


def _normalize_whitespace(text):
    """Private: collapse multiple spaces/tabs/newlines into single spaces."""
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")
    import re
    return re.sub(r'\s+', ' ', text).strip()


def _truncate_with_ellipsis(text, max_length):
    """Private: truncate text and add ellipsis if too long."""
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")
    if not isinstance(max_length, int) or max_length < 4:
        raise ValueError("max_length must be an integer >= 4")
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def _extract_initials(name):
    """Private: extract initials from a full name."""
    if not isinstance(name, str):
        raise TypeError(f"Expected string, got {type(name).__name__}")
    parts = name.strip().split()
    if not parts:
        raise ValueError("Name cannot be empty")
    return "".join(p[0].upper() for p in parts if p)


def format_display_name(first_name, last_name, max_length=20):
    """Format a display name from first and last name.

    Uses private helpers for normalization, truncation, and initials.

    Returns a dict with formatted name variants.
    """
    clean_first = _normalize_whitespace(first_name)
    clean_last = _normalize_whitespace(last_name)
    full_name = f"{clean_first} {clean_last}"

    return {
        "full": _truncate_with_ellipsis(full_name, max_length),
        "initials": _extract_initials(full_name),
        "first_initial_last": f"{clean_first[0].upper()}. {clean_last}",
        "last_first": f"{clean_last}, {clean_first}",
    }
