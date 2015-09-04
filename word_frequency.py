from re import sub
import sys

def word_frequency(in_string):
    '''Returns top 20 most frequent words from input file'''
    word_dictionary = {}
    counted_dictionary = []

        # Clean each word and check if it is in word_dictionary
    for word in in_string.split():
        word = word_cleaner(word)
        existing_count_of_this_word = word_dictionary.get(word, 0)
        word_dictionary[word] = existing_count_of_this_word + 1

    counted_dictionary = sorted(word_dictionary.items(), key=lambda w: w[1], reverse=True)
    for i in counted_dictionary[:20]:
        print("{} {}".format(i[0], i[1]))

    return word_dictionary


def word_cleaner(word):
    # Clean word by removing punctuation: periods, commas, single quote,
    # double quotes, colons, parenthesis, and double dashes)
    return sub(r'^[.,\'":;()\[\]!]*|[.,\'":;()\[\]!]*$|', '', word.lower())


def main():
    in_string = ''
    if len(sys.argv) == 0:
        with open('sample.txt') as f:
            in_string = ' '.join(f.readlines()).replace('\n', ' ')
    else:
        with open(sys.argv[1]) as f:
            in_string = ' '.join(f.readlines()).replace('\n', ' ')
    return word_frequency(in_string)


if __name__=='__main__':
    main()
