from rational import rational


def test_case01():
    assert rational('1 / 2 + 3 / 4') == '10/8 = 5/4'


def test_case02():
    assert rational('1 / 2 - 3 / 4') == '-2/8 = -1/4'


def test_case03():
    assert rational('2 / 3 * 6 / 6') == '12/18 = 2/3'


def test_case04():
    assert rational('1 / 2 / 3 / 4') == '4/6 = 2/3'


def test_case05():
    assert rational('5 / 3 - 5 / 3') == '0/9 = 0/1'


def test_case06():
    assert rational('1 / 1 - 1 / 1') == '0/1 = 0/1'


def test_case07():
    assert rational('1 / 1 / 1 / 1') == '1/1 = 1/1'
