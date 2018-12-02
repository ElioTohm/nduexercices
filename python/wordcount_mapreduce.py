'''Usage: wordcount_mapreduce.py [-h] DATA_DIR

Read a collection of .txt documents and count how many times each word
appears in the collection.

Arguments:
   DATA_DIR  A directory with documents (.txt files).

Options:
   -h --help
'''

from __future__ import division, print_function
import os, glob, logging
from docopt import docopt

logging.basicConfig(level=logging.DEBUG)

def count_words(filepath):
   counts = {}
   with open(filepath, 'r') as f:
      words = [word.strip() for word in f.read().split()]

      for word in words:
         if word not in counts:
            counts[word] = 0
         counts[word] += 1
      return counts


def merge_counts(counts1, counts2):
   for word, count in counts2.items():
      if word not in counts1:
         counts1[word] = 0
      counts1[word] += counts2[word]
   return counts1


if __name__ == '__main__':
   args = docopt(__doc__)
   if not os.path.exists(args['DATA_DIR']):
      raise ValueError('Invalid data directory: %s' % args['DATA_DIR'])

   per_doc_counts = map(count_words, glob.glob(os.path.join(args['DATA_DIR'], '*.txt')))
   counts = reduce(merge_counts, [{}] + per_doc_counts)
   logging.debug(counts)