# https://www.python.org/dev/peps/pep-0564/
# https://docs.python.org/3.7/library/time.html#time.time_ns

import time

print(f'time    => {time.time()}')
print(f'time_ns => {time.time_ns()}')

print()

mono = time.monotonic_ns()
time.sleep(1)
print(f'monotonic_ns - mono => {time.monotonic_ns() - mono}')

print()

perf = time.perf_counter_ns()
time.sleep(.75)
print(f'perf_counter_ns - perf => {time.perf_counter_ns() - perf}')

print()

thread = time.thread_time_ns()
time.sleep(.5)
print(f'thread_time_ns - thread => {time.thread_time_ns() - thread}')
# system + user CPU time = 0 because all we did was sleep!
