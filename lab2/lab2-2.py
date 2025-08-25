import os

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b  # floating-point division
    raise ValueError("Unknown operator: " + op)

def evaluate(expression):
    values = []   # stack for numbers
    ops = []      # stack for operators
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        # handle negative number
        if (expression[i] == '-' and
            (i == 0 or expression[i-1] == '(' or expression[i-1] in '+-*/')):
            i += 1
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            values.append(-val)
            continue

        # number
        if expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            values.append(val)
            continue

        # opening parenthesis
        elif expression[i] == '(':
            ops.append(expression[i])

        # closing parenthesis
        elif expression[i] == ')':
            while ops and ops[-1] != '(':
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(apply_op(a, b, op))
            ops.pop()  # remove '('

        # operator
        else:
            while (ops and precedence(ops[-1]) >= precedence(expression[i])):
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(apply_op(a, b, op))
            ops.append(expression[i])
        i += 1

    # apply remaining operators
    while ops:
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(apply_op(a, b, op))

    return values[-1]


filename = os.path.join("lab2/testcase2-2", "2_Expression.txt")  # กำหนดไฟล์ในโฟลเดอร์ย่อย

if not os.path.isfile(filename):
    print(f"File '{filename}' not found.")
else:
    print(f"=== Running {filename} ===")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            expr = line.strip()
            if not expr:  # ข้ามบรรทัดว่าง
                continue
            try:
                result = evaluate(expr)
                print(f"{expr} = {result}")
            except Exception as e:
                print(f"Error evaluating '{expr}': {e}")