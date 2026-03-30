#!/bin/bash
#
# Creates a PR designed to test Tusk's lint error auto-fix iteration.
#
# Adds utility functions with patterns that reliably produce lint errors
# when tests are generated, even when Claude Code tries to follow lint rules.
#
# Usage: ./create-lint-test-pr.sh [--disable-pr-creation]
#
# Prerequisites:
#   - Testing sandbox config must have a lint script configured
#   - Recommended lint script (update via DB):
#     export PYTHONPATH=/home/user/repo && black --check {{file}} && isort --check-only {{file}} && pylint {{file}} --disable=C0114,C0115,C0116 --max-line-length=79 --max-args=3 --max-locals=8
#

set -e

DISABLE_PR_CREATION=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --disable-pr-creation)
            DISABLE_PR_CREATION=true
            shift
            ;;
        --help)
            echo "Usage: $0 [--disable-pr-creation]"
            echo ""
            echo "Creates a PR with utility functions designed to trigger lint errors"
            echo "during Tusk test generation, to test the lint error auto-fix feature."
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Ensure we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [[ "$CURRENT_BRANCH" != "main" ]]; then
    echo "Error: Must be on main branch. Currently on: $CURRENT_BRANCH"
    exit 1
fi

TIMESTAMP=$(date +%s)
BRANCH_NAME="lint-test-${TIMESTAMP}/data-processing"

echo "Creating lint test PR on branch: $BRANCH_NAME"

git checkout -b "$BRANCH_NAME"

mkdir -p utils

# This module has functions that are complex enough to generate tests with:
# - Many local variables (violates max-locals=8)
# - Functions with 4+ args (violates max-args=3)
# - Long assertion lines (violates max-line-length=79)
# - Private helpers that need source file changes to test
cat > utils/data_processor.py << 'EOF'
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
EOF

git add utils/data_processor.py
git commit -m "feat: add data processing utilities with validation"
git push -u origin "$BRANCH_NAME"

if [[ "$DISABLE_PR_CREATION" == false ]]; then
    gh pr create --title "Add data processing utilities" --body "$(cat << 'PREOF'
## Summary
- Adds `utils/data_processor.py` with data processing, aggregation, and transformation functions
- Includes private validation helpers (`_sanitize_string`, `_clamp_value`)

## Why this exists
This PR is designed to test Tusk's **lint error auto-fix iteration** feature. The code is intentionally structured to produce lint errors in generated tests:

- `process_user_record` has 6 parameters → tests will have many locals and long assertion lines
- `aggregate_records` has 4 parameters → parameterized tests will exceed `max-args`
- `_sanitize_string` and `_clamp_value` are private → tests need source file modifications to access them
- Complex return dicts → assertion lines will exceed 79 chars

### Expected behavior with lint iteration enabled
1. Claude Code generates tests → some fail pylint (`max-args`, `max-locals`, `line-too-long`)
2. Lint iteration calls Claude Code to fix the errors (up to 2 attempts)
3. Collateral changes (e.g. making private helpers public) are detected and classified
4. Tests are re-run after fixes to ensure no regressions
PREOF
)" --base main

    gh pr view --web
    git checkout main

    echo ""
    echo "PR created successfully!"
    echo "Branch: $BRANCH_NAME"
else
    echo ""
    echo "PR creation disabled. Branch: $BRANCH_NAME"
fi
