import time
import threading
start = time.perf_counter()
def thread_func(seconds):
    print(f"wait 1 {seconds}")
    time.sleep(seconds)
    print("done!")
threads = []
for t in range(10):
    threads.append(threading.Thread(target=thread_func, args=[t]))
for i in threads:
    i.start()
for i in threads:
    i.join()

finish = time.perf_counter()
print(finish - start)