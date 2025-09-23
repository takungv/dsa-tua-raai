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


def prime_factors_sieve(x, primes):
    """หาตัวประกอบเฉพาะของ x โดยใช้ primes ที่เตรียมไว้"""
    factors = []
    for p in primes:
        if p * p > x:
            break
        while x % p == 0:
            factors.append(p)
            x //= p
    if x > 1:
        factors.append(x)
    return factors


def FindGCD2(m, n, primes):
    """หาค่า GCD โดยใช้ sieve + prime factorization"""
    factors_m = prime_factors_sieve(m, primes)
    factors_n = prime_factors_sieve(n, primes)

    common = []
    for f in factors_m:
        if f in factors_n:
            common.append(f)
            factors_n.remove(f)
    
    gcd_val = 1
    for f in common:
        gcd_val *= f
    return gcd_val


# ----------------------------
# อ่านไฟล์ numbers.txt
# ----------------------------
with open("lab1/testcase/Extra Case2 plot.txt", "r") as f:
    lines = f.readlines()

# วนคำนวณ GCD สำหรับแต่ละบรรทัด
results = []
i = 1
for line in lines:
    if(i==38):
        break
    line = line.strip()
    if not line:
        continue
    m, n = map(int, line.split(","))

    limit = int(max(m, n)**0.5) + 1
    primes = sieve(limit)

    gcd_val = FindGCD2(m, n, primes)
    results.append(f"GCD({m}, {n}) = {gcd_val}")
    i+=1
    #print(i)

# แสดงผล
for r in results:
    print(r)

# ----------------------------
# ถ้าอยากบันทึกผลลัพธ์ลงไฟล์ใหม่
# ----------------------------
with open("gcd_results.txt", "w") as f:
    f.write("\n".join(results))