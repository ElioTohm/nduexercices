#! python
import json
import sys
import multiprocessing
from collections import Counter

process_queue = multiprocessing.Queue()
result = {}


def count(filepath):
    print("Counting Word Occurence in file " + filepath)
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


def main():
    pool = multiprocessing.Pool(1)
    arg_num = 1
    while arg_num < len(sys.argv):
        result[arg_num] = pool.apply_async(count, args=(sys.argv[arg_num],))
        arg_num += 1

    writeToFile(result[1].get())
    writeToFile(result[2].get())

    pool.close()
    pool.terminate()


if __name__ == "__main__":
    main()
