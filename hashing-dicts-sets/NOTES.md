# Hashing, Dictionaries & Sets — Concept Notes

Notes for **Amazon SDE 2** (and similar) interviews: focus is on **concepts you use while coding**—how hash tables work, when to pick dict vs set, complexity, pitfalls, and tradeoffs. No walkthroughs of specific coding problems.

---

## 0. Why this topic matters at SDE 2 level

Interviewers expect you to **choose** the right structure, **state assumptions** (uniform hashing, load factor), and **discuss tradeoffs** (memory vs speed, worst case vs average). You should be able to explain **why** lookups are fast, **what breaks** hash tables (bad keys, collisions), and how Python’s `dict` / `set` relate to the abstract **hash map** / **hash set** you’d design on a whiteboard.

---

## 1. What is Hashing?

**Hashing** maps data of arbitrary size to a **fixed-size** value (a **hash** or **hash code**) using a **hash function**. That value is used to pick a **bucket** (array index), usually `hash(key) % bucket_count`, so you can store and look up values without scanning the whole collection.

### Hash function

A hash function takes a **key** and returns an **integer** (conceptually an index into buckets).

**Properties of a good hash function:**

- **Deterministic:** Same key → same hash (for the lifetime of the structure; Python’s `hash()` for strings is salted per process for security, but within one run it’s stable for dict/set use).
- **Uniform distribution:** Keys spread across buckets so collisions stay rare.
- **Fast:** O(1) relative to key size for typical keys.

### Python’s built-in `hash`

Only **hashable** (immutable) types can be hashed: `int`, `float`, `str`, `tuple` (if all elements are hashable), `frozenset`, `bool`, `None`. **Mutable** types (`list`, `dict`, `set`) are **not** hashable—they cannot be dict keys or set elements.

---

## 2. Hash Table (underlying structure)

A hash table is an **array of buckets**. To store a key–value pair:

1. Compute bucket index from the key’s hash (and table size).
2. Place the pair in that bucket (handling collisions—see below).
3. Lookup repeats the same index computation.

Retrieval is **average O(1)** because you jump directly to a bucket instead of scanning all keys.

---

## 3. Collisions

A **collision** is two different keys mapping to the **same bucket**.

### Chaining (separate chaining)

Each bucket holds a **list** (or tree) of entries. Lookup: go to bucket, then scan the chain for the exact key.

- **Pros:** Simple; no hard “full table” limit.
- **Cons:** Extra pointers; worst case O(n) if everything lands in one bucket.

### Open addressing

All entries live **in** the table. On collision, **probe** for another slot (linear, quadratic, or double hashing).

- **Pros:** No separate chains; can be cache-friendly.
- **Cons:** Clustering; table can fill; deletion is trickier.

**Interview point:** Know both names and that **average** behavior stays O(1) with a good function and load factor; **worst** case is O(n).

---

## 4. Load factor & resizing

**Load factor** α = (number of entries) / (number of buckets).

- Too high → more collisions → slower operations.
- Typical implementations **resize** (e.g. double bucket count) and **rehash** all entries when α crosses a threshold.

Python’s `dict` grows when the table is roughly **two-thirds full** (≈ α ≈ 2/3). Resizing is why single inserts are **amortized** O(1), not every insert strictly O(1).

---

## 5. Amortized O(1) — concept

Most inserts/updates are O(1). Occasionally the table **resizes**—an O(n) pass to rehash everything. Spread over many operations, the **average cost per insert** is still constant. That is **amortized** O(1). Be ready to say: “Worst single operation can be O(n) on resize; over a sequence, average is O(1).”

---

## 6. Python `dict` (hash map)

A `dict` maps **hashable keys** to **values**. Internally it is a hash table with optimizations (e.g. compact layout, open addressing in CPython).

### Operations (average vs worst)

| Operation        | Average | Worst (pathological) |
| ---------------- | ------- | --------------------- |
| Insert / update  | O(1)    | O(n)                  |
| Lookup / `in`    | O(1)    | O(n)                  |
| Delete           | O(1)    | O(n)                  |
| Iterate all keys | O(n)    | O(n)                  |

Worst case assumes many collisions or adversarial keys; **in practice** dict behaves like O(1) for typical workloads.

### `dict` vs `defaultdict` vs `Counter`

| Type           | Concept |
| -------------- | ------- |
| `dict`         | General mapping; missing key raises `KeyError` (use `.get(k, default)` to avoid). |
| `defaultdict`  | Factory supplies a default for missing keys—useful when every key maps to a mutable aggregate (e.g. list) without manual `if key not in d`. |
| `Counter`      | Specialized for counts; conceptually a dict from element → integer count. |
| `OrderedDict`  | Historically for order; since **Python 3.7+**, plain `dict` preserves **insertion order** as part of the language spec. |

### Dict views: `.keys()`, `.values()`, `.items()`

These return **dynamic views**: they reflect the dict as it changes. Iterating while **adding** keys can be OK; **deleting** during iteration needs care. Conceptually: views are not independent snapshots.

### Equality vs identity for keys

Lookups use **equality** (`==`) after matching **hash**. Two objects that compare equal must have the **same hash** (Python enforces this for user-defined classes if you implement `__eq__` and `__hash__`). **Never mutate** an object that is already a dict key in a way that changes its hash or equality—behavior is undefined and can break the table.

---

## 7. Python `set` (hash set)

A `set` stores **unique hashable elements**—no separate value. Same collision and hashing story as dict keys.

### Set algebra (concept)

- **Union** `|` — elements in either set.
- **Intersection** `&` — in both.
- **Difference** `-` — in first, not in second.
- **Symmetric difference** `^` — in exactly one.

Complexity is linear in the sizes of the operands for typical implementations.

**Use a set when** you only need **membership** and **uniqueness**, not key→value mapping.

---

## 8. `frozenset` and composite keys

**`frozenset`** is an **immutable** set, therefore **hashable**. Use it (or **tuple**) when you need a **set-like or multi-part key**: e.g. grouping by a set of tags, or using `(origin, dest)` as one key. A normal `set` cannot be a dict key because it is mutable.

---

## 9. Hashable vs unhashable — rules

| Hashable (if contents allow) | Unhashable |
| ---------------------------- | ---------- |
| `int`, `float`, `bool`, `None`, `str` | `list` |
| `tuple` of hashables | `dict` |
| `frozenset` | `set` |

**Rule:** Dict keys and set elements must be hashable. **Mutating** a key after insertion is a serious bug.

---

## 10. When to use what (decision lens)

| Need | Structure | Reasoning |
| ---- | --------- | --------- |
| Key → value | `dict` | O(1) average lookup by key. |
| Counts / frequencies | `Counter` or `dict` | Integer values per key; Counter adds convenience. |
| Group many values per key | `defaultdict(list)` (or similar) | Avoid repetitive “if key not in dict” boilerplate. |
| Only uniqueness / membership | `set` | O(1) average `in`; dedup. |
| Key that behaves like a set | `frozenset` | Hashable. |
| Preserve insertion order | `dict` (3.7+) | Order is part of language semantics. |

**Heuristic:** If you repeatedly ask “is **X** already seen?” while scanning, a **set** or **dict** avoids O(n) list scans.

---

## 11. Designing a hash map (conceptual — whiteboard)

Without libraries, a minimal API is often **put(key, value)**, **get(key)**, **remove(key)**.

**Conceptual pieces:**

1. **Bucket array** + **hash function** (mod array length).
2. **Collision policy** — chaining vs open addressing; state a choice and one pro/con.
3. **Resize** when load factor too high; **rehash** all entries into a larger array.
4. **get** must match **put** on equality: same key identity/equality rules as language dict.

SDE 2: you may also mention **concurrency**—a simple hash map is **not** thread-safe without locks or concurrent data structures; Python’s GIL serializes many bytecodes but logical races still exist in multi-threaded code.

---

## 12. Limitations & pitfalls (coding + interviews)

- **Worst-case O(n)** if all keys collide or hashes are adversarial.
- **Space:** Hash tables need extra slots; load factor trades memory vs speed.
- **No ordering by value** — dict order is insertion order, not sorted order; use **sorted()** or a **tree map** concept if you need sorted keys (different structure).
- **Floating-point keys** — equality quirks can surprise you; usually avoid unless you know the domain.
- **`KeyError` vs `.get()`** — explicit failure vs default; choose for API clarity.
- **Iteration order** — don’t rely on order across different dicts built differently unless you sort keys explicitly.

---

## 13. Conceptual patterns (no named problems)

These are **ways of thinking**, not specific LeetCode titles:

1. **Frequency / histogram** — Map key → count; compare two maps for multiset equality; find dominant or rare keys.
2. **Complement / inverse lookup** — Store what you’ve seen so the “partner” of each new item is O(1) to test (conceptually: `target - x`, matching pair, etc.).
3. **Canonical key for grouping** — Map many objects to one representative key (e.g. sorted tuple of characters, sorted tuple of numbers) so equivalent items share a bucket.
4. **Sliding window with counts** — Dict as multiset over the window; increment on enter, decrement on leave; track how many distinct keys or nonzero counts.
5. **Set algebra on collections** — Reduce problems to union/intersection/difference when the question is about overlap or uniqueness across large inputs.

---

## 14. Complexity cheat sheet

| Operation   | dict (avg) | set (avg) | list (compare) |
| ----------- | ---------- | --------- | -------------- |
| Insert      | O(1)       | O(1)      | O(1) append      |
| Lookup / `in` | O(1)     | O(1)      | O(n)           |
| Delete      | O(1)       | O(1)      | O(n)           |
| Iterate     | O(n)       | O(n)      | O(n)           |

**Takeaway:** Dict and set give **expected constant-time** membership and updates; lists require **linear** scan for membership.

---

## 15. Related topics (brief pointers)

- **Consistent hashing** — Distributed systems; different problem from one-machine dicts, but “hash ring” often comes up for SDE2 system design.
- **Bloom filters** — Probabilistic membership; space-efficient; **false positives** possible—not a replacement for exact dict/set.
- **Trie vs hash map** — Prefix structure vs exact key; different time/space tradeoffs for string keys.

These are optional depth for “hashing-adjacent” discussions beyond core Python dict/set.
