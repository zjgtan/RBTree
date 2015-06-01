#-*- coding: utf-8 -*-
from tree import Tree
from tree import TreeNode


class RBTreeNode(TreeNode):
    def __init__(self, value, color=None):
        TreeNode.__init__(self, value)
        self.color = color #颜色

class RBTree(Tree):

    def insert(self, value):
        
        if self.root == None:
            self.root = RBTreeNode(value, 'BLACK')
            return

        p = self.root
        while p != None:
            if p.value == value:
                return
            elif p.value > value:
                if p.left != None: 
                    p = p.left
                else: 
                    p.left = RBTreeNode(value, 'RED')
                    node = p.left
                    node.parent = p
                    break
            elif p.value < value:
                if p.right != None:
                    p = p.right
                else:
                    p.right = RBTreeNode(value, 'RED')
                    node = p.right
                    node.parent = p
                    break
        if node.parent == self.root:
            return

        if node.parent.value < node.parent.parent.value:
            while node.parent.color=='RED':
                parent = node.parent
                grand = parent.parent
                if grand.left == parent:
                    uncle = grand.right
                else:
                    uncle = grand.left

                if parent.color == 'RED' and uncle != None and uncle.color == 'RED':
                    self._insert_case_1(node, parent, uncle, grand)
                    if grand == self.root:
                        grand.color = 'BLACK'
                        break
                    else:
                        node = grand
                elif parent.color == 'RED' and (uncle == None or uncle.color == 'BLACK') and node.value > parent.value:
                    self._insert_case_2(node, parent, uncle, grand)
                    node = parent # 将父节点更新为当前节点
                elif parent.color == 'RED' and (uncle == None or uncle.color == 'BLACK') and node.value < parent.value:
                    self._insert_case_3(node, parent, uncle, grand)
        
    def _insert_case_1(self, node, parent, uncle, grand):
        parent.color = 'BLACK'
        uncle.color = 'BLACK'
        grand.color = 'RED'
        


    def _insert_case_2(self, node, parent, uncle, grand):
        self._left_rotate(parent)

    def _insert_case_3(self, node, parent, uncle, grand):
        parent.color = 'BLACK'
        grand.color = 'RED'
        self._right_rotate(grand)

    def find(self, value):
        pass

    def delete(self, value):
        pass

    def _left_rotate(self, node):
        # 左旋转
        rchild = node.right
        
        node.right = rchild.left
        if rchild.left != None:
            rchild.left.parent = node
        rchild.parent = node.parent
        if node.parent == None:
            self.root = rchild
        elif node == node.parent.left:
            node.parent.left = rchild
        else:
            node.parent.right = rchild

        rchild.left = node
        node.parent = rchild

    def _right_rotate(self, node):
        # 右旋转
        lchild = node.left

        node.left = lchild.right
        if lchild.right != None:
            lchild.right.parent = node
        lchild.parent = node.parent
        if node.parent == None:
            self.root = lchild
        elif node == node.parent.right:
            node.parent.right = lchild
        else:
            node.parent.left = lchild
        lchild.right = node
        node.parent = lchild


def main():
    tree = RBTree()
    tree.insert(10)
    tree.insert(9)
    tree.print_tree(lambda node: "({0},{1})".format(node.value, node.color))
    tree.insert(8)
    tree.print_tree(lambda node: "({0},{1})".format(node.value, node.color))

   
if __name__== '__main__':
    main()
