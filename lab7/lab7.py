def bitrev_dc(arr):
    if len(arr) <= 1:
        return arr
    
    evens = [x for x in arr if x % 2 == 0]
    odds  = [x for x in arr if x % 2 == 1]
    
    left  = bitrev_dc([x//2 for x in evens])
    right = bitrev_dc([x//2 for x in odds])
    
    # นำกลับมาคูณ 2 ให้เหมือนเดิม
    left  = [x*2 for x in left]
    right = [x*2+1 for x in right]
    
    return left + right

def bit_reversal_divide_conquer(n):
    arr = list(range(n+1))
    return bitrev_dc(arr)

##############################################

def reverse_bits(x, k):
    r = 0
    for _ in range(k):
        r = (r << 1) | (x & 1)
        x >>= 1
    return r

def bit_reversal(n):
    # หา k ให้ 2^k > n
    k = 1
    while (1 << k) <= n:
        k += 1

    result = []
    for i in range(1 << k):
        r = reverse_bits(i, k)
        if r <= n:
            result.append(r)
    return result

n = 5
print("==========DC==========")
print(bit_reversal_divide_conquer(n))
print("====================")
print(bit_reversal(n))
