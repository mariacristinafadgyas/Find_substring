def find_substring(text, substring):
    """
    Function to find occurrences of a substring in a given text.

    Args:
        text (str): The text in which to search for the substring.
        substring (str): The substring to search for in the text.

    Returns:
        list: A list containing the indices of the occurrences of the substring in the text.
    """
    indices = []
    len_substring = len(substring)
    len_text = len(text)

    for i in range(len_text - len_substring + 1):
        if text[i:i + len_substring] == substring:
            indices.append(i)

    return indices


def test_find_substring():

    try:
        find_substring(123, "test")
    except TypeError as e:
        assert str(e) == "Both string and substring should be strings", "Test for wrong input failed"


    try:
        find_substring("test string", "")
    except ValueError as e:
        assert str(e) == "Substring cannot be empty", "Test for an empty string failed"


    assert find_substring("test string test", "test") == [0, 12], "Additional test failed"


def main():
    find_substring("test string test", "test")
    test_find_substring()


if __name__ == "__main__":
    main()