import re

cjk_regex = re.compile(
    r'[\u4E00-\u9FFF\u3400-\u4DBF\u20000-\u2A6DF'
    r'\u2A700-\u2B73F\u2B740-\u2B81F\u2B820-\u2CEAF'
    r'\u2CEB0-\u2EBEF\uF900-\uFAFF]'
)

def isCJK(string):
    """check whether string contains chinese, japanese, korean charactors

    Args:
        string (str): string to check

    Returns:
        bool: contains cjk or not
    """
    return bool(cjk_regex.search(string))

def getTextIndex(string):
    return "Chinese" if isCJK(string) else "English"