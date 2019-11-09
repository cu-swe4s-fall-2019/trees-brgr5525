class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def insert(root, key, value=None):
    if root == None:
        root = Node(key, value)
        return root

    else:
        try:
            if key < root.key:
                if root.left == None:
                    root.left = Node(key, value)
                else:
                    insert(root.left, key, value)
            else:
                if root.right == None:
                    root.right = Node(key, value)
                else:
                    insert(root.right, key, value)
        except TypeError:
            raise TypeError('Key types must be comparable')
        return root

def search(root, key):
    try:
        root.key
    except AttributeError:
        return None

    if key == root.key:
        return root
    else:
        try:
            if key < root.key:
                return search(root.left, key)
            else:
                return search(root.right, key)
        except TypeError:
            raise TypeError('Key types could not be compared')

        return None
