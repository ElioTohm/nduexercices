#! python
"""
    this example we are loading the hole files into memory 
    each file will be used in a process and will be handle by the multiprocessing library in python 
    this example is using pool to show the queue handling of tasks on the process

"""
import json
import sys
import time
import multiprocessing
from collections import Counter

result = {}
curated_results = {}

# map file to list of words and use dictionary to map words to count
def mapper(filepath):
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

# reducer counts array of dictionary
def reducer(result):
    counter = Counter()
    for data in result:
        counter.update(data)
    return dict(counter)

def writeToFile(result):
    with open('result.json', 'w+') as result_file:
        # dump sorted result in data
        json.dump(sorted(result.iteritems()), result_file)

def mapCallback(result):
    print "done"

def main():
    # utilizing all - 2 of the available cores on the machine end set max threads perchild to limit memory use
    pool = multiprocessing.Pool(processes=(multiprocessing.cpu_count())-2, maxtasksperchild=1000)
    # using pool to handle individual files in 1 process
    result = pool.map_async(mapper, sys.argv[1:len(sys.argv)], callback=mapCallback)    
    # reduce and write result to files
    writeToFile(reducer(result.get()))
    # close pool and terminate
    pool.close()
    pool.terminate()


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print 'execution took {} seconds'.format(elapsed_time)