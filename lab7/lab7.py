# -------------------------------
# Divide & Conquer (O(n))
# -------------------------------

def divide_conquer(l, r, result):
    if l > r:
        return
    mid = (l + r) // 2
    result.append(mid)
    divide_conquer(l, mid - 1, result)
    divide_conquer(mid + 1, r, result)

result = []
divide_conquer(0, 5, result)
print(*result)

# -------------------------------
# Sort by reversed bits (O(n log n))
# -------------------------------
def sort_by_key_method(n):
    def rev_bits(x, k):
        r = 0
        for _ in range(k):
            r = (r << 1) | (x & 1)
            x >>= 1
        return r

    k = (n + 1).bit_length()
    arr = list(range(n + 1))
    arr.sort(key=lambda i: rev_bits(i, k))
    return arr


#print(*(sort_by_key_method(200)))