import string


def alphabet_position(text):
    alpha = list(string.ascii_lowercase)
    d = {item: num + 1 for num, item in enumerate(alpha)}
    new_string = ''
    for item in text.lower():
        if item in d:
            new_string += str(d[item]) + ' '
    return new_string[:-1]


print(alphabet_position("The sunset sets at twelve o' clock."))