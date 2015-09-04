"""
1. Open a file.
Use a dictionary to
"""
from re import sub


def word_frequency(in_string):
    '''Returns top 20 most frequent words from input file'''
    word_dictionary = {}
    counted_dictionary = []

        # Clean each word of each line and check if it is in word_dictionary
    for word in in_string.split():
        word = word_cleaner(word)
        existing_count_of_this_word = word_dictionary.get(word, 1)
        word_dictionary[word] = existing_count_of_this_word + 1
    print(word_dictionary)
    counted_dictionary = zip(*word_dictionary)
    counted_dictionary = sorted(counted_dictionary, reverse=True)
    return counted_dictionary[:20]


def word_cleaner(word):
    # Clean word by removing punctuation: periods, commas, single quote,
    # double quotes, colons, parenthesis, and double dashes)
    return sub(r'^[.,\'":()\[\]]*|[.,\'":()\[\]]*$|', '', word.lower())


def main():
    in_string = ''
    with open('sample.txt') as f:
        in_string = ' '.join(f.readlines()).replace('\n', ' ')
    return word_frequency(in_string)


if __name__=='__main__':
    main()
