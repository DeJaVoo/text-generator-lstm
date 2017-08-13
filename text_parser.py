number_of_args = 2


def parse(txt):
    """
    Parses text document to vector representation
    :param txt: txt file
    :return: map for char to int and int to char, number of chars in text file, number of unique chars in text file
    """
    # map unique chars to integers
    chars = sorted(list(set(txt)))
    char_to_int = dict((c, i) for i, c in enumerate(chars))
    int_to_char = dict((i, c) for i, c in enumerate(chars))
    # summarize the loaded data
    n_chars = len(txt)
    n_vocab = len(chars)
    return {"char_to_int": char_to_int, "int_to_char": int_to_char}, n_chars, n_vocab
