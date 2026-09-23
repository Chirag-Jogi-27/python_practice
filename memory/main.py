import sys

r = range(0, 10_000_000)
l = list(range(0, 10_000_000))

print(f"Memory for range(): {sys.getsizeof(r)} bytes")
print(f"Memory for list:    {sys.getsizeof(l)} bytes")
