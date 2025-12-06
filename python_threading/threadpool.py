# import concurrent
import time
import concurrent.futures

start = time.perf_counter()
def thread_func(seconds):
    print(f"waiting {seconds}")
    time.sleep(seconds)
    return (f"waited for {seconds}")

## use concurrency method 1:
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,2,1,3]
    results = [ executor.submit(thread_func,sec) for sec in secs]
    print(results)
    for result in concurrent.futures.as_completed(results):
        print(result.result())

# use concurrency method 2:
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 2, 1, 3]
    results = executor.map(thread_func, secs)
    for result in results:
        print(result)

finish = time.perf_counter()
print(finish - start)