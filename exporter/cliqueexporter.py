# -*- coding: utf-8 -*-
from .exporter import Exporter
from .todoexporter import create_person_simple_string


HEADER = '''\
Following cliques have been found:
'''

GROUP_TEMPLATE = '''
TEAM {number}: {count} friends
{friends}
'''


class CliqueExporter(Exporter):
    def __init__(self, filename):
        Exporter.__init__(self)
        self._filename = filename

    def export_data(self, data):
        groups = self._extract_groups(data)
        groups = self._sort_groups_from_biggest(groups)
        with open(self._filename, 'wt') as f:
            f.write(HEADER)
            for i, group in enumerate(groups):
                f.write(self._create_group_string(group, i+1))

    @staticmethod
    def _create_group_string(group, number):
        friend_strings = (
            create_person_simple_string(friend)
            for friend in group
        )
        return GROUP_TEMPLATE.format(
            number=number,
            count=len(group),
            friends='\n'.join(friend_strings)
        )

    @staticmethod
    def _extract_groups(all_people):
        groups = set()
        for person in all_people:
            group = set(person.results.matches)
            if len(group) <= 1:
                continue
            group.add(person)
            groups.add(tuple(sorted(group, key=lambda p: p.number)))
        return groups

    @staticmethod
    def _sort_groups_from_biggest(groups):
        return sorted(groups, key=lambda x: len(x), reverse=True)


exporter = CliqueExporter
