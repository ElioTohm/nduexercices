    #! python
import json
import sys
import time
import multiprocessing
from collections import Counter

process_queue = multiprocessing.Queue()
result = {}
curated_results = {}

def countInLine(words):
    print"Counting "
    local_counts = {}
    for word in words.split():
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

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count()/2, maxtasksperchild=1000)

    # utilizing half the available cores on the machine end set max threads perchild to limit memory use
    lines = open(sys.argv[1], 'r').read().split("\n")

    result = pool.map_async(countInLine, lines)    
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