import numpy
from keras.utils import np_utils


def prepare_dataset(seq_length, txt, n_chars, char_to_int, n_vocab):
    """
    Prepare data set for LSTM
    :param seq_length: sequence length (size of sentence)
    :param txt: text file
    :param n_chars: numbe of chars in text file
    :param char_to_int: chars to int map
    :param n_vocab: number of unique chars in text file
    :return:
    """
    dataX = []
    dataY = []
    for i in range(0, n_chars - seq_length, 1):
        seq_in = txt[i:i + seq_length]
        seq_out = txt[i + seq_length]
        dataX.append([char_to_int[char] for char in seq_in])
        dataY.append(char_to_int[seq_out])
    n_patterns = len(dataX)
    print "Total Patterns: ", n_patterns
    # reshape X: [samples, time steps, features]
    X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
    # normalize by vocabulary size
    X = X / float(n_vocab)
    # Convert dataY to binary class matrix
    y = np_utils.to_categorical(dataY)
    return X, y , dataX
