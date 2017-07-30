from text_parser import parse
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

    char_to_int, n_chars, n_vocab = parse(txt)

    print "Total Characters: ", n_chars
    print "Total Vocab: ", n_vocab
    print "Char To Int Dictionary: ", char_to_int

if __name__ == "__main__":
    main()