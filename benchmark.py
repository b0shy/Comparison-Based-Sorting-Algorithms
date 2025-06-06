import time
import random
import matplotlib.pyplot as plt


# Sorting Algorithm Implementations


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        arr[k:] = L[i:] + R[j:]

# Heap Sort (vector-based, insert one at a time)
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            parent = (j - 1) // 2
            if arr[j] > arr[parent]:
                arr[j], arr[parent] = arr[parent], arr[j]

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# In-place Quicksort (pivot can be first/last/random — using last here)
def quicksort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Modified Quicksort (median-of-three + insertion sort for small arrays)
def insertion_sort_sub(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    trio = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    trio.sort()
    return trio[1][1]

def quicksort_modified(arr, low=0, high=None, cutoff=10):
    if high is None:
        high = len(arr) - 1
    if high - low + 1 <= cutoff:
        insertion_sort_sub(arr, low, high)
    elif low < high:
        pivot_index = median_of_three(arr, low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pi = partition(arr, low, high)
        quicksort_modified(arr, low, pi - 1, cutoff)
        quicksort_modified(arr, pi + 1, high, cutoff)


# Benchmarking Logic
def time_sort(sort_fn, data):
    total = 0
    for _ in range(5):
        copy = data.copy()
        start = time.perf_counter()
        sort_fn(copy)
        total += time.perf_counter() - start
    return total / 5

def run_benchmark():
    input_sizes = [1000, 2000, 3000, 5000, 10000, 20000, 30000, 40000, 50000, 60000]
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Heap Sort": heap_sort,
        "In-place Quicksort": lambda arr: quicksort_inplace(arr),
        "Modified Quicksort": lambda arr: quicksort_modified(arr)
    }

    results = {name: [] for name in algorithms}

    for size in input_sizes:
        base_data = [random.randint(0, 1000000) for _ in range(size)]
        for name, sort_fn in algorithms.items():
            if name == "Insertion Sort" and size > 10000:
                results[name].append(None)
                continue
            avg_time = time_sort(sort_fn, base_data)
            results[name].append(avg_time)
            print(f"{name} | Size {size} | Avg Time: {avg_time:.4f} sec")

    for name, times in results.items():
        clean_sizes = [s for t, s in zip(times, input_sizes) if t is not None]
        clean_times = [t for t in times if t is not None]
        plt.plot(clean_sizes, clean_times, label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Average Runtime (seconds)")
    plt.title("Sorting Algorithm Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig("sorting_performance.png")
    plt.show()


    # Special Case Testing
    print("\nSpecial Case Timings:")
    last_data = [random.randint(0, 1000000) for _ in range(10000)]
    special_cases = {
        "Sorted": sorted(last_data),
        "Reverse Sorted": sorted(last_data, reverse=True)
    }

    for label, special_input in special_cases.items():
        print(f"\n{label} Input:")
        for name, sort_fn in algorithms.items():
            copy = special_input.copy()
            t = time_sort(sort_fn, copy)
            print(f"{name}: {t:.4f} sec")
            

if __name__ == "__main__":
    run_benchmark()
