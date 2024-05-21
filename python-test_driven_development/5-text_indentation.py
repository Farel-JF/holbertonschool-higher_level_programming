#!/usr/bin/python3
def text_indentation(text):
    """Prints text with 2 new lines after each of these characters: ., ?, and :

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.','?',':']
    result = ""
    i = 0
    lenght = len(text)

    while i < lenght:
        result += text[i]
        if text[i] in characters:
            result += "\n\n"
            i += 1
            while i < lenght and text[i] == '':
                i +1
            continue
        i += 1

    print(result.strip())
