# -*- coding: utf-8 -*-
from core.matching import SimpleMatchmaker, CliqueMatchmaker
import importlib


class Application(object):
    MATCHMAKERS = {
        'simple': SimpleMatchmaker,
        'clique': CliqueMatchmaker
    }

    def __init__(self, input_plugin, output_plugin, matchmaker):
        self._input_plugin = input_plugin
        self._output_plugin = output_plugin
        self._matchmaker = matchmaker

    def process(self):
        input_arguments = self._check_and_parse_input_plugin(self._input_plugin)
        output_arguments = self._check_and_parse_output_plugin(self._output_plugin)
        matchmaker = self._check_and_parse_matchmaker(self._matchmaker)

        import_plugin = self._get_import_plugin(input_arguments)
        data = import_plugin.import_data()

        matchmaker().run(data)

        for argument in output_arguments:
            export_plugin = self._get_export_plugin(argument)
            export_plugin.export_data(data)

    @staticmethod
    def _check_and_parse_input_plugin(string):
        try:
            name, arguments = string.split(':')
        except ValueError:
            raise RuntimeError('Incorrect input plugin string')

        return name, arguments

    @staticmethod
    def _check_and_parse_output_plugin(string):
        try:
            raw_ouputs = string.split(';')
            outputs = []
            for output in raw_ouputs:
                name, arguments = output.split(':')
                outputs.append((name, arguments))
            if len(output) == 0:
                raise ValueError()
        except ValueError:
            raise RuntimeError('Incorrect output plugin string')
        return outputs

    def _check_and_parse_matchmaker(self, string):
        try:
            return self.MATCHMAKERS[string]
        except KeyError:
            raise RuntimeError('Incorrect matchmaker string')

    @staticmethod
    def _get_import_plugin(input_arguments):
        name, arguments = input_arguments
        module = importlib.import_module('importer.%simporter' % name)
        return module.importer(arguments)

    @staticmethod
    def _get_export_plugin(output_arguments):
        name, arguments = output_arguments
        module = importlib.import_module('exporter.%sexporter' % name)
        return module.exporter(arguments)
