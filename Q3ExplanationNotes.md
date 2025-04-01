# Longest Common Substring Approach

I assumed:
1) There can be multiple longest common substrings, and I will report any one of them
2) Case sensitivity, otherwise, both strings can be lowercased before proceeding.

## Brute Frce Approach

1. **First thought**: We can use an exhaustive brute-force approach where, in a double loop, we:
   - Search every substring of `s1` → **O(n²)**
   - Assign this to a temporary substring, something like `substring = s1[i:j]` → **O(n)**
   - Check if it exists in `s2` → **O(m)**

   This gives an average case time complexity of **O(n³ * m)**. Very inefficient. There are other methods too.

---

## Dynamic Programming (DP) Approach

A very similar problem is **Longest Common Subsequence (LCS)**. The approach involves:

1. **Two cases**:
   - **Case 1**: If the last letters of both strings match (`s1[-1] == s2[-1]`), then we know this character is part of the LCS. So, we recurse on `1 + LCS(s1[:-1], s2[:-1])`.
   - **Case 2**: Otherwise, we remove the last letter from either string and recurse:
     - `LCS(s1, s2[:-1])`
     - `LCS(s1[:-1], s2)`

2. **Example Analysis**:
   - Consider `s1 = ababbacdce` & `s2 = haababadeedc`.
   - The last letters do not match.
   - However, the last `e` in `s1` might match with the second-last `d` in `s2` (it does not).
   - The second-last `c` in `s1` might match with the last `c` in `s2` (it does).
   - If we removed both the last `e` and last `c` from `s1` and `s2`, we would miss this match!
   - Hence, we recurse on `max(LCS(s1, s2[:-1]), LCS(s1[:-1], s2))`.

3. **Bottom-up DP approach**:
   - Use an **n × m matrix** for LCS.
   - Each block `(i, j)` in this matrix represents the LCS length up to the `i`-th element in `s1` and the `j`-th element in `s2`.
   - To find out each value `M[i][j]`, modifying from the recursive approach:
     - If `s1[i] == s2[j]`, we add `1` to `M[i-1][j-1]` (because `M[i-1][j-1]` is LCS of `s1[:-1]`, `s2[:-1]`).
     - Otherwise, we take `max(M[i][j-1], M[i-1][j])` (because it is the max LCS of `(s1, s2[:-1])` and `(s1[:-1], s2)`).

---

## Applying this to **Longest Common Substring**

With **substrig**, whenever `s1[-1] != s2[-1]`, the substring **ends there**, as it is not contiguous. This requires modifying our bottom-up approach:

- If `s1[-1] == s2[-1]`, we know we have found at least one substring of length `1`. Similar to LCS, we update:
  - If `s1[i] == s2[j]`, we add `1` to `M[i-1][j-1]`.
- Otherwise, unlike LCS where we check discontinuity matches, we **reset to 0**.
- Additionally, we must handle the base case: comparing against an empty string results in a length of `0`.