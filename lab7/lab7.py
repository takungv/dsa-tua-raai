# -------------------------------
# Divide & Conquer (O(n))
# -------------------------------
def divide_and_conquer_method(n):
    def bitrev_order(k):
        if k == 0:
            return [0]
        prev = bitrev_order(k - 1)
        return [2 * x for x in prev] + [2 * x + 1 for x in prev]

    k = (n + 1).bit_length()
    order = bitrev_order(k)
    return [x for x in order if x <= n]


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


print(*(divide_and_conquer_method(10000)))
#print(*(sort_by_key_method(200)))