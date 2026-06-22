# Rough Notes: Merging Two Sorted Lists in Python

This document contains comprehensive notes, optimal algorithms, and code snippets for merging two sorted lists in Python. It covers the naive approach, the optimal two-pointer iterative technique, standard library lazy evaluation using `heapq.merge`, the in-place LeetCode variation, a detailed discussion on edge cases, and robust unit tests.

---

## 1. Problem Statement

### Definition
Given two integer lists, `list1` and `list2`, both sorted in non-decreasing order, merge them into a single, fully sorted list. The resulting list must also be sorted in non-decreasing order.

### Input/Output Examples

* **Example 1 (Standard Case)**:
  * **Input**: `list1 = [1, 3, 5]`, `list2 = [2, 4, 6]`
  * **Output**: `[1, 2, 3, 4, 5, 6]`

* **Example 2 (Empty Lists)**:
  * **Input**: `list1 = []`, `list2 = [1, 2]`
  * **Output**: `[1, 2]`

* **Example 3 (Duplicate Elements)**:
  * **Input**: `list1 = [1, 2, 2]`, `list2 = [2, 3, 4]`
  * **Output**: `[1, 2, 2, 2, 3, 4]`

* **Example 4 (Negative Numbers & Different Lengths)**:
  * **Input**: `list1 = [-10, -5]`, `list2 = [-20, 0, 5, 10, 15]`
  * **Output**: `[-20, -10, -5, 0, 5, 10, 15]`

---

## 2. Naive Approach: Concatenation and Sorting

### Concept
The simplest way to solve this problem is to ignore the pre-sorted property of the input lists. We can concatenate the two lists using the `+` operator and then sort the resulting list using Python's built-in `sorted()` function or the `.sort()` method.

### Python Code
```python
def merge_naive(list1: list[int], list2: list[int]) -> list[int]:
    # Concatenate the lists and sort the combined list
    combined = list1 + list2
    combined.sort()
    return combined
```

### Why it is Suboptimal
* **Ignores Sorted Structure**: This approach treats the inputs as completely unsorted arrays, throwing away the existing order. 
* **Redundant Work**: It performs comparison operations to sort elements that were already in the correct relative order.
* **Higher Time Complexity**: Sorting a collection of size $N+M$ from scratch takes $O((N+M) \log(N+M))$ operations, whereas we can achieve linear time $O(N+M)$ by taking advantage of the pre-sorted lists.

### Complexity Analysis
* **Time Complexity**: $\mathcal{O}((N+M) \log(N+M))$, where $N = \text{len}(list1)$ and $M = \text{len}(list2)$. Python's sorting algorithm (Timsort) has a worst-case time complexity of $\mathcal{O}(L \log L)$ for a list of length $L$. Here, $L = N+M$.
* **Space Complexity**: $\mathcal{O}(N+M)$ to store the concatenated list of size $N+M$. Timsort also requires up to $\mathcal{O}(N+M)$ auxiliary space in the worst case.

---

## 3. Optimal Iterative Approach: Two-Pointer Technique

### Concept & Step-by-Step Walkthrough
Since both inputs are already sorted, we can build the merged list in a single linear pass using two pointers (indices), `i` and `j`, starting at index 0 of `list1` and `list2` respectively.

1. **Initialization**:
   * Set `i = 0` (pointer for `list1`)
   * Set `j = 0` (pointer for `list2`)
   * Create an empty list `merged = []`
2. **Comparison Loop**:
   * While `i < len(list1)` and `j < len(list2)`:
     * Compare the elements at the current pointer positions: `list1[i]` and `list2[j]`.
     * If `list1[i] <= list2[j]`, append `list1[i]` to `merged` and increment `i` by 1.
     * Else, append `list2[j]` to `merged` and increment `j` by 1.
   * *Note: Using `<=` instead of `<` ensures the sorting remains stable (maintaining the original order of duplicate values).*
3. **Appends Residual Elements**:
   * When the loop terminates, one list has been fully traversed.
   * Append any remaining elements of `list1` (from index `i` to the end) to `merged`.
   * Append any remaining elements of `list2` (from index `j` to the end) to `merged`.
   * Since one list is already exhausted, only one of these slice extensions will have an effect.

### Python Code
```python
def merge_two_pointer(list1: list[int], list2: list[int]) -> list[int]:
    merged = []
    i, j = 0, 0
    n, m = len(list1), len(list2)
    
    # Iterate through both lists comparing elements
    while i < n and j < m:
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
            
    # Append any remaining elements from either list
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged
```

### Complexity Analysis
* **Time Complexity**: $\mathcal{O}(N+M)$. We visit each element of `list1` and `list2` exactly once. Each append operation is $\mathcal{O}(1)$ amortized. Slicing and extending the remaining list takes time proportional to the number of residual elements, which is at most $\mathcal{O}(N+M)$.
* **Space Complexity**: $\mathcal{O}(N+M)$ because we construct and return a new list containing all $N+M$ elements. The auxiliary space (extra memory used besides the output list) is $\mathcal{O}(1)$ as we only maintain a few integer pointers and length variables.

---

## 4. Pythonic / Advanced Library Approach: `heapq.merge`

### Concept & Under the Hood Mechanics
Python's standard library provides a highly optimized utility for merging sorted iterables: `heapq.merge`. 

* **Min-Heap Implementation**: Under the hood, `heapq.merge` uses a min-heap (binary heap) to merge multiple sorted inputs. For $K$ input iterables, it maintains a min-heap containing the current element from each iterable. At each step, it pops the smallest element from the heap and pushes the next element from the iterator that provided the popped element.
* **Heap size**: When merging just two sorted lists ($K = 2$), the heap size is at most 2. Pushing and popping from a heap of size 2 is extremely fast and takes $\mathcal{O}(\log 2) \approx \mathcal{O}(1)$ constant time.
* **Lazy Evaluation (Generator)**: Instead of constructing and returning a fully merged list in memory, `heapq.merge` returns a **generator (iterator)** that yields elements lazily on-demand.

### Why this is Highly Memory Efficient
For standard in-memory lists, `heapq.merge` can be wrapped in `list()` to produce a merged list. However, its real power lies in handling **huge or streamed datasets** (e.g., merging two 50GB files containing sorted integers, database logs, or API streams):
1. **No full load**: We do not need to load the entire combined dataset into RAM.
2. **Streaming**: We can stream elements line-by-line from files or generators, feed them into `heapq.merge`, and write them directly to a destination output file.
3. **Auxiliary Space**: It uses only $\mathcal{O}(K)$ auxiliary space (where $K$ is the number of iterables). For two files, $K = 2$, meaning it requires $\mathcal{O}(1)$ auxiliary space regardless of how large the files are.

### Python Code
```python
import heapq
from typing import Iterator

# Standard in-memory wrapper
def merge_heapq_list(list1: list[int], list2: list[int]) -> list[int]:
    return list(heapq.merge(list1, list2))

# Streaming/Lazy Generator example
def merge_heapq_lazy(list1: list[int], list2: list[int]) -> Iterator[int]:
    # Returns a generator. Elements are evaluated on-demand.
    return heapq.merge(list1, list2)
```

---

## 5. LeetCode Variation: In-Place Merge (LeetCode 88)

### Problem Definition
In this variation, instead of returning a new list, we are asked to merge `nums2` into `nums1` **in-place**.
* `nums1` has an overall length of `m + n`, where the first `m` elements are sorted integers, and the last `n` elements are set to `0` as placeholders.
* `nums2` has a length of `n` with sorted integers.
* The merge must be performed in-place within `nums1` without allocating additional list space.

### Intuition: Back-to-Front Three-Pointer Technique
If we try to merge starting from the beginning (index 0), we risk overwriting valid, unmerged elements in `nums1`, or we must shift elements which would degrade the performance to $\mathcal{O}(N \cdot (M+N))$ time.

To solve this optimally in $\mathcal{O}(1)$ space, we merge **back-to-front** (starting with the largest numbers):
1. Since the end of `nums1` (the last `n` slots) is filled with unused placeholder zeros, we can safely overwrite them.
2. We place three pointers:
   * `p1 = m - 1` (points to the last active element in `nums1`)
   * `p2 = n - 1` (points to the last element in `nums2`)
   * `p = m + n - 1` (points to the write location at the end of `nums1`)
3. Compare `nums1[p1]` and `nums2[p2]`. Place the larger element at `nums1[p]` and decrement the corresponding pointer (`p1` or `p2`) and the write pointer `p`.
4. Continue this until `p2 < 0`:
   * If `p1` becomes negative first, we copy the remaining elements from `nums2` into `nums1`.
   * If `p2` becomes negative first, we can stop immediately! Any remaining elements in `nums1` are already in their correct, sorted positions at the front of the array.

### Python Code
```python
def merge_inplace(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1      # Pointer for active elements in nums1
    p2 = n - 1      # Pointer for elements in nums2
    p = m + n - 1   # Pointer for write index in nums1
    
    # Merge elements from back to front
    while p2 >= 0:
        # If nums1 still has elements and nums1's element is greater
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
```

### Complexity Analysis
* **Time Complexity**: $\mathcal{O}(M+N)$. We perform a single backward pass through both arrays, doing constant-time operations at each step.
* **Space Complexity**: $\mathcal{O}(1)$ auxiliary space, since the merge is performed in-place within the existing capacity of `nums1`.

---

## 6. Edge Cases

When designing or testing sorted-merge algorithms, it is essential to handle and verify the following edge cases:

| Edge Case | Scenario | Behavior |
| :--- | :--- | :--- |
| **Empty Lists** | Both `list1` and `list2` are empty. | Returns `[]` immediately without errors. |
| **One Empty List** | One list is empty, other has elements (e.g., `list1 = []`, `list2 = [1, 2, 3]`). | The pointer loop exits immediately, and the non-empty list is appended in $\mathcal{O}(1)$ via slices. |
| **Single Element Lists** | Lists with only one element (e.g., `[5]` and `[3]`). | Correctly compares the single values and returns `[3, 5]`. |
| **Duplicate Values** | Values occur multiple times within a list or across both lists. | The use of `<=` preserves stable sorting, maintaining the correct relative order of identical keys. |
| **Drastically Different Lengths** | One list is tiny, the other is huge (e.g., `[1]` and `[2, 3, ..., 1000]`). | The `while` loop terminates after 1 comparison, and the remainder of the long list is sliced and appended in $\mathcal{O}(1)$ slice time. |
| **Negative Numbers** | Inputs contain negative integers (e.g., `[-10, -5]` and `[-20, 0]`). | Comparisons correctly order negative values according to algebraic order. |

---

## 7. Comprehensive Unit Tests

The following unit tests can be run using `pytest` or executed as a standalone script using Python's built-in `assert` statements.

```python
import pytest
import heapq

# --- Implementations for testing ---

def merge_naive(list1, list2):
    combined = list1 + list2
    combined.sort()
    return combined

def merge_two_pointer(list1, list2):
    merged = []
    i, j = 0, 0
    n, m = len(list1), len(list2)
    while i < n and j < m:
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

def merge_heapq_list(list1, list2):
    return list(heapq.merge(list1, list2))

def merge_inplace(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


# --- Pytest Test Suite ---

@pytest.mark.parametrize("merge_func", [merge_naive, merge_two_pointer, merge_heapq_list])
def test_standard_merge(merge_func):
    """Test standard merging of two sorted lists of equal or similar lengths."""
    assert merge_func([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_func([10, 20, 30], [15, 25, 35]) == [10, 15, 20, 25, 30, 35]

@pytest.mark.parametrize("merge_func", [merge_naive, merge_two_pointer, merge_heapq_list])
def test_empty_lists(merge_func):
    """Test with completely empty lists or one empty list."""
    assert merge_func([], []) == []
    assert merge_func([], [1, 2, 3]) == [1, 2, 3]
    assert merge_func([1, 2, 3], []) == [1, 2, 3]

@pytest.mark.parametrize("merge_func", [merge_naive, merge_two_pointer, merge_heapq_list])
def test_duplicates(merge_func):
    """Test that duplicates within and across lists are handled stably and correctly."""
    assert merge_func([1, 2, 2, 3], [2, 2, 4]) == [1, 2, 2, 2, 2, 3, 4]
    assert merge_func([5, 5, 5], [5, 5]) == [5, 5, 5, 5, 5]

@pytest.mark.parametrize("merge_func", [merge_naive, merge_two_pointer, merge_heapq_list])
def test_drastically_different_lengths(merge_func):
    """Test merging lists with major length disparities."""
    assert merge_func([1], [2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert merge_func([2, 3, 4, 5, 6, 7, 8, 9, 10], [1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.mark.parametrize("merge_func", [merge_naive, merge_two_pointer, merge_heapq_list])
def test_negative_numbers(merge_func):
    """Test merging sorted lists with negative numbers."""
    assert merge_func([-10, -5, 0], [-20, -15, -2, 5]) == [-20, -15, -10, -5, -2, 0, 5]


# --- In-Place Merge (LeetCode 88) Tests ---

def test_inplace_merge_standard():
    nums1 = [1, 2, 3, 0, 0, 0]
    merge_inplace(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

def test_inplace_merge_empty_nums2():
    nums1 = [1]
    merge_inplace(nums1, 1, [], 0)
    assert nums1 == [1]

def test_inplace_merge_empty_nums1():
    nums1 = [0]
    merge_inplace(nums1, 0, [1], 1)
    assert nums1 == [1]

def test_inplace_merge_duplicates():
    nums1 = [1, 2, 2, 0, 0, 0, 0]
    merge_inplace(nums1, 3, [2, 2, 3, 4], 4)
    assert nums1 == [1, 2, 2, 2, 2, 3, 4]

def test_inplace_merge_all_elements_smaller():
    nums1 = [10, 20, 30, 0, 0, 0]
    merge_inplace(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 10, 20, 30]


# --- Standalone Execution ---
if __name__ == "__main__":
    # If run directly, execute the tests using basic assert statements
    print("Running basic assertions for merge_two_pointer...")
    assert merge_two_pointer([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_two_pointer([], []) == []
    assert merge_two_pointer([], [1, 2]) == [1, 2]
    assert merge_two_pointer([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]
    assert merge_two_pointer([-5, 10], [-10, 0, 20]) == [-10, -5, 0, 10, 20]
    
    print("Running basic assertions for merge_inplace...")
    n1 = [1, 2, 3, 0, 0, 0]
    merge_inplace(n1, 3, [2, 5, 6], 3)
    assert n1 == [1, 2, 2, 3, 5, 6]
    
    print("All basic assertion tests passed successfully!")
```
