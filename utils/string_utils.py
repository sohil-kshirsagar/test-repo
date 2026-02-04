def capitalize_first_letter(string):
    """
    If string is None, return empty string
    Otherwise, return the string with the first letter capitalized
    """
    if string is None or string == "":
        return ""
    return string[0].upper() + string[1:]

