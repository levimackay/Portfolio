from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name(family_name="Mackay", given_name="Levi") == "Mackay; Levi"
    
def test_extract_family_name():
    assert extract_family_name(full_name="Mackay; Levi") == "Mackay"
    
def test_extract_given_name():
    assert extract_given_name(full_name="Mackay; Levi")

pytest.main(["-v", "--tb=line", "-rN", __file__])