# -*- coding: utf-8 -*-
import pytest
from application import Application


@pytest.fixture
def dummy_app():
    return Application('', '', '')


def test_parsing_correct_input_plugin_string_works(dummy_app):
    correct_string = 'csv:foo.txt'

    name, arguments = dummy_app._check_and_parse_input_plugin(correct_string)

    assert name == 'csv'
    assert arguments == 'foo.txt'


def test_parsing_broken_input_plugin_string_raises_runtimeerror(dummy_app):
    broken_string = 'wtfomg'

    try:
        name, arguments = dummy_app._check_and_parse_input_plugin(broken_string)
        assert False
    except RuntimeError:
        assert True


def test_parsing_output_plugin_string_with_one_plugin_works(dummy_app):
    correct_string = 'todo:todos.txt'

    plugins = dummy_app._check_and_parse_output_plugin(correct_string)

    assert len(plugins) == 1
    name, arguments = plugins[0]
    assert name == 'todo'
    assert arguments == 'todos.txt'


def test_parsing_output_plugin_string_with_two_plugins_works(dummy_app):
    correct_string = 'todo:todos.txt;csv:whatever.csv'

    plugins = dummy_app._check_and_parse_output_plugin(correct_string)

    assert len(plugins) == 2
    name, arguments = plugins[1]
    assert name == 'csv'
    assert arguments == 'whatever.csv'


def test_parsing_broken_output_plugin_string_raises_runtimeerror(dummy_app):
    broken_string = 'wtfomg'

    try:
        dummy_app._check_and_parse_output_plugin(broken_string)
        assert False
    except RuntimeError:
        assert True


def test_parsing_correct_matchmaker_works(dummy_app):
    correct_string = 'simple'

    matchmaker = dummy_app._check_and_parse_matchmaker(correct_string)

    assert matchmaker is not None


def test_parsing_broken_matchmaker_raises_runtimeerror(dummy_app):
    broken_string = 'extreme'

    try:
        dummy_app._check_and_parse_matchmaker(broken_string)
        assert False
    except RuntimeError:
        assert True


def test_getting_csv_import_plugin_works(dummy_app):
    arguments = ('csv', 'dummy.csv')

    dummy_app._get_import_plugin(arguments)


def test_getting_todo_export_plugin_wokrs(dummy_app):
    arguments = ('todo', 'todos.txt')

    dummy_app._get_export_plugin(arguments)
