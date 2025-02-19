import pytest

@pytest.fixture(autouse=False)
def setUp():
    print("1")
    print("2")
    yield
    print("clean up")