## Python Script Improvement Exercise

The file `script1.py` is a Python script that has been written to calculate statistics about DNA sequences described in a FASTA file.

You can clone this repository by executing the following command in a terminal window:

```
git clone git@git.embl.de:stamper/software-carpentry-nov2015.git
```

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
