import time

for i in range(3, 0, -1):
    print(f"\rStarting in {i}...", end="", flush=True)
    time.sleep(1)

print("\rStarted!            ")
