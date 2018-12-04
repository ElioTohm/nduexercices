#! python
"""
    simple multi processing test first attempt
"""
import json
import sys
import multiprocessing
from collections import Counter

def count(resultqueue, filepath):
    print("Counting Word Occurence in file " + filepath)
    local_counts = {}
    with open(filepath, 'r') as f:
        words = [word.strip() for word in f.read().split() if word.isalpha()]
        for word in words:
            lowercase_word = word.lower()
            if lowercase_word not in local_counts:
                local_counts[lowercase_word] = 0
            local_counts[lowercase_word] += 1
    result_queue.put(local_counts)

def writeToFile(result):
    with open('result.json', 'a+') as result_file:
        json.dump(format(result), result_file)

if __name__ == "__main__":
    jobs = []
    result_queue = multiprocessing.Queue()
    
    for n in range(1, len(sys.argv)):
        process = multiprocessing.Process(target=count, args=(result_queue, sys.argv[n]))            
        process.start()
        jobs.append(process)


    print("Waiting for result...")

    result = result_queue.get() # wait

    writeToFile(result)
    
    for process in jobs: # then kill them all off
        process.terminate()

