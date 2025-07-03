# Algorithms Tasks 🧮

This repository contains my university algorithms assignment where I implemented two classic problems **from scratch**, without using built-in Python functions.

## 📌 Task Details
- **Project name**: Algorithms Tasks
- **Course**: Algorithms (COMXXX)
- **Grade weight**: 10 points
- **Rules**: No plagiarism, no built-in sort, max, etc.

## ✏️ Implemented Algorithms

### 1️⃣ Max Product of Three
Given a non-empty zero-indexed array A, find the maximal product of any triplet (P, Q, R).  
**Example:**
- Input: `[1,2,3,4]`
- Output: `24`

Includes:
- Pseudocode
- Algorithm analysis
- Time complexity calculation

---

### 2️⃣ Median of Two Sorted Arrays
Given two sorted arrays `nums1` and `nums2`, return the median of the merged sorted array.  
**Example:**
- Input: `nums1 = [1, 3]`, `nums2 = [2]`
- Output: `2`

Includes:
- Pseudocode
- Algorithm analysis
- Time complexity calculation

---

## 📊 Features
- Fully documented code with comments and docstrings.
- Simple, clear logic – no built-in Python shortcuts.
- Written for educational and learning purposes.

## ⚙️ Requirements
- Python 3.x

## 📂 Structure
```
python-algo/
├── Max-Product-of-Three Ali all .py    # Multiple approaches for max product (O(n) forward, count sort)
├── count-sort-max_all-ali.py          # Count sort implementation with pseudocode
├── max_Ahmed abo bakr.py              # Alternative max product implementation
├── max_formard                        # Forward approach implementation
├── Median-of-Two-Sorted-Arrays.py     # Bubble sort approach (O(n²))
├── median_sabry.py                    # Median implementation without built-ins
├── median_sabry_hib 2.py              # Median with input validation
├── median_merge                       # Merge sort approach for median
├── Pseudocode for median_sabry.txt    # Detailed pseudocode documentation
└── README.md                          # This file
```

## 🔧 Implementation Details

### Max Product of Three Approaches:
1. **Forward O(n) Approach**: Single pass through array tracking max and min values
2. **Count Sort Approach**: O(n) time complexity using counting sort for specific ranges
3. **Bubble Sort Approach**: O(n²) basic sorting approach

### Median of Two Sorted Arrays Approaches:
1. **Merge Approach**: Merging two sorted arrays and finding median
2. **Bubble Sort Approach**: O(n²) sorting of combined arrays
3. **Custom Implementation**: No built-in functions, manual array operations

## 📝 Algorithm Analysis

Both algorithms are implemented with detailed time complexity analysis and include multiple approaches ranging from O(n) to O(n²) depending on the method used. The implementations prioritize educational value and clarity over optimization.