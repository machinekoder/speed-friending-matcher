# -*- coding: utf-8 -*-
import pytest
from . import people_testdata


@pytest.fixture
def testdata():
    basedata = people_testdata.testdata()
    tobi, sara, mark, luisa = basedata
    tobi.results.matches = {sara, mark}
    sara.results.matches = {tobi, mark}
    mark.results.matches = {tobi, sara}
    luisa.results.matches = {tobi}
    return basedata


@pytest.fixture
def exporter(tmpdir):
    from exporter.graphexporter import GraphExporter
    todo_file = tmpdir.join('out.raw')
    return GraphExporter(filename=str(todo_file))


def test_writing_output_to_file_works_as_expected(testdata, exporter):
    exporter.export_data(testdata)

    with open(exporter._filename, 'rt') as f:
        written = f.read()

    assert any(l in written for l in ('Mark -- "Sara Mustermann";', '"Sara Mustermann" -- Mark;'))
    assert any(l in written for l in ('Mark -- Tobi;', 'Tobi -- Mark;'))
    assert any(l in written for l in ('Luisa -- Tobi;', 'Tobi -- Luisa;'))
    assert any(l in written for l in ('"Sara Mustermann" -- Tobi;', 'Tobi -- "Sara Mustermann";'))
    assert len(written.split('\n')) == 7
