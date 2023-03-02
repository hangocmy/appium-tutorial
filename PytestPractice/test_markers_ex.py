import pytest


@pytest.mark.functional
def test_login():
    print("Executing login test")


@pytest.mark.regression
def test_user_reg():
    print("Executing User Reg test")


@pytest.mark.functional
def test_compose_email():
    print("Executing compose email test")


@pytest.mark.skip
def test_skip():
    print("Skipping test")

'''
1. Run theo tên testcase: pytest tên_file.py -s -v -k "tên_function"
    >> pytest test_markers_ex.py -s -v -k login

2. Run testcase ngoại trừ tên testcase chỉ định: pytest tên_file.py -s -v -k "not tên_function"
    >> pytest test_markers_ex.py -s -v -k "not login"
    
3. Run testcase theo mark đã được đánh dấu @pytest.mark.{tên_mark}
    >> pytest test_markers_ex.py -s -v -m "functional"
    
4. Run testcase ngoại trừ test được đánh dấu @pytest.mark.{tên_mark}
    >> pytest test_markers_ex.py -s -v -m "not functional"
    
5. Skipp testcase
'''
