import pytest


@pytest.fixture(scope='module')
def setup():
    print("Creating DB Connection")
    yield
    print("Closing DB Connection")


@pytest.fixture(scope='function')
def before():
    print("Launching browser")
    yield
    print("Closing browser")


@pytest.mark.usefixtures("setup", "before")
def test_dologin():
    print("Executing login test")


@pytest.mark.usefixtures("setup", "before")
def test_user_reg():
    print("Executing User Reg test")
