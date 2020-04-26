import string
import random

def bst_search(tree, key):
    cur = tree.root
    while cur is not None:
        if key == cur.key:
            return cur  # Found!
        elif key < cur.key:
            cur = cur.left
        else:
            cur = cur.right
    return None  # Not found :(


def bst_insert(tree, node):
    if tree.root is None:
        tree.root = node
        node.left = None
        node.right = None
    else:
        cur = tree.root
        while cur is not None:
            if node.key < cur.key:
                if cur.left is None:
                    cur.left = node  # Set node
                    cur = None
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node  # Set node
                    cur = None
                else:
                    cur = cur.right
        node.left = None
        node.right = None


def bst_remove(tree, key):
    p = None  # parent
    c = tree.root  # current
    while c is not None:
        # search
        if c.key == key:  # node found

            if not c.left and not c.right:  # remove leaf
                if p is None:
                    # is root
                    tree.root = None
                elif p.left == c:
                    p.left = None
                else:
                    p.right = None
            elif c.left and not c.right:  # remove node with only left child
                if p is None:
                    tree.root = c.left
                elif p.left == c:
                    p.left = c.left
                else:
                    p.right = c.left

            elif not c.left and c.right:  # remove node with only right child
                if p is None:
                    tree.root = c.right
                elif p.left == c:
                    p.left = c.right
                else:
                    p.right = c.right
            else:  # remove node with two children
                # find successor (leftmost child of right subtree)
                s = c.right
                while s.left:
                    s = s.left
                data = s.key
                bst_remove(tree, data)  # remove successor
                c.key = data
            return  # node found and removed
            
        elif c.key < key:  # search right
            p = c
            c = c.right
        else:  # search left
            p = c
            c = c.left
    return  # not found :(


def bst_print_inorder(node):
    if node is None:
        return
    bst_print_inorder(node.left)
    print(node)
    bst_print_in_order(node.right)

def bst_list_inorder(node):
    if node is None:
        return []
    return bst_list_inorder(node.left) + [node] + bst_list_inorder(node.right)


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
       return str(bst_list_inorder(self.root))

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)
    
    def __repr__(self):
        return str(self.key)


def main():
    nodes = []
    for c in range(1, 21):
        nodes.append(Node(c))
    scrambled_nodes = scrambled(nodes)
    print_list(scrambled_nodes)
    tree = Tree()
    for n in scrambled_nodes:
        bst_insert(tree, n)
    
    # bst_print_inorder(tree.root)
    lst = bst_list_inorder(tree.root)
    print(lst)


def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest


def print_list(lst):
    for n in lst:
        if n == lst[-1]:
            print(n)
        else:
            print(n, end=" ")


if __name__ == "__main__":
    main()