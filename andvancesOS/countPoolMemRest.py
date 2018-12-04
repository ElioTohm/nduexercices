#! python
"""
    the following handles the second assignment which is memory restriction with multiple files
    it has the same logic as CountPool.py however instead of loading the hole file into a list of words
    we will read file in chunks using python yeild and convert those chunks to list of words
"""
import json
import sys
import time
import multiprocessing
from collections import Counter

process_queue = multiprocessing.Queue()
result = {}
curated_results = {}


def writeToFile(result):
    with open('result.json', 'w+') as result_file:
        # dump sorted result in data
        json.dump(sorted(result.iteritems()), result_file)

# read file in chunks utilizing yield
def readInChunks(file_object, chunk_size=50024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 50k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

# mapper AKA counting words using dictionary
def mapper(chunk):
    print"Counting words from chunks... "
    # use dictionary to map counts
    local_counts = {}
    # convert chunks to list of words take only alphabetical strings to make things easier
    words = [word for word in chunk.split() if word.isalpha()]
    for word in words:
        # convert words to lower case
        lowercase_word = word.lower()
        if lowercase_word not in local_counts:
            local_counts[lowercase_word] = 0
        local_counts[lowercase_word] += 1
    return local_counts


# reducer using counter to count array of dictionary
def reducer(result):
    counter = Counter()
    for data in result:
        counter.update(data)
    return dict(counter)

def main():
    # utilizing all - 2 of the available cores on the machine end set max threads perchild to limit memory use
    pool = multiprocessing.Pool(processes=(multiprocessing.cpu_count())-2, maxtasksperchild=1000)
    # take all arguments from system except first argument which is python file name
    for file in sys.argv[1:]:
        chunks = []
        # open each file
        opened_file = open(file)
        # convert file into chunks
        for piece in readInChunks(opened_file):
            chunks.append(piece)
        # process chunk in pool
        result = pool.map_async(mapper, chunks)    
    
    # await the result
    # result.wait()

    # reduce function to count all results from children
    # and write to file
    writeToFile(reducer(result.get())) 

    # close and terminate processs
    pool.close()
    pool.terminate()


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print 'execution took {} seconds'.format(elapsed_time)