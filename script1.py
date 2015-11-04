filename = 'exampleSequences1.fasta'
handle = open(filename, 'r')
for line in handle.readlines():
    if line[0] == '>':
      print(line)
      a = 0
      c = 0
      g = 0
      t = 0
    else:
      for l in line:
          if l == 'A':
              a = a + 1
          elif l == 'C':
              c = c + 1
          elif l == 'G':
              g = g +1
          else:
              t = t + 1
      print('nucleotide content:')
      print('A:', str(a))
      print('C:', str(c))
      print('G:', str(g))
      print('T:', str(t))
      x = float(c + g) / (c + g + a + t)
      print(x)
      