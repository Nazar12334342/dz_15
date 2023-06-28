import pytest
from dz_1 import Node

@pytest.fixture
def bst():
    data = [5, 3, 8, 2, 4, 1, 7, 9]
    root = Node.build_binary_search_tree(data)
    return root

def test_insert(bst):
    bst.insert(6)
    assert bst.right.left.left.val == 6

def test_find_min(bst):
    assert bst.find_min() == 1

def test_find_max(bst):
    assert bst.find_max() == 9

def test_delete_element(bst):
    bst.delete_element(4)
    assert bst.left.right.val != 4

