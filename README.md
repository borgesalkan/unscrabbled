# Unscrabbled

This is a simple Python project that you may just clone and run on your machine.
**Unscrabbled** can unscramble letters and print a list of scrabble words after referring to a dictionary.

## Getting Started

refer below sub-sections to get started.

### Prerequisites

The project should work fine on Mac or Linux with Python 2 or above.

### Installing

Clone the repo on your local machine in any working directory.
```
git clone git@github.com:borgesalkan/unscrabbled.git
```

Change directory to **unscrabbled**.

```
cd unscrabbled/
```

We are all set to run the project.

## Running the code

Simple run.
```
$ python main.py 'ettew'
Found words: TWEET.
```

You may give your favorite list of words in a text file. Just assign file name with full path to `infile` arg.
```
$ python main.py --infile=words_list.txt 'ettew'
Found words: TWEET.
```

If you want 5 letter word from say 7 letters, then use the `length` argument.
```
$ python main.py --length=5 'etltewr'
Found words: ETTLE, RELET, RELET, REWET, REWET, TEWEL, TEWEL, TWEEL, TWEEL, TWEER, TWEER, TWEET.
```

There are some other optional arguments that you may choose to use. For a full list, checkout the help
```
$ python main.py --help
usage: main.py [-h] [--infile INFILE] [--outfile OUTFILE] [--length LENGTH]
               letters

Unscramble letters to return Scrabble words.

positional arguments:
  letters            Optional input file name listing all scrabble words

optional arguments:
  -h, --help         show this help message and exit
  --infile INFILE    Optional input file name listing all scrabble words
  --outfile OUTFILE  Optional output file name to store dictionary of scrabble
                     words
  --length LENGTH    Optional length of scrabble words
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Collins Scrabble words 2015.
