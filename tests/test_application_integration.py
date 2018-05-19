# -*- coding: utf-8 -*-
import pytest
from application import Application


@pytest.fixture
def output_dir(tmpdir):
    return str(tmpdir.join(''))


def test_application_integration(output_dir):
    input_arguments = 'csv:example/sample.csv'
    output_arguments = 'todo:%s/todo.txt' % output_dir
    matchmaker = 'simple'

    app = Application(input_arguments, output_arguments, matchmaker)
    app.process()
