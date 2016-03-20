# Example of a test that should pass:

def test_assign():
    a = 1


# Example of a test that fails:

def test_sort():
    a = 1
    a.sort()


# Example of using assert which passes:

def test_assert_passes():
    a = 1
    assert a == 1


# Example of using assert which fails:

def test_assert_fails():
    a = 1
    assert a == 2
