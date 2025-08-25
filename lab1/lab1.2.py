def sieve(limit):
    """สร้าง list ของจำนวนเฉพาะ ≤ limit ด้วย Sieve of Eratosthenes"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    primes = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            primes.append(i)
    return primes


def prime_factors_sieve(x):
    """หาตัวประกอบเฉพาะของ x โดยใช้ sieve()"""
    factors = []
    primes = sieve(int(x**0.5))  # เรียกใช้ sieve เพื่อได้ prime ≤ √x

    for p in primes:
        while x % p == 0:
            factors.append(p)
            x //= p
    if x > 1:  # ถ้าเหลือ x > 1 แปลว่า x เป็น prime ตัวใหญ่
        factors.append(x)
    return factors


def FindGCD2(m, n):
    """หาค่า GCD โดยใช้ sieve + prime factorization"""
    factors_m = prime_factors_sieve(m)
    factors_n = prime_factors_sieve(n)

    common = []
    for f in factors_m:
        if f in factors_n:
            common.append(f)
            factors_n.remove(f)
    
    gcd_val = 1
    for f in common:
        gcd_val *= f
    return gcd_val


# ตัวอย่างการรัน
m, n = 653184188245, 758331017965
print("FindGCD2:", FindGCD2(m, n))