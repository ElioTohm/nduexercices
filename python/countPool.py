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
        
        words = [word.strip() for word in f.read().split()]
        for word in words:
            if word not in local_counts:
                local_counts[word] = 0
            local_counts[word] += 1
    return local_counts

def writeToFile(result):
    with open('result.json', 'a+') as result_file:
        json.dump(format(result), result_file)

def mapCallback(result):
    print result

def main():

    # utilizing half the available cores on the machine
    pool = multiprocessing.Pool(multiprocessing.cpu_count()/2)

    result = pool.map_async(count, sys.argv[1:len(sys.argv)], callback=writeToFile)    
    result.wait()
    # dict(Counter(curated_results[1])+Counter(curated_results[2]))

    pool.close()
    pool.terminate()


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print 'execution took {} seconds'.format(elapsed_time)