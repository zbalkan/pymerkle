import pytest
import hashlib
from pymerkle.hasher import MerkleHasher
from pymerkle.constants import ALGORITHMS
from tests.conftest import option, all_configs


blob = b'oculusnonviditnecaurisaudivit'

prefx00 = b'\x00'
prefx01 = b'\x01'


@pytest.mark.parametrize('config', all_configs(option))
def test_hash_buff(config):
    h = MerkleHasher(**config)

    if h.security:
        assert h.hash_buff(blob) == getattr(hashlib, h.algorithm)(
            prefx00 + blob).digest()
    else:
        assert h.hash_buff(blob) == getattr(hashlib, h.algorithm)(
            blob).digest()


@pytest.mark.parametrize('config', all_configs(option))
def test_hash_pair(config):
    h = MerkleHasher(**config)

    if h.security:
        assert h.hash_pair(blob, blob) == getattr(hashlib, h.algorithm)(
            prefx01 + blob + blob).digest()
    else:
        assert h.hash_pair(blob, blob) == getattr(hashlib, h.algorithm)(
            blob + blob).digest()
