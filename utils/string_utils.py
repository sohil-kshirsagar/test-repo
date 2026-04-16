def capitalize_first_letter(string):
    """
    Capitalize the first letter of a string
    If string is None, return empty string
    Otherwise, return the string with the first letter capitalized
    """
    if string is None:
        return ""
    if len(string) == 0:
        return ""
    return string[0].upper() + string[1:]

