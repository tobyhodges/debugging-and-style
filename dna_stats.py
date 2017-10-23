#! /usr/bin/env python
'''This script counts nucleotides in sequences in
a DNA FASTA file, prints the content of each sequence
and the G/C content too.'''
from argparse import ArgumentParser # tool for parsing command line arguments
# load in special type of dictionary that remembers the order of its keys
from collections import OrderedDict
from sys import stderr, stdout      # objects for writing to STDERR and STDOUT

def calculate_GC(nucleotide_counts):
    '''Given a dictionary of nucleotide counts, such as the second-level
    dictionaries returned from count_letter(), calculate G/C content and return
    it as a percentage.

    Usage:

    calculate_GC(count_dict) -> float'''

    c_count = nucleotide_counts['C']
    g_count = nucleotide_counts['G']
    total_length = sum(nucleotide_counts.values())
    # use float() to make the % calculation compatible with python version 2
    percentage_GC = (float(c_count + g_count) / total_length) * 100
    return percentage_GC

def count_letters(filename, alphabet='DNA'):
    '''Counts the frequency of each letter in each sequence contained in a
    FASTA file. Returns a dictionary of dictionaries keyed by sequence ID string.
    Each nested dictionary contains letter:count pairs for the respective sequence.

    Usage:

    count_letters(file_name, alphabet='DNA') -> dict

    alphabet    str from ['DNA','RNA','PROTEIN' ]
    '''

    _alphabets = {'DNA': list('ACGT'),
                  'RNA': list('ACGU'),
                  'PROTEIN': list('ARNDBCEQZGHILKMFPSTWYV')}
    try: # use try:except blocks to perform simple tests and specify error behaviour
        _alphabet_letters = _alphabets[alphabet.upper()]
    except KeyError: # define what should happen when an unexpected key is used
        raise KeyError("Unexpected alphabet: {}. Must be one of: 'DNA', 'RNA', 'PROTEIN'".format(alphabet)) # custom error message to help user understand what went wrong
    sequence_counts = OrderedDict()
    with open(filename, 'r') as handle:
        for line in handle.readlines():
            line = line.strip()
            if line[0] == '>': # find header/description lines
                id_string = line.lstrip('>') # remove > from start of seq header
                sequence_counts[id_string] = OrderedDict( (l,0) for l in _alphabet_letters ) # initialise count for this sequence, with an OrderedDictionary built from a for-loop written onto a single line
                ignored = {} # initialise an empty dictionary to capture any unexpected letters
            else: # if not a header line, must be a sequence line, so count the letters
                for letter in line.upper():
                    if letter not in _alphabet_letters: # capture non-alphabet letters
                        if letter in ignored:
                            ignored[letter] += 1
                        else:
                            stderr.write( # print message for logging/debugging
                            'ignoring unexpected letter {} found in sequence {}\n'.
                            format(letter, id_string))
                            ignored[letter] = 1
                    else:
                        sequence_counts[id_string][letter] += 1
                if ignored: # print counts for ignored letters, useful for later debugging
                    stderr.write('ignored letter counts for {}:\n{}\n'.format(
                    id_string,
                    '\n'.join(['{}: {}'.format(k, v) for k,v in ignored.items()])
                    ))
    return sequence_counts

# create argument parser to manage interface
parser = ArgumentParser(description='''Count the nucleotides
in each sequence in a DNA FASTA file, and print a summary of
the content of each sequence, and the G/C % too.''')
parser.add_argument('fasta', # positional argument(s) for input file(s)
                    metavar='FASTA',
                    type=str,
                    nargs='+',
                    help='A file of DNA sequences in FASTA format')
parser.add_argument('-g', '--GC', # option for calculating G/C content
                    action='store_true', # this is a boolean (true/false) option, which should store a 'True' value if specified on the command line
                    help='calculate GC content for DNA sequences')
args = parser.parse_args()
files = args.fasta # get the FASTA file name(s) from the command line arguments
# loop through all provided files and calculate the stats...
for filename in files:
    stdout.write('\nGetting counts for file {}\n'.format(
    filename))
    # call count_letters function defined above
    counts = count_letters(filename, 'DNA')
    # for each
    for seq_id, count_dict in counts.items():
        stdout.write('{}\n'.format(seq_id)) # write sequence id to STDOUT
        for letter, count in count_dict.items():
            stdout.write('{}\t{}\n'.format(letter, count)) # counts to STDOUT
        if args.GC:
            # call the calculate_GC function defined above
            GC_content = calculate_GC(count_dict)
            # use {:.2} to insert percentage into string with two decimal places of precision
            stdout.write('GC content:\t{:.2f}%\n'.format(GC_content))
