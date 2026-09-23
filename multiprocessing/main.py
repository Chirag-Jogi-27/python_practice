from concurrent.futures import ProcessPoolExecutor
import time


def cpu_heavy_calculation(n):
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    numbers = [10_000_000, 10_000_000, 10_000_000, 10_000_000]

    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_heavy_calculation, numbers))
    end = time.perf_counter()

    print(f"Time taken with Multiprocessing: {end - start:.2f} seconds")
