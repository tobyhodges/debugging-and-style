# Debugging and Coding Style in Python

__Materials for an exercise on debugging and coding in Python.__

The file `script1.py` is a Python script that has been written to calculate
statistics about DNA sequences described in a [FASTA file*](#fasta-format).

Download or `git clone` this repository and then follow the instructions below.

#### Your Tasks

1. __Before__ you look at the sequence files in this repository, open the script in your favourite editor and discuss ways in which it could be improved. Things to think about might include
 - How easy is it to understand what the script does?
 - How robust is the script?
 - Does it follow good coding standards?
 - Does it do what it is supposed to?
 - What problems can you foresee, if the script were to be shared with others or applied to a different sequence file?
2. Now run the script on `exampleSequences1.fasta`
 - Has this made you notice any more improvements that could be made?
3. What about if you run the script on `exampleSequences2.fasta`?
4. Make a copy of the script (or start from scratch if you prefer!) and make as many improvements to the code as you think are necessary to make it
 - robust
 - portable
 - shareable
 - easy to maintain/adapt
 - do what it is supposed to do!
(__Note:__ You may be aware that the Biopython library includes functions and object classes to work with sequence objects. Please avoid using the library for these exercises.)
5. If you have time, try to further adapt the script to expand its functionality such that, given a file of protein sequences instead, it will produce counts of the different amino acids.

#### *FASTA Format

FASTA is a file format designed to hold information about biological sequence
molecules. Generally speaking, there are three different types of molecule that
can be represented in a FASTA file - DNA, RNA, and protein. All of these molecules
are polymers - strings of repeated units in a particular order. These subunits
are drawn from a finite pool, with each specific type of subunit referred to by
a letter. For this reason, the pool of possible units is often referred to as an
_alphabet_.

DNA and RNA molecules are constructed from four different units (_nucleotides_):
 _A_, _C_, _G_, and _T_ for DNA; _A_, _C_, _G_, and _U_ for RNA.
The protein alphabet is larger, made up of 20 different possible units (_amino acids_).

The file format itself is constructed as follows:

```
>id1 additional_info
<sequence1>
[<sequence1>]
[<sequence1>]
[...]
[<sequence1>]

[>id2 additional_info
<sequence2>
[<sequence2>]
[<sequence2>]
[...]
[<sequence2>] ]

[...]
```

A single FASTA file may contain records for one or more sequences. Each sequence
record is constructed from the following two elements:

1. A header line, beginning with a `>` symbol. This header line can contain the
following parts:
  - an identifier for the sequence (__required__). This should be unique (at least)
within the file
  - more information about the sequence (__optional__). This additional information
is separated from the identifier by a space
2. The sequence of the molecule, described in the approriate alphabet. Long
sequences can be split across multiple lines.

The Wikipedia page for FASTA format is well written and has more information:
https://en.wikipedia.org/wiki/FASTA_format
