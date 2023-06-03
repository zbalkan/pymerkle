import pytest
from tests.conftest import option, resolve_backend

MerkleTree = resolve_backend(option)

entries = [b'a', b'b', b'c', b'd', b'e']


def test_append():
    tree = MerkleTree()
    assert tree.get_size() == 0

    for entry in entries:
        index = tree.append(entry)
        value = tree.get_leaf(index)

        assert index == tree.get_size()
        assert value == tree.hash_leaf(entry).hex()
