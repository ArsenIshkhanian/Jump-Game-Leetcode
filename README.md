# 🦘 Jump Game - LeetCode (Medium)

## 📘 Problem

This repository contains my Python solution to the **"Jump Game"** problem from LeetCode.

- **Difficulty:** Medium  
- **Topic:** 1D Dynamic Programming / Greedy  
- **Language:** Python  
- **LeetCode Link:** [Jump Game](https://leetcode.com/problems/jump-game/)

### Problem Summary:
You are given an array of non-negative integers, where each element represents your maximum jump length at that position.  
Determine if you can reach the last index starting from the first.

---

## 🧠 Approach

This solution uses a **recursive backtracking** approach with memoization (via list tracking):

- At each step, the function tries jumping from the current index up to the value at that index.
- It recursively checks each reachable index to see if the end is reachable.
- If a sublist has already been visited (i.e., memoized), it is skipped to avoid redundant work.

> ⚠️ This recursive solution works correctly for small inputs, but is **not optimized for large datasets** due to high time complexity (exponential in worst case).  
> An optimal approach would use **greedy** or **dynamic programming** to achieve linear time.

