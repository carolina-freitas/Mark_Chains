"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_data = open(file_path).read()
    # file_data.rstrip()
    # file_data.read()


    # green_eggs = ""

    # for line in file_data:
    #     green_eggs += line


    return file_data

# file_data = open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    green_eggs_words = text_string.split()

    chains = {}

    for idx in range(len(green_eggs_words) - 2):
        chain_key = (green_eggs_words[idx], green_eggs_words[idx+1])

        if chain_key in chains:
            chains[chain_key].append(green_eggs_words[idx+2])

        else:
            chains[chain_key] = [green_eggs_words[idx+2]]

    print(chains)
    # your code goes here
    return chains

# make_chains(file_data)

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    while True:
        keys = chains.keys()
        keys = list(keys)

        if len(words) < 1:
            words.extend(keys[0])

        elif (words[-2], words[-1]) in chains:
            rand_string = choice(chains[(words[-2], words[-1])])
            words.append(rand_string)
            
        else:
            break
        
    # print(words)

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

print(sys.argv)

# program_name = sys.argv[0]
# arguments = sys.argv[1:]
# count = len(arguments)
