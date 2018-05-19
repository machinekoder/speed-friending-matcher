# -*- coding: utf-8 -*-
from .simple_matchmaker import SimpleMatchmaker


class CliqueMatchmaker(SimpleMatchmaker):
    """
    Finds subsets (cliques) in the data bigger than a single two person match.
    """

    def __init__(self):
        super(CliqueMatchmaker, self).__init__()
        self._graph = {}

    def run(self, data):
        super(CliqueMatchmaker, self).run(data)
        self._graph = {person: set(person.results.matches) for person in data}
        for person in data:
            self._find_biggest_clique_for_person(person)

    def _find_biggest_clique_for_person(self, person, **__):

        def dfs(graph, start):
            visited = set()
            stack = [(start, {start})]
            longest_path = {start}
            while stack:
                (vertex, path) = stack.pop()
                if vertex not in visited:
                    # only visit if all in path are friends
                    if vertex is start or all(v in graph[vertex] for v in path):
                        visited.add(vertex)
                        path = set(path).union([vertex])
                        if len(path) > len(longest_path):
                            longest_path = path
                        stack.extend((v, path) for v in (graph[vertex] - visited))
            return longest_path

        matches = dfs(self._graph, person)
        matches.remove(person)

        person.results.matches = matches
