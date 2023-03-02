import pytest

def setup_module(module):
    print("Creating DB Connection")


def teardown_module(module):
    print("Closing DB Connection")


def setup_function(function):
    print("Lauching browser")


def tear_function(function):
    print("Tear down browser")


def test_dologin():
    print("Executing login test")


def test_user_reg():
    print("Executing User Reg test")
