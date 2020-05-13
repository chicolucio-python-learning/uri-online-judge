from basic import sum_two_var, present_result


def test_case01():
    assert sum_two_var(10, 9) == 19
    assert present_result(19) == 'X = 19'


def test_case02():
    assert sum_two_var(-10, 4) == -6
    assert present_result(-6) == 'X = -6'


def test_case03():
    assert sum_two_var(15, -7) == 8
    assert present_result(8) == 'X = 8'
