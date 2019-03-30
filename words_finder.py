import ast
import itertools


def find_words(letters, length=None, in_file=None):
    """Returns a list of scrabble words found based on the letters passed in.
    :param letters: Required list of characters or an str
    :param length: Optional length of scrabble words to be returned
    :param in_file: Optional file name that stores dictionary of sorted letters mapped to lists of scrabble words
    :return: List of scrabble words that can be formed using the letters and length
    """
    letters = ''.join(sorted(''.join(list(letters)).upper()))
    if length > len(letters):
        return []

    length = length or len(letters)

    in_file_name = in_file or 'words_dict.json'
    in_file = open(in_file_name, 'r')
    letters_dict = ast.literal_eval(in_file.read())
    in_file.close()

    results = []
    for key in itertools.combinations(letters, length):
        word = ''.join(sorted(key))
        if word in letters_dict:
            results.extend(letters_dict[word])

    results.sort()

    return results
