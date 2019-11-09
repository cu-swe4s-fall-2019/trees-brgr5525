import unittest
import binary_tree as bt


class TestBinaryTree(unittest.TestCase):

    def test_node_init(self):
        root = bt.Node()

        self.assertEqual(root.key, None)
        self.assertEqual(root.value, None)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, None)

    def test_insert_root_none(self):
        root = bt.insert(None, 5, 'one')

        self.assertEqual(root.key, 5)
        self.assertEqual(root.value, 'one')
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, None)

    def test_insert_left_child_none(self):
        root = bt.insert(None, 5, 'one')
        root = bt.insert(root, 4, 'two')

        self.assertEqual(root.left.key, 4)
        self.assertEqual(root.left.value, 'two')
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right, None)

    def test_insert_right_child_none(self):
        root = bt.insert(None, 5, 'one')
        root = bt.insert(root, 7, 'three')

        self.assertEqual(root.right.key, 7)
        self.assertEqual(root.right.value, 'three')
        self.assertEqual(root.right.left, None)
        self.assertEqual(root.right.right, None)

    def test_insert_left_child_present(self):
        root = bt.insert(None, 5, 'one')
        root = bt.insert(root, 4, 'two')
        root = bt.insert(root, 4.5, 'four')

        self.assertEqual(root.left.right.key, 4.5)
        self.assertEqual(root.left.right.value, 'four')
        self.assertEqual(root.left.right.left, None)
        self.assertEqual(root.left.right.right, None)

    def test_search_root_node(self):
        root = bt.insert(None, 5, 'one')
        r = bt.search(root, 5)

        self.assertEqual(r, root)

    def test_search_left_child(self):
        root = bt.insert(None, 5, 'one')
        root = bt.insert(root, 4, 'two')
        r = bt.search(root, 4)

        self.assertEqual(r, root.left)

    def test_search_right_child(self):
        root = bt.insert(None, 5, 'one')
        root = bt.insert(root, 7, 'three')
        r = bt.search(root, 7)

        self.assertEqual(r, root.right)

    def test_search_key_not_found(self):
        root = bt.insert(None, 5, 'one')
        root = bt.insert(root, 4, 'two')
        root = bt.insert(root, 4.5, 'four')
        r = bt.search(root, 10)

        self.assertEqual(r, None)

    def test_search_more_complex(self):
        root = bt.insert(None, 5, 'one')
        root = bt.insert(root, 4, 'two')
        root = bt.insert(root, 7, 'three')
        root = bt.insert(root, 9, 'four')
        root = bt.insert(root, 8, 'five')
        r = bt.search(root, 8)

        self.assertEqual(r, root.right.right.left)

    def test_key_is_nonnumber(self):
        root = bt.insert(None, 'cheese')
        root = bt.insert(root, 'brie')
        root = bt.insert(root, 'gouda')
        root = bt.insert(root, 'cheddar')
        r = bt.search(root, 'provolone')

        self.assertEqual(r, None)

    def test_key_type_error(self):
        root = bt.insert(None, 'cheese')
        root = bt.insert(root, 'brie')
        root = bt.insert(root, 'gouda')
        root = bt.insert(root, 'cheddar')

        self.assertRaises(TypeError, bt.insert, (root, 5))
        self.assertRaises(TypeError, bt.search, (root, 5))


if __name__ == '__main__':
    unittest.main()
