from re import sub
import sys
from copy import deepcopy


def word_frequency(in_string):
    '''Returns top 20 most frequent words from input file'''
    word_dictionary = {}
    output_dictionary = {}
    counted_dictionary = []

        # Clean each word and check if it is in word_dictionary
    for word in in_string.split():
        word = word_cleaner(word)
        existing_count_of_this_word = word_dictionary.get(word, 0)
        word_dictionary[word] = existing_count_of_this_word + 1

    output_dictionary = remove_common(word_dictionary)

    counted_dictionary = sorted(output_dictionary.items(), key=lambda w: w[1], reverse=True)
    for i in counted_dictionary[:20]:
        print("{} {}".format(i[0], i[1]))

    return output_dictionary


def remove_common(word_dictionary):
    COMMON_WORDS = ["a,able,about,across,after,all,almost,also,am,among,an,and,"
                    "any,are,as,at,be,because,been,but,by,can,cannot,could,dear,"
                    "did,do,does,either,else,ever,every,for,from,get,got,had,"
                    "has,have,he,her,hers,him,his,how,however,i,if,in,into,is,"
                    "it,its,just,least,let,like,likely,may,me,might,most,must,my,"
                    "neither,no,nor,not,of,off,often,on,only,or,other,our,own,"
                    "rather,said,say,says,she,should,since,so,some,than,that,the,"
                    "their,them,then,there,these,they,this,tis,to,too,twas,us,"
                    "wants,was,we,were,what,when,where,which,while,who,whom,why,"
                    "will,with,would,yet,you,your"]
    COMMON_LIST = ''.join(COMMON_WORDS).split(',')
    export_dictionary = deepcopy(word_dictionary)
    for key, value in word_dictionary.items():
        if key in COMMON_LIST:
            del export_dictionary[key]
    return export_dictionary



def word_cleaner(word):
    # Clean word by removing punctuation: periods, commas, single quote,
    # double quotes, colons, parenthesis, and double dashes)
    return sub(r'^[.,\'":;()\[\]!]*|[.,\'":;()\[\]!]*$', '', word.lower())


# def histogram(in_dict):
#     counted_dictionary = sorted(in_dict.items(), key=lambda w: w[1], reverse=True)
#     for i in counted_dictionary[:20]:
#         print("{} {}".format(i[0], i[1]*'#'))


def main():
    in_string = ''
    if len(sys.argv) == 1:
        with open('sample.txt') as f:
            in_string = ' '.join(f.readlines()).replace('\n', ' ')
    else:
        # print(sys.argv[1])
        with open(sys.argv[1]) as g:
            in_string = ' '.join(g.readlines()).replace('\n', ' ')

    # histogram(word_frequency(in_string))
    return word_frequency(in_string)


if __name__=='__main__':
    main()
