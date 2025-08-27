import os

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ความสำคัญของ operator
def precedence(op):
    if op in ('+', '-', '–', '—'):   # รองรับทุกแบบของ minus
        return 1
    if op in ('*', '/'):
        return 2
    return 0


# สร้าง Binary Expression Tree
def construct_tree(expr):
    values = []
    ops = []
    i = 0
    
    while i < len(expr):
        # ข้ามช่องว่าง
        if expr[i] == ' ':
            i += 1
            continue 

        # ตัวเลข
        if expr[i].isdigit():
            val = 0
            while i < len(expr) and expr[i].isdigit():
                val = val * 10 + int(expr[i])
                i += 1
            values.append(Node(val))
            continue
        
        # วงเล็บเปิด
        elif expr[i] == '(':
            ops.append(expr[i])

        # วงเล็บปิด
        elif expr[i] == ')':
            while ops and ops[-1] != '(':
                op = ops.pop()
                right = values.pop()
                left = values.pop()
                node = Node(op)
                node.left = left
                node.right = right
                values.append(node)
            ops.pop() # ลบ '('

        # operator
        else:
            while ops and (precedence(ops[-1]) >= precedence(expr[i])):
                op = ops.pop()
                right = values.pop()
                left = values.pop()
                node = Node(op)
                node.left = left
                node.right = right
                values.append(node)
            ops.append(expr[i])
        i += 1

    # สร้าง node จาก operator ที่เหลือ
    while ops:
        op = ops.pop()
        right = values.pop()
        left = values.pop()
        node = Node(op)
        node.left = left
        node.right = right
        values.append(node)

    return values[-1] # root ของ tree

# ---------- ข้อ 1: Traversal ----------
def inorder(root):
    if root:
        return inorder(root.left) + [str(root.value)] + inorder(root.right)
    return []

def preorder(root):
    if root:
        return [str(root.value)] + preorder(root.left) + preorder(root.right)
    return []

def postorder(root):
    if root:
        return postorder(root.left) + postorder(root.right) + [str(root.value)]
    return []

# ---------- ข้อ 2: Evaluate จาก Postorder ----------
def evaluate_postorder(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token in ('+',):
                stack.append(a + b)
            elif token in ('-', '–', '—'):   # รองรับลบทุกแบบ
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]
# ========== ทดลองกับไฟล์ ==========
filename = os.path.join("lab3/testcase3", "test3.txt")

if not os.path.isfile(filename):
    print(f"File '{filename}' not found.")
else:
    print(f"=== Running {filename} ===")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            expr = line.strip()
            if not expr:
                continue
            expr = expr.strip('"')
            try:
                tree = construct_tree(expr)

                # ข้อ 1: Traversal
                inord = inorder(tree)
                preord = preorder(tree)
                postord = postorder(tree)

                print(f"Expression: {expr}")
                print(" Inorder  :", " ".join(inord))
                print(" Preorder :", " ".join(preord))
                print(" Postorder:", " ".join(postord))

                # ข้อ 2: Evaluate (ใช้ Postorder)
                result = evaluate_postorder(postord)
                print(" Result   :", result)
                print()
            except Exception as e:
                print(f"Error evaluating '{expr}': {e}")
