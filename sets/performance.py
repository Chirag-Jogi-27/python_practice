import time

large_list = list(range(10_000_000))
large_set = set(large_list)

target = 9_999_999

start = time.perf_counter()
print(target in large_list)
end = time.perf_counter()
print(f"List 'in' lookup time: {end - start:.6f} seconds")

start = time.perf_counter()
print(target in large_set)
end = time.perf_counter()
print(f"Set 'in' lookup time:  {end - start:.6f} seconds")
