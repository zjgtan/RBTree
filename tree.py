#-*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Tree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        # 插入
        pass

    def find(self, value):
        # 查找
        pass

    def delete(self, value):
        # 删除
        pass

    def _print(self, node, hight, func):
        if node == None:
            return

        self._print(node.left, hight + 1, func)
        print " " * hight * 2 + func(node)
        self._print(node.right, hight + 1, func)

    def print_tree(self, func=lambda node: str(node.value)):
        # 显示
        if self.root == None:
            return

        self._print(self.root, 0, func)
        print


        
if __name__ == '__main__':
    tree = Tree()
    tree.root = TreeNode(0)
    tree.root.value = 0
    tree.root.left = TreeNode(1)
    tree.root.left.value = 1
    tree.root.right = TreeNode(2)
    tree.root.right.value = 2
    tree.print_tree()
