def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def FindGCD_multi(*args):
    if len(args) < 2:
        raise ValueError("ต้องมีอย่างน้อย 2 ตัวเลข")
    
    gcd_val = args[0]
    for num in args[1:]:
        gcd_val = gcd_euclid(gcd_val, num)
    return gcd_val


with open("lab1/testcase/Extra Case2 plot.txt", "r") as file:
    lines = file.readlines()
i=1
for line in lines:
    if(i==38):
        break
    nums = [int(x.strip()) for x in line.split(",")]
    result = FindGCD_multi(*nums)
    print(f"GCD{tuple(nums)} = {result}")
    i+=1