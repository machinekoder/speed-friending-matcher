# -*- coding: utf-8 -*-
from core.person import Person


class CliqueMatchmaker(object):
    """
    Finds subsets (cliques) in the data bigger than a single two person match.
    """

    def __init__(self):
        self._everyone = {}

    def run(self, data):
        self._everyone = {person.number: person for person in data}
        for person in data:
            self._match_person(person, data)

    def _match_person(self, person, all_people):
        if not type(person) is Person:
            raise TypeError('Can only match a person')

        matching_set = {person}
        marked_people = set()
        for number in person.marked_numbers:
            try:
                marked_people.add(self._everyone[number])
            except KeyError:
                continue

        for other_person in marked_people:
            if self._matches_everyone_in_set_of_people(other_person, matching_set):
                matching_set.add(other_person)
        matching_set.remove(person)

        person.results.matches = matching_set

    @staticmethod
    def _matches_everyone_in_set_of_people(person, people):
        for other_person in people:
            if other_person.number not in person.marked_numbers:
                return False
        return True
