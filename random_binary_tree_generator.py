'''
random_binary_tree_generator
www.geeksforgeeks.org/random-binary-tree-generator-using-python

-> 52
       -> 42
   -> 97
           -> 88
       -> 90
     52
  /     \
42      97
       /  \
     90   88

The root node is 52.
Its left child is 42 and its right child is 97.
The right child 97 has a right child 88 and a left child 90.
The left child 42 has no children.
'''

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_random_binary_tree(size):
    if size == 0:
        return None

    # Choose random sizes for left and right subtrees
    left_size = random.randint(0, size-1)
    right_size = size - 1 - left_size

    # Generate left and right subtrees recursively
    left_subtree = generate_random_binary_tree(left_size)
    right_subtree = generate_random_binary_tree(right_size)

    # Create new node with random value
    root = Node(random.randint(0, 100))

    # Assign left and right subtrees to children
    root.left = left_subtree
    root.right = right_subtree

    return root

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(" " * 4 * level + "->", node.value)
        print_tree(node.left, level + 1)

# Функция dfs выполняет предварительный DFS-обход дерева путем
# рекурсивного посещения каждого узла в дереве и вывода его значения. Ф
# ункция сначала выводит значение текущего узла, з
# атем рекурсивно посещает его левое поддерево,
# а затем рекурсивно посещает его правое поддерево.
def dfs(node):
    if node is not None:
        print(node.value)
        dfs(node.left)
        dfs(node.right)

# Функция find_max() рекурсивно находит максимальное значение в дереве,
# проверяя значение текущего узла, максимальное значение в его левом поддереве
# и максимальное значение в его правом поддереве.
# Функция возвращает отрицательную бесконечность, если узел Отсутствует.
def find_max(node):
    if node is None:
        return float('-inf')
    else:
        left_max = find_max(node.left)
        right_max = find_max(node.right)
        return max(node.value, left_max, right_max)


#()#############################################
def thetest_tree(tree_size:int):
    print('\n'*4)
    print(f'{tree_size=}')
    tree = generate_random_binary_tree(tree_size)
    print_tree(tree)

    print("Preorder DFS: ")
    dfs(tree)
    print("\n")

    max_value = find_max(tree)
    print("The maximum value in the tree is:", max_value)


if __name__ == "__main__":
    thetest_tree(tree_size=5)
    thetest_tree(tree_size=10)