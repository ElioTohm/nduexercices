#! python
import json
import sys
import time
import multiprocessing
import numpy
from collections import Counter

process_queue = multiprocessing.Queue()
result = {}
curated_results = {}

def count(filepath):
    print"Counting Word Occurence in file {}".format(filepath)
    local_counts = {}
    with open(filepath, 'r') as f:
        # create list of words that are alphanumerci only
        words = [word.strip() for word in f.read().split() if word.isalpha()]
        for word in words:
            lowercase_word = word.lower()
            if lowercase_word not in local_counts:
                local_counts[lowercase_word] = 0
            local_counts[lowercase_word] += 1
    return local_counts

def writeToFile(result):
    with open('result.json', 'w+') as result_file:
        # dump sorted result in data
        json.dump(sorted(result.iteritems()), result_file)

def mapCallback(result):
    print "done"

def main():

    # utilizing half the available cores on the machine
    pool = multiprocessing.Pool(multiprocessing.cpu_count()/2)

    result = pool.map_async(count, sys.argv[1:len(sys.argv)], callback=mapCallback)    
    result.wait()

    counter = Counter()
    for data in result.get():
        counter.update(data)

    writeToFile(dict(counter))

    pool.close()
    pool.terminate()


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print 'execution took {} seconds'.format(elapsed_time)