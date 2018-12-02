from __future__ import print_function
import os, random, logging
from docopt import docopt


def generate_random_lists(num_lists, ints_per_list, min_int, max_int):
   return [[random.randint(min_int, max_int) for _ in range(ints_per_list)] for _ in range(num_lists)]

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


if __name__ == '__main__':
   args = docopt(__doc__)
   num_lists, ints_per_list, min_int, max_int, dest_dir = [
      int(args['NUM_LISTS']),
      int(args['INTS_PER_LIST']),
      int(args['MIN_INT']),
      int(args['MAX_INT']),
      args['DEST_DIR']
   ]

   if not os.path.exists(dest_dir):
      os.makedirs(dest_dir)

   lists = generate_random_lists(num_lists, ints_per_list, min_int, max_int)
   curr_list = 1
   for lst in lists:
      with open(os.path.join(dest_dir, '%d.txt' % curr_list), 'w') as f:
         f.write(os.linesep.join(map(str, lst)))
      curr_list += 1
   logging.debug('Numbers written.')
