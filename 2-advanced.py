import pytest

def test_catch_exception():
    a = 1
    with pytest.raises(AttributeError):
        a.sort()


def test_catch_exception_message():
    a = 1
    with pytest.raises(AttributeError) as exc:
        a.sort()
    assert exc.value.args[0] == "'int' object has no attribute 'sort'"


@pytest.mark.parametrize('value', [1,2,3])
def test_sum(value):
    assert 2 * value == value + value


@pytest.mark.parametrize(('values', 'expected'), (([1,2,3], 6),([1],1), ([1,2],3)))
def test_sum_list(values, expected):
    assert sum(values) == expected


def test_write(tmpdir):
    filename = tmpdir.join('test.txt').strpath
    with open(filename, 'w') as f:
        f.write('test')
