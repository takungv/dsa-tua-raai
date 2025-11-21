# ===== Naive Search =====
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)
    return matches


# ===== KMP Prefix =====
def compute_prefix(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi


# ===== KMP Search =====
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix(pattern)
    matches = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)  # 0-based index
            j = pi[j - 1]
    return pi, matches


# ===== Circular KMP LR =====
def circular_kmp_lr(text, pattern):
    n = len(text)
    text_doubled = text + text
    pi = compute_prefix(pattern)
    matches = []
    j = 0

    for i in range(len(text_doubled)):
        while j > 0 and text_doubled[i] != pattern[j]:
            j = pi[j - 1]
        if text_doubled[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            start = i - len(pattern) + 1
            if start < n:   # ต้องเริ่มใน text จริงเท่านั้น
                matches.append(start)
            j = pi[j - 1]

    return matches  # 0-based


# ===== Circular KMP RL =====
def circular_kmp_rl(text, pattern):
    rev_text = text[::-1]
    n = len(text)
    rev_double = rev_text + rev_text
    pi = compute_prefix(pattern)

    matches = []
    j = 0

    for i in range(len(rev_double)):
        while j > 0 and rev_double[i] != pattern[j]:
            j = pi[j - 1]
        if rev_double[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            end = i - len(pattern) + 1
            if end < n:
                real_pos = n - end     # กลับตำแหน่งจริง (1-based ตรงนี้)
                matches.append(real_pos)
            j = pi[j - 1]

    return sorted(matches)


# ===== Read input =====
with open("lab8/testcase/8.7.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

chars = lines[0].split()
n, m = map(int, lines[1].split())
pattern = lines[2].split()
text = lines[3].split()


# ===== Normal KMP =====
pi, matches_lr = kmp_search(text, pattern)

# ===== Circular LR / RL =====
circular_lr = circular_kmp_lr(text, pattern)
circular_rl = circular_kmp_rl(text, pattern)


# ===== Output =====
print("=== KMP Algorithm (Circular Included) ===")
print(" ".join(map(str, pi)))        # prefix table

total = len(circular_lr) + len(circular_rl)
print(total)

# Circular LR
for pos in circular_lr:
    print(pos + 1, "LR")

# Circular RL
for pos in circular_rl:
    print(pos, "RL")
