# Load LSTM network and generate text
import sys
from sys import argv

import numpy
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.models import Sequential

from prepare_dataset import prepare_dataset
from text_parser import parse

number_of_args = 2


def main():
    # Check for expected number of Arguments
    if len(argv) != number_of_args:
        exit("Invalid number of arguments")

    # Get train, test files path and output folder full path
    script, txt_file_path = argv

    # load ascii text and covert to lowercase
    # read txt and lowercase it
    txt = open(txt_file_path).read()
    txt = txt.lower()

    # create mapping of unique chars to integers, and a reverse mapping
    conversion_dic, n_chars, n_vocab = parse(txt)
    char_to_int = conversion_dic["char_to_int"]
    int_to_char = conversion_dic["int_to_char"]

    # prepare the dataset of input to output pairs encoded as integers
    X, y, dataX = prepare_dataset(100, txt, n_chars, char_to_int, n_vocab)
    # define the LSTM model
    model = Sequential()
    model.add(LSTM(2, input_shape=(X.shape[1], X.shape[2])))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    # load the network weights
    model.load_weights(filename)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    # pick a random seed
    start = numpy.random.randint(0, len(dataX) - 1)
    pattern = dataX[start]
    print "Seed:"
    print "\"", ''.join([int_to_char[value] for value in pattern]), "\""
    # generate characters
    for i in range(1000):
        x = numpy.reshape(pattern, (1, len(pattern), 1))
        x = x / float(n_vocab)
        prediction = model.predict(x, verbose=0)
        index = numpy.argmax(prediction)
        result = int_to_char[index]
        seq_in = [int_to_char[value] for value in pattern]
        sys.stdout.write(result)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
    print "\nDone."


if __name__ == "__main__":
    main()
