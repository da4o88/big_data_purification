import re
# from cleanco import basename


def name_upper_case(text):
    """Capitalize words in string names"""

    temp_text = text.split(' ')
    name = []
    for word in temp_text:
        word = word.lower()
        word = word.capitalize()

        if '&' in word:
            word = word.upper()

        name.append(word)
    name = ' '.join(name)
    return name


def clean_company_name(company_name):
    strings_forbidden = ['LIMITED', 'LTD.', 'LTD', 'ltd.', 'Limited', 'limited']
    text = company_name

    # text = ' This -is - sentence. (of course is not legal) to - "doubt" me-, in this time-line-. But (response of
    # the http is not posible) now, '
    pattern = r"[\(].*?[\)]"
    matches = re.findall(pattern, text)

    if ',' in text:
        text = text.split(',')
        text = text[0]

    if '(' in text:
        for i in matches:
            text = text.replace(i, '')

    for j in strings_forbidden:
        text = text.replace(j, '')

    #  "" i  - uslov za proverka, konsultacija
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

    name = name_upper_case(text)

    # Not work error terms missing pos.args
    # name = "Some Big Pharma, LLC"
    # name = basename(name)

    return name
