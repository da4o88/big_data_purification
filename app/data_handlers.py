import re


def name_upper_case(text):
    """
    Capitalize words in string names
    :param text:
    :return: string
    """

    temp_text = text.split(' ')
    name = []
    for word in temp_text:
        word = word.lower()
        word = word.capitalize()

        if '&' in word:
            word = word.upper()

        if '.' in word:
            word = word.upper()

        name.append(word)
    name = ' '.join(name)
    return name


def clean_company_name(company_name):
    """
    Clean company name from unnecessary words like ('LIMITED', 'LTD.', 'LTD') etc.
    :param company_name:
    :return: string
    """

    strings_forbidden = ['LIMITED', 'LTD.', 'LTD', 'ltd.', 'Limited', 'limited', 'Ltd', 'Ltd.']
    text = company_name

    # Remove text after ","
    if ',' in text:
        text = text.split(',')
        text = text[0]

    if '(' in text:
        # Pattern to remove everything between ()
        pattern = r"[\(].*?[\)]"
        matches = re.findall(pattern, text)

        for i in matches:
            text = text.replace(i, '')

    # Remove word like "LTD", "LTD.", "Limited" etc.
    for j in strings_forbidden:
        text = text.replace(j, '')

    if '"' in text:
        for ch in text:
            if ch == '"':
                text = text.replace(ch, '')

    # Remove hyphen character from string
    if '-' in text:
        temp_text = ""
        temp_index = 0
        text_length = len(text)
        for i in range(text_length):
            if text[i] == '-':
                if 0 < i < text_length - 1:
                    if text[i - 1] != ' ' and text[i + 1] != ' ':
                        continue
                temp_text += text[temp_index + 1:i]
                temp_index = i
        text = temp_text

    # Remove blank spaces
    text = text.strip()

    # Capitalize word in name
    name = name_upper_case(text)

    return name
