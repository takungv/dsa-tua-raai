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
            matches.append(i - m + 1)
            j = pi[j - 1]
    return pi, matches


# ===== Read input =====
with open("lab8/testcase/8.7.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

chars = lines[0].split()
n, m = map(int, lines[1].split())
pattern = lines[2].split()
text = lines[3].split()

text_double = text + text  # วนรอบ 2 เท่า
length = len(text)

# ===== Run KMP =====
pi, matches_lr = kmp_search(text_double, pattern)
matches_lr = [pos for pos in matches_lr if pos < length]  # จำกัดภายใน text เดิม

# RL (search reversed)
rev_text = text_double[::-1]
_, matches_rev = kmp_search(rev_text, pattern)
matches_rl_1based = sorted(length - i for i in matches_rev if i < length)

# ===== Run Naive =====
matches_naive_lr = naive_search(text_double, pattern)
matches_naive_lr = [pos for pos in matches_naive_lr if pos < length]

rev_naive = naive_search(rev_text, pattern)
matches_naive_rl = sorted(length - i for i in rev_naive if i < length)

# ===== Remove duplicates =====
matches_lr = sorted(set(matches_lr))
matches_rl_1based = sorted(set(matches_rl_1based))
matches_naive_lr = sorted(set(matches_naive_lr))
matches_naive_rl = sorted(set(matches_naive_rl))

# ===== แสดงผล (KMP) =====
print("=== KMP Algorithm ===")
print(" ".join(map(str, pi)))
print(len(matches_lr) + len(matches_rl_1based))

for pos in matches_lr:
    print(pos + 1, "LR")
for pos in matches_rl_1based:
    print(pos, "RL")

# ===== แสดงผล (Naive) =====
print("\n=== Naive Algorithm ===")
print(len(matches_naive_lr) + len(matches_naive_rl))

for pos in matches_naive_lr:
    print(pos + 1, "LR")
for pos in matches_naive_rl:
    print(pos, "RL")
