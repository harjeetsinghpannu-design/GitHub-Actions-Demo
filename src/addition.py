# app.py
# This is a test commit
# This is the latest commit for testing purposes
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(6, 5) == 11
