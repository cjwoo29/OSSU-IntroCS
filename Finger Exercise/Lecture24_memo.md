# Lecture 24: Sorting Algorithms

## 1. Amortized Cost of Sorting

- **Motivation:** Linear search in an unsorted list takes $\Theta(n)$ time. Binary search takes $O(\log n)$ time, but it requires the list to be sorted.


- **When to Sort First:** It never makes mathematical sense to sort a list just to perform a single search. However, it is beneficial if you sort the list once and then perform many searches ($K$ searches). For a large number of searches ($K$), the one-time cost of sorting becomes negligible (amortized cost).

---

## 2. Basic Sorting Algorithms

**Bogo Sort (Random / Monkey Sort)**

- **Method:** Like throwing a deck of cards in the air, picking them up, and checking if they are sorted, repeating until they are.


- **Complexity:**
    - **Best Case:** $\Theta(n)$ (just checking if the list is already sorted).
    - **Worst Case:** Unbounded ($\Theta(?)$) because it depends entirely on random chance and could theoretically run forever.





**Bubble Sort**
- **Method:** Successively compares consecutive pairs of elements and swaps them if the smaller one is not first. The algorithm makes multiple passes over the list and stops only when a full pass completes with no swaps.
- **Complexity:** $\Theta(n^2)$ where $n$ is the length of the list.

**Selection Sort**

- **Method:** It iteratively extracts the minimum element from the remaining unsorted portion of the list and swaps it into its correct position (starting at index 0, then index 1, etc.). This ensures that at the $i$-th step, the first $i$ elements are completely sorted.

- **Complexity:** $\Theta(n^2)$ because the outer loop runs $n$ times and the inner loop runs an average of $n/2$ times.

---

## 3. Merge Sort (Divide and Conquer)

- **Method:**
    1. **Divide:** Conquers the problem recursively by repeatedly splitting the list in half until individual sublists contain only 1 element (which is inherently sorted).
    2. **Merge:** Combines the sorted sublists back together linearly by comparing their smallest front elements and copying them into a result list.

- **Complexity:** * The merging step takes linear time $\Theta(n)$ as it passes through the elements once.
    - Successively dividing the list in half creates $\Theta(\log n)$ recursive levels.
    - **Overall Complexity:** $\Theta(n \log n)$ , which represents the mathematical threshold for the fastest a comparison-based sort can be.

---

## 4. Summary of Complexities

- **Bogo Sort:** Unbounded

- **Bubble Sort:** $\Theta(n^2)$

- **Selection Sort:** $\Theta(n^2)$

- **Merge Sort:** $\Theta(n \log n)$

The lecture concludes by noting that evaluating algorithm efficiency asynchronously (using Big Theta notation for worst-case growth) allows developers to build and assess efficient programs independently of specific hardware or implementation details.