from BinarySearchTree import BinarySearchTree, Node


def find_in_range(starting_node, min_key, max_key):
    return [
        node.key
        for node in bst_list_inorder(starting_node)
        if node.key >= min_key and node.key <= max_key
    ]


def bst_list_inorder(node):
    if node is None:
        return []
    return bst_list_inorder(node.left) + [node] + bst_list_inorder(node.right)


if __name__ == "__main__":
    tree = BinarySearchTree()

    # Insert some random-looking integers into the tree.
    user_values = input("Enter values to be inserted separated by spaces: ")
    print()

    for value in user_values.split():
        new_node = Node(value)
        tree.insert(new_node)

    print("Initial tree:")
    print(tree)
    print()

    # Read in range values and starting node's key
    min_key = input()
    max_key = input()
    start_key = input()

    starting_node = tree.search(start_key)

    keys_in_range = find_in_range(starting_node, min_key, max_key)

    print("Keys in range:", keys_in_range)

# Test with 

# bat start ding being clock quick last name truck
# craft
# question
# ding