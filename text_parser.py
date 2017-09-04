number_of_args = 2


def parse(txt):
    """
    Parses the given text and provides a dictionary to convert char to int and int to char
    :param txt: text file
    :return: dictionary containing arrays to convert between char to int and int to char, as well as the number of total characters (n_chars) and number of different characters (n_vocab)
    """
    # map unique chars to integers
    chars = sorted(list(set(txt)))
    char_to_int = dict((c, i) for i, c in enumerate(chars))
    int_to_char = dict((i, c) for i, c in enumerate(chars))
    # summarize the loaded data
    n_chars = len(txt)
    n_vocab = len(chars)
    return {"char_to_int": char_to_int, "int_to_char": int_to_char}, n_chars, n_vocab
