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


# ===== Read input =====
with open("lab8/testcase/8.1.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]  # skip empty lines

chars = lines[0].split()
n, m = map(int, lines[1].split())
pattern = lines[2].split()
text = lines[3].split()

circle_text = text + text

print(circle_text)

# ===== Run KMP =====
pi, matches_lr = kmp_search(text, pattern)

# RL (search reversed)
rev_text = text[::-1]
_, matches_rev = kmp_search(rev_text, pattern)
matches_rl_1based = sorted(len(text) - i for i in matches_rev)

# ===== Run Naive =====
matches_naive_lr = naive_search(text, pattern)
rev_naive = naive_search(rev_text, pattern)
matches_naive_rl = sorted(len(text) - i for i in rev_naive)

# ===== แสดงผล (KMP) =====
print("=== KMP Algorithm ===")
print(" ".join(map(str, pi)))                    # prefix table
print(len(matches_lr) + len(matches_rev))        # จำนวนทั้งหมดที่เจอ

for pos in matches_lr:
    print(pos + 1, "LR")                         # ตำแหน่งเริ่ม (1-based)
for pos in matches_rl_1based:
    print(pos, "RL")                             # ตำแหน่งจบ (1-based)

# ===== แสดงผล (Naive) =====
#print("\n=== Naive Algorithm ===")
#print(len(matches_naive_lr) + len(matches_naive_rl))
#for pos in matches_naive_lr:
#    print(pos + 1, "LR")
#for pos in matches_naive_rl:
#    print(pos, "RL")
