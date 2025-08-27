class Node:
    """โครงสร้างของ Node สำหรับ Expression Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ===== Traversals =====
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

# ===== Tokenizer (แยกตัวเลขหลายหลัก, operator, วงเล็บ) =====
def tokenize(expression):
    tokens = []
    number = ""
    for ch in expression:
        if ch.isdigit():
            number += ch
        else:
            if number:
                tokens.append(number)
                number = ""
            if ch in "+-*/()":
                tokens.append(ch)
    if number:
        tokens.append(number)
    return tokens


# ===== Infix → Postfix (Shunting Yard Algorithm) =====
def infix_to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []
    
    for token in tokens:
        if token.isdigit():  
            output.append(token)
        elif token in "+-*/":
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # เอา '(' ออก
    
    while stack:
        output.append(stack.pop())
    return output


# ===== สร้าง Expression Tree จาก Postfix =====
def construct_tree(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(Node(token))
        else:
            node = Node(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack[0]


# ===== Evaluate Postorder ด้วย Stack =====
def evaluate_postorder(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
    return stack[0]


# ===== Main Program =====
if __name__ == "__main__":
    expr = input("Enter expression (e.g., (10+25)-3): ").replace(" ", "")
    
    # 1) Tokenize
    tokens = tokenize(expr)
    
    # 2) Infix → Postfix
    postfix = infix_to_postfix(tokens)
    print("Postfix:", " ".join(postfix))
    
    # 3) สร้าง Expression Tree
    root = construct_tree(postfix)
    
    # 4) Traversals
    print("Inorder:  ", " ".join(inorder(root)))
    print("Preorder: ", " ".join(preorder(root)))
    print("Postorder:", " ".join(postorder(root)))
    
    # 5) Evaluate
    print("Result:", evaluate_postorder(postfix))