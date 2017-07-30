number_of_args = 2


def parse(txt):
    # map unique chars to integers
    chars = sorted(list(set(txt)))
    char_to_int = dict((c, i) for i, c in enumerate(chars))
    # summarize the loaded data
    n_chars = len(txt)
    n_vocab = len(chars)
    return char_to_int, n_chars, n_vocab
