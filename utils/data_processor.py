"""Data processing utilities with validation and transformation."""


def _sanitize_string(value):
    """Private helper to clean string inputs."""
    if not isinstance(value, str):
        raise TypeError(f"Expected string, got {type(value).__name__}")
    return value.strip().lower()


def _clamp_value(value, min_val, max_val):
    """Private helper to clamp a numeric value within bounds."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected number, got {type(value).__name__}")
    return max(min_val, min(max_val, value))


def process_user_record(name, email, age, country, role="user", is_active=True):
    """Process a user record with validation and normalization.

    Args:
        name: User's full name
        email: User's email address
        age: User's age (must be 0-150)
        country: Two-letter country code
        role: User role (default: "user")
        is_active: Whether user is active (default: True)

    Returns:
        dict with normalized user data

    Raises:
        TypeError: If inputs have wrong types
        ValueError: If inputs fail validation
    """
    clean_name = _sanitize_string(name)
    clean_email = _sanitize_string(email)
    clean_country = _sanitize_string(country)

    if "@" not in clean_email:
        raise ValueError(f"Invalid email format: {email}")

    if len(clean_country) != 2:
        raise ValueError(f"Country code must be 2 characters: {country}")

    clamped_age = _clamp_value(age, 0, 150)
    if clamped_age != age:
        raise ValueError(f"Age out of range (0-150): {age}")

    username = clean_email.split("@")[0]
    domain = clean_email.split("@")[1]
    is_corporate = domain not in ("gmail.com", "yahoo.com", "hotmail.com", "outlook.com")

    return {
        "name": clean_name,
        "email": clean_email,
        "username": username,
        "domain": domain,
        "age": age,
        "country": clean_country,
        "role": role.lower(),
        "is_active": is_active,
        "is_corporate": is_corporate,
        "display_name": f"{clean_name} ({username})",
    }


def aggregate_records(records, group_by_field, value_field, operation="sum"):
    """Aggregate a list of records by a field.

    Args:
        records: List of dicts to aggregate
        group_by_field: Field name to group by
        value_field: Field name containing values to aggregate
        operation: One of "sum", "avg", "count", "min", "max"

    Returns:
        dict mapping group keys to aggregated values

    Raises:
        ValueError: If operation is invalid or fields are missing
    """
    valid_operations = ("sum", "avg", "count", "min", "max")
    if operation not in valid_operations:
        raise ValueError(
            f"Invalid operation '{operation}'. Must be one of: {', '.join(valid_operations)}"
        )

    groups = {}
    for record in records:
        if group_by_field not in record:
            raise ValueError(f"Record missing field: {group_by_field}")
        if value_field not in record and operation != "count":
            raise ValueError(f"Record missing field: {value_field}")

        key = record[group_by_field]
        if key not in groups:
            groups[key] = []

        if operation == "count":
            groups[key].append(1)
        else:
            groups[key].append(record[value_field])

    result = {}
    for key, values in groups.items():
        if operation == "sum":
            result[key] = sum(values)
        elif operation == "avg":
            result[key] = sum(values) / len(values) if values else 0
        elif operation == "count":
            result[key] = len(values)
        elif operation == "min":
            result[key] = min(values)
        elif operation == "max":
            result[key] = max(values)

    return result


def transform_nested_data(data, key_path, transform_fn):
    """Apply a transformation to nested dict values at a given key path.

    Args:
        data: Input dict (possibly nested)
        key_path: Dot-separated path to the target field (e.g. "user.address.city")
        transform_fn: Function to apply to the value

    Returns:
        New dict with the transformation applied (original unchanged)

    Raises:
        KeyError: If key path doesn't exist in data
        TypeError: If data is not a dict
    """
    if not isinstance(data, dict):
        raise TypeError(f"Expected dict, got {type(data).__name__}")

    keys = key_path.split(".")
    result = dict(data)  # shallow copy

    current = result
    for i, key in enumerate(keys[:-1]):
        if key not in current:
            raise KeyError(f"Key '{key}' not found at path level {i}")
        if not isinstance(current[key], dict):
            raise TypeError(
                f"Expected dict at '{key}' (path level {i}), got {type(current[key]).__name__}"
            )
        current[key] = dict(current[key])  # shallow copy each level
        current = current[key]

    final_key = keys[-1]
    if final_key not in current:
        raise KeyError(f"Final key '{final_key}' not found in data")

    current[final_key] = transform_fn(current[final_key])
    return result
