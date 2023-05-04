import pytest
import os
import sys
# Add the parent directory of both rf2rnd and tests to the sys.path list
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from rf2rnd import collect_rf_data, collect_hopping_rf_data, extract_random_bits, randint, randflo

extractors = [
    'von_neumann_extractor',
    'xor_extractor',
    'majority_vote_extractor',
    'bit_shift_extractor'
]

@pytest.fixture(scope="module")
def samples():
    return collect_rf_data()

def test_extract_random_bits(samples):
    bits = extract_random_bits(samples, extractors[0])
    assert len(bits) == 4096

def test_randflo(samples):
    bits = extract_random_bits(samples, extractors[0])
    f_num = randflo(bits, 1, 0, 10000)
    assert isinstance(f_num, float)

def test_randint(samples):
    bits = extract_random_bits(samples, extractors[0])
    int_num = randint(bits, 1, 0, 10000)
    assert isinstance(int_num, int)

def test_randflo_batch(samples):
    bits = extract_random_bits(samples, extractors[0])
    f_nums = randflo(bits, 10, 0, 10000)
    assert isinstance(f_nums, list)
    assert len(f_nums) == 10

def test_randint_batch(samples):
    bits = extract_random_bits(samples, extractors[0])
    int_nums = randint(bits, 10, -10, -10000)
    assert isinstance(int_nums, list)
    assert len(int_nums) == 10
    assert all(isinstance(n, int) for n in int_nums)
    assert all(-10000 <= n <= -10 for n in int_nums)
