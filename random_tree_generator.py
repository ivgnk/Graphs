'''
random_tree_generator
https://ru.anyquestion.info/a/sozdanie-koda-na-python-dlya-generatsii-sluchaynogo-dereva
создает случайное дерево максимальной глубины 3 и выводит значения узлов, начиная с корня
'''

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

#()#############################################
def generate_random_tree(depth):
    if depth == 0:
        return None
    node = Node(random.randint(1, 100))
    num_children = random.randint(1, 5)
    for i in range(num_children):
        child = generate_random_tree(depth - 1)
        if child is not None:
            node.children.append(child)
    return node

#()#############################################
def thetest_tree():
    tree = generate_random_tree(3)
    print(tree.value)
    for child in tree.children:
        print(child.value)
        for grand_child in child.children:
            print(grand_child.value)

if __name__ == "__main__":
    thetest_tree()