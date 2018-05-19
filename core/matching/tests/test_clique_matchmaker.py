# -*- coding: utf-8 -*-
import pytest
from core.person import Person


@pytest.fixture
def testdata():
    data = []
    tobi = Person(name='Tobi', number=1, email='tobi@gmail.com', phone='0123456789',
                  marked_numbers={2, 3, 4})
    sara = Person(name='Sara Mustermann', number=2, email='', phone='123456789',
                  marked_numbers={1, 4, 3})
    mark = Person(name='Mark', number=3, email='mark@mark.com', phone='987654321',
                  marked_numbers={2, 5, 1})
    luisa = Person(name='Luisa', number=4, email='', phone='49123456789',
                   marked_numbers={5, 1})
    data.append(tobi)
    data.append(sara)
    data.append(mark)
    data.append(luisa)
    return data


@pytest.fixture
def matchmaker():
    from core.matching import CliqueMatchmaker
    return CliqueMatchmaker()


def test_matchmaking_returns_correct_subset_of_data(matchmaker, testdata):
    matchmaker.run(testdata)

    tobi, sara, mark, luisa = testdata
    assert tobi.results.matches == {sara, mark}
    assert sara.results.matches == {tobi, mark}
    assert mark.results.matches == {sara, tobi}
    assert luisa.results.matches == {tobi}
