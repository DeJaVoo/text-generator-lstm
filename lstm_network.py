from sys import argv

from keras.callbacks import ModelCheckpoint
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

    # read txt and lowercase it
    txt = open(txt_file_path).read()
    txt = txt.lower()

    conversion_dic, n_chars, n_vocab = parse(txt)
    char_to_int = conversion_dic["char_to_int"]

    # prepare the dataset of input to output pairs encoded as integers
    X, y, dataX = prepare_dataset(100, txt, n_chars, char_to_int, n_vocab)
    # define the LSTM model
    model = Sequential()
    model.add(LSTM(512, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(512))
	model.add(Dropout(0.2))
	model.add(LSTM(512))
	model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    # define the checkpoint
    filepath = "weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    # fit the model
    model.fit(X, y, epochs=2, batch_size=128, callbacks=callbacks_list)


if __name__ == "__main__":
    main()
