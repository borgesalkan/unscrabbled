from collections import defaultdict, OrderedDict


def parse(in_file=None, out_file=None):
    """Reads list of words from a file and writes a new file sorted by letters in each word.
    :param in_file: Optional input file name of all words as an str
    :param out_file: Optional output filr name to store the sorted words dictionary
    :return:
    """
    in_file_name = in_file or 'words_list.txt'
    out_file_name = out_file or 'words_dict.json'

    in_file = open(in_file_name, 'r')

    words = in_file.read().split()
    in_file.close()

    letters_defaultdict = defaultdict(list)
    for word in words:
        word.upper()
        key = ''.join(sorted(word))
        letters_defaultdict[key].append(word)

    sorted_keys = sorted(list(letters_defaultdict.keys()))
    out_file = open(out_file_name, 'w')
    out_file.write('{\n')
    for key in sorted_keys:
        line = "\t'{key}': {values},\n".format(key=key, values=letters_defaultdict[key])
        out_file.write(line)
    out_file.write('}')
    out_file.close()
