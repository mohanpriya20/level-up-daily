# Time & Space Complexity

How **runtime** and **extra memory** grow with input size **n** (asymptotic analysis).

# Asymptotic Notation

Asymptotic notation is **a mathematical tool used in computer science to analyze an algorithm's efficiency by describing how its time or space requirements grow as the input size approaches infinity**

---

## 1. Notation


| Symbol      | Meaning                                              |
| ----------- | ---------------------------------------------------- |
| **O(f(n))** | Upper bound (worst-case growth not worse than f(n)). |
| **Ω(f(n))** | Lower bound.                                         |
| **Θ(f(n))** | Tight: same growth as f(n) (both O and Ω).           |


Drop constants and low-order terms: `5n² + 100n` → **O(n²)**. Any log base → **O(log n)**.

“Big O” in discussion usually means **worst-case** unless stated otherwise.

---

## 2. Time classes (fast → slow)


| Class        | Note                                |
| ------------ | ----------------------------------- |
| O(1)         | Constant                            |
| O(log n)     | Halving each step                   |
| O(n)         | Single pass                         |
| O(n log n)   | Efficient sort, many D&C algorithms |
| O(n²)        | Typical nested loops on n           |
| O(n³)        | Triple nested                       |
| O(2ⁿ), O(n!) | Only feasible for small n           |


---

## 3. How to read code


| Pattern                | Time                                                     |
| ---------------------- | -------------------------------------------------------- |
| Sequential blocks      | Sum; keep **dominant** term only.                        |
| Loop over n, O(1) body | O(n)                                                     |
| Loop body O(k)         | O(n·k)                                                   |
| Nested n × n           | O(n²) (watch: some patterns are O(n), e.g. two pointers) |
| Branches               | Worst branch dominates for upper bound.                  |
| Recursion              | Write recurrence → solve (§7) or recursion tree.         |


---

## 4. Space


| Term          | Meaning                                                            |
| ------------- | ------------------------------------------------------------------ |
| **Auxiliary** | Extra beyond input (temps, stack, new structures).                 |
| **Input**     | Often excluded unless problem says “in-place” / “excluding input”. |


Recursion depth **d**, O(1) per frame → **O(d)** stack. Full array copy → **O(n)** extra.

---

## 5. Worst, best, average, amortized


| Case          | Meaning                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| **Worst**     | Input that maximizes work (e.g. quicksort always bad pivot → O(n²)).                                      |
| **Best**      | Easiest input (e.g. already sorted where that helps).                                                     |
| **Average**   | Expected over random input or random choices (e.g. randomized quicksort → O(n log n) expected).           |
| **Amortized** | Rare expensive step (e.g. array **double**); spread over many cheap ops → e.g. **amortized O(1)** append. |


---

## 6. Structure operations (typical / average)


| Structure     | Access | Search   | Insert   | Delete   | Space |
| ------------- | ------ | -------- | -------- | -------- | ----- |
| Array (index) | O(1)   | O(n)     | O(n)*    | O(n)*    | O(n)  |
| Linked list   | O(n)   | O(n)     | O(1)*    | O(1)*    | O(n)  |
| Hash table    | —      | O(1)†    | O(1)†    | O(1)†    | O(n)  |
| BST balanced  | —      | O(log n) | O(log n) | O(log n) | O(n)  |
| BST skewed    | —      | O(n)     | O(n)     | O(n)     | O(n)  |


 Known node / ends; † average; hash & BST worst can degrade to O(n).

---

## 7. Master theorem (D&C)

**T(n) = a·T(n/b) + f(n)**  
**a** subproblems, each size **n/b**; **f(n)** = divide + combine per level.

Compare **n^(log_b a)** with **f(n)**:

1. **f(n)** polynomially smaller than **n^(log_b a)** → **Θ(n^(log_b a))**
2. **f(n) = Θ(n^(log_b a))** → **Θ(n^(log_b a) log n)**
3. **f(n)** polynomially larger (+ regularity) → **Θ(f(n))**

Examples: **2T(n/2) + O(n)** → Θ(n log n) (merge sort). **T(n/2) + O(1)** → O(log n) (binary search).  
Unsure: **recursion tree**, sum per level.

---

## 8. Halving / doubling

- Problem size **halved** each step → **O(log n)** steps.
- Table **doubled** when full → **O(n)** total copy **amortized** over n inserts.

---

## 9. Pitfalls

- Two sizes **n** and **m**: **O(n + m)** vs **O(n·m)**.
- **Membership in list** inside loop over n → **O(n²)**.
- **String +=** in loop → **O(n²)**; use list + `**join`**.
- **Sort** then scan → include **O(n log n)** for sort.
- **dict/set**: say **average** O(1) vs **worst** O(n) if relevant.
- **Deep recursion** → stack limits; consider iterative.

---

## 10. Stating complexity

1. Define **n** (and **m**, etc.).
2. **Time:** dominant loops, recursion, sorts.
3. **Space:** auxiliary vs input; stack; extra structures.
4. Say **worst / average / amortized** if it matters.

---

## 11. Beyond basics

- **Akra–Bazzi** — uneven splits.
- **Potential method** — formal amortized proofs.
- **Cache / I/O model** — large external data.

After each problem: **what is n? what dominates time? what extra space?**