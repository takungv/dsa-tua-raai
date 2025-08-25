def generate_subsets_stack(elements):
    stack = [[]]   # เริ่มจาก subset ว่าง
    result = []

    while stack:
        subset = stack.pop()      # ดึงชุดล่าสุดออกมา
        result.append(subset)     # เก็บผลลัพธ์

        # ขยาย subset โดยเพิ่มสมาชิกใหม่เข้าไป
        for elem in elements:
            if not subset or elem > subset[-1]:  # กัน subset ซ้ำ
                stack.append(subset + [elem])

    return result


# ทดลองกับ [1,2,3]
T1 = [[1],[2],[3]]
print("Subsets ของ", T1, ":")
print(generate_subsets_stack(T1))

# ทดลองกับ [1,2]
T2 = [[1],[2]]
print("\nSubsets ของ", T2, ":")
print(generate_subsets_stack(T2))