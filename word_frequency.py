"""
1. Open a file.
Use a dictionary to
"""
from re import sub


def word_frequency():
    '''Returns top 20 most frequent words from input file'''
    file_in = open('sample.txt')
    file_lines = file_in.readlines()
    file_in.close()

    word_dictionary = {}
    line_words = []

    for line in file_lines:
        # Strip newlines and split line
        line_words = repr(line.rstrip('\n')).split()

        # Clean each word of each line and check if it is in word_dictionary
        for word in line_words:
            # Clean word by removing punctuation
            # (periods, commas, single quote, double quotes, colons,
            # parenthesis, and double dashes)
            word = sub(r'^[.,\'":()\[\]]*|[.,\'":()\[\]]*$|', '', word.lower())
            print(word)
            word_dictionary.get(word, 1)
    return line_words[:21]


def main():
    word_frequency()


if __name__=='__main__':
    main()
