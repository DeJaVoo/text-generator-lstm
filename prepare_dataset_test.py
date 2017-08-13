from text_parser import parse
from prepare_dataset import prepare_dataset
from sys import argv

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
    X, y, dataX = prepare_dataset(400,txt,n_chars,char_to_int,n_vocab)
    print "X is ", X
    print "y is ", y


if __name__ == "__main__":
    main()