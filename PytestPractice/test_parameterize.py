import pytest


def get_data():
    return [
        ("hangocmy.work1@gmail.com", "pass1"),
        ("hangocmy.work2@gmail.com", "pass2"),
        ("hangocmy.work3@gmail.com", "pass3")
    ]


@pytest.mark.parametrize("username, password", get_data())
def test_dologin(username, password):
    print(username, "---", password)
