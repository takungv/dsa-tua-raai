
import os

def extract_code_safe(source: str) -> str:

    result = []
    i = 0
    n = len(source)
    while i < n:
        c = source[i]
        # ข้าม comment
        if c == '#':
            while i < n and source[i] != '\n':
                i += 1
        # ข้าม string literals
        elif c in ('"', "'"):
            quote = c
            # ตรวจ triple quote
            if i + 2 < n and source[i:i+3] == quote*3:
                quote *= 3
                i += 3
            else:
                i += 1
            while i < n:
                # เจอ quote ปิด
                if source[i:i+len(quote)] == quote:
                    i += len(quote)
                    break
                # ข้าม escape \
                if source[i] == '\\':
                    i += 1
                i += 1
        else:
            result.append(c)
            i += 1
    return ''.join(result)


# === ฟังก์ชันเช็ค balanced ===
def is_balanced(s: str) -> bool:
    """
    ตรวจสอบวงเล็บ (), [], {} ใน code string
    """
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return not stack


# === ตัวอย่างการใช้งานกับไฟล์เดียว ===
filename = "lab2/testcase2-1/test2.py"  # เปลี่ยนชื่อไฟล์ตามต้องการ
#lab2/testcase2-1/test4.py
if not os.path.isfile(filename):
    print(f"File '{filename}' not found.")
else:
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()

    cleaned = extract_code_safe(code)

    if is_balanced(cleaned):
        print("The file is balanced.")
    else:
        print("The file is NOT balanced.")

