Comparison-Based Sorting Algorithms

This project implements and benchmarks five comparison-based sorting algorithms:

- Insertion Sort
- Merge Sort
- Heap Sort (vector-based, one insertion at a time)
- In-place Quicksort
- Modified Quicksort (median-of-three pivot + insertion sort for small arrays)

How to Run:

1. Install the required library:
   pip install matplotlib

2. Run the benchmark script:
   python main.py

What It Does:

- Measures and compares average runtime of each algorithm for input sizes from 1,000 to 60,000.
- Uses the same random input for each algorithm at each size.
- Tests two special cases:
  - Sorted input
  - Reverse sorted input

Output:

- Console shows average runtimes for all algorithms and special cases.
- A graph is saved as sorting_performance.png showing runtime vs input size.