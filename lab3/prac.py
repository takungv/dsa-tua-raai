import os

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def priority_ops(op):
    if op in ('+','-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0

#init tree
def construct_tree(expr):
    values = []
    ops = []
    i = 0

    while i < len(expr):

        #skip space
        if expr[i] == ' ':
            i += 1
            continue


        #int convert
        if expr[i].isdigit():
            val = 0
            while i < len(expr) and expr[i].isdigit():
                val = val*10 + int(expr[i])
                i += 1
            values.append(Node(val))
            continue

        #(
        elif expr[i] == '(':
            ops.append(expr[i])

        #)
        elif expr[i] == ')':
            while ops and ops[-1] != '(':
                op = ops.pop()
                right = values.pop()
                left = values.pop()
                node = Node(op)
                node.left = left
                node.right = right

                values.append(node)
            ops.pop() #remove '('

        #operand
        else:
            while ops and (priority_ops(ops[-1]) >= priority_ops(expr[i])):
                op = ops.pop()
                right = values.pop()
                left = values.pop()
                node = Node(op)
                node.left = left
                node.right = right
                values.append(node)
            ops.append(expr[i])
        i += 1
    
    while ops:
        op = ops.pop()
        right = values.pop()
        left = values.pop()
        node = Node(op)
        node.left = left
        node.right = right
        values.append(node)

    return values[-1]


#-----Travaersal-----
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
#----------

filename = os.path.join("lab3/testcase3", "Lab_3 example.txt")

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

                inord = inorder(tree)
                preord = preorder(tree)
                postord = postorder(tree)

                print(" -------------------------------")
                print(" Inorder :"," ".join(inord))
                print(" Preorder :"," ".join(preord))
                print(" Postorder :", " ".join(postord))
                print(" -------------------------------")


            except Exception as e:
                print(f"Error evaluating '{expr}' : {e}")