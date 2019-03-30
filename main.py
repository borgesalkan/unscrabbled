import sys
from argparse import ArgumentParser


import words_finder
import words_parser


parser = ArgumentParser(description='Un-scrabble letters')
parser.add_argument('--infile', type=str, help='Optional input file name listing all scrabble words')
parser.add_argument('--outfile', type=str, help='Optional output file name to store dictionary of scrabble words')
parser.add_argument('--length', type=int, help='Optional length of scrabble words')
parser.add_argument('letters', type=str, help='Optional input file name listing all scrabble words')


if __name__ == '__main__':
    name_space = parser.parse_args(sys.argv[1:])
    in_file, out_file = name_space.infile, name_space.outfile
    letters, length = name_space.letters, name_space.length

    if in_file or out_file:
        words_parser.parse(in_file, out_file)

    results = words_finder.find_words(letters=letters, length=length, in_file=out_file)
    if not results:
        print('No words found for the letters {letters}{length}.'.format(
            letters=', '.join(list(letters)), length=' of length {}'.format(length) if length else ''))

    else:
        print('Found words: {}.'.format(', '.join(results)))
