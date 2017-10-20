'''This script counts nucleotides in sequences in
a DNA FASTA file, prints the content of each sequence
and the G/C content too.'''
from sys import argv

# command_line_arguments = argv[1:]
# program_name = argv[0]
# print(program_name)
# print(command_line_arguments)

filename = argv[1]
handle = open(filename, 'r')
for line in handle.readlines():
    line = line.strip()
    if line[0] == '>': # find header/description lines
      print(line)
      nucleotides = {'A': 0,
                     'C': 0,
                     'G': 0,
                     'T': 0}
    else:
      for l in line:
          nucleotides[l] += 1
      print('nucleotide content:')
      for nucleotide in nucleotides:
          print('%s: %d' % (nucleotide, nucleotides[nucleotide]))
      c = nucleotides['C']
      g = nucleotides['G']
      a = nucleotides['A']
      t = nucleotides['T']
      GC_content = float(c + g) / (c + g + a + t)
      print(GC_content)
handle.close()
