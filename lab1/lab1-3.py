def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# ตัวอย่าง
m, n = 36, 48
print(gcd_euclid(m, n))