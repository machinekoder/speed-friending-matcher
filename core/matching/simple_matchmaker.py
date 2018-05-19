# -*- coding: utf-8 -*-
from core.person import Person


class SimpleMatchmaker(object):
    def __init__(self):
        pass

    def run(self, data):
        for person in data:
            self._match_person(person, data)

    def _match_person(self, person, all_people):
        if not type(person) is Person:
            raise TypeError('Can only match a person')

        for other_person in all_people:
            self._match_two_people(person, other_person)

        person.results.matches = set.intersection(person.results.marked_by_me, person.results.marked_me)

    def _match_two_people(self, person, other_person):
        if person is other_person:
            return

        if person.number in other_person.marked_numbers:
            person.results.add_marked_me(other_person)

        if other_person.number in person.marked_numbers:
            person.results.add_marked_by_me(other_person)