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


def FindGCD_multi(*args):
    if len(args) < 2:
        raise ValueError("ต้องมีอย่างน้อย 2 ตัวเลข")
    
    gcd_val = args[0]
    for num in args[1:]:
        gcd_val = FindGCD1(gcd_val, num)
    return gcd_val


# ---------- อ่านไฟล์ ----------
with open("lab1/testcase/Extra Case2 plot.txt", "r") as file:
    lines = file.readlines()

i = 1
for line in lines:
    if(i == 38):
        break
    nums = [int(x.strip()) for x in line.split(",")]
    result = FindGCD_multi(*nums)
    print(f"GCD{tuple(nums)} = {result}")
    i += 1
