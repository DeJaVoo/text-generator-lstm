# Load LSTM network and generate text
import sys

import numpy
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.models import Sequential
from prepare_dataset import prepare_dataset
from sys import argv

number_of_args = 3

def main():
    """
    Receives 2 parameters - the text to use as a starting point, and the weights file
    :return: prints out 1000 characters based on the training and the chosen seed
    """
    # Check for expected number of Arguments
    if len(argv) != number_of_args:
        exit("Invalid number of arguments")

    # load ascii text and covert to lowercase
    filename = argv[1]  #text
    raw_text = open(filename).read()
    raw_text = raw_text.lower()

    # create mapping of unique chars to integers, and a reverse mapping
    chars = sorted(list(set(raw_text)))
    chars.insert(0,'\r')
    print chars
    char_to_int = dict((c, i) for i, c in enumerate(chars))
    int_to_char = dict((i, c) for i, c in enumerate(chars))
    # summarize the loaded data
    n_chars = len(raw_text)
    n_vocab = len(chars)
    print "Total Characters: ", n_chars
    print "Total Vocab: ", n_vocab
    # prepare the dataset of input to output pairs encoded as integers
    seq_length = 100
    X, y, dataX = prepare_dataset(seq_length, raw_text, n_chars, char_to_int, n_vocab)

    # define the LSTM model
    print (X.shape[1], X.shape[2])
    model = Sequential()
    model.add(LSTM(512, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(512))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))

    # load the network weights
    weightFile = argv[2]
    model.load_weights(weightFile)
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