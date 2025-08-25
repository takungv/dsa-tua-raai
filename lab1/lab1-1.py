def prime_factors_naive(x):
    """หาตัวประกอบเฉพาะแบบ naive (trial division)"""
    factors = []
    divisor = 2
    while x > 1:
        # ถ้า x หารด้วย divisor ลงตัว ให้บันทึกตัวประกอบ
        while x % divisor == 0:
            factors.append(divisor)
            x //= divisor
        divisor += 1
    return factors

def FindGCD1(m, n):
    """หาค่า GCD โดยใช้ prime factorization แบบ naive"""
    factors_m = prime_factors_naive(m)
    factors_n = prime_factors_naive(n)
    
    # หาค่าที่เหมือนกัน
    common = []
    for f in factors_m:
        if f in factors_n:
            common.append(f)
            factors_n.remove(f)  # ป้องกันการนับซ้ำเกินไป
    
    # คูณตัวประกอบร่วม
    gcd_val = 1
    for f in common:
        gcd_val *= f
    return gcd_val