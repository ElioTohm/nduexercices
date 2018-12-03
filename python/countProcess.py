import multiprocessing

def runmycode(result_queue, iterations):
   print("Requested...")
   while 1==1: # This is an infinite loop, so I assume you want something else here
       with iterations.get_lock(): # Need a lock because incrementing isn't atomic
           iterations.value += 1
   if "result found (for example)":
       result_queue.put("result!")

   print("Done")


if __name__ == "__main__":
    processs = []
    result_queue = multiprocessing.Queue()

    iterations = multiprocessing.Value('i', 0)
    for n in range(4): # start 4 processes
        process = multiprocessing.Process(target=runmycode, args=(result_queue, iterations))
        process.start()
        processs.append(process)

    print("Waiting for result...")

    result = result_queue.get() # wait

    for process in processs: # then kill them all off
        process.terminate()

    print("Got result: {}".format(result))
    print("Total iterations {}".format(iterations.value))
