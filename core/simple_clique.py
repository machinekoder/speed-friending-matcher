# -*- coding: utf-8 -*-
from core.person import Person


class SimpleClique(object):
    def __init__(self):
        self.seen = None
        self.everyone = None

    def run(self, data):
        """Set person.result.matches for everyone in data.

        Args:
          data: A list of Person objects
        """
        self.everyone = {person.number: person for person in data}
        for person in data:
            self.seen = set()
            clique = set()
            self._clique_search(person, clique)
            person.results.matches = clique

    def _clique_search(self, person, clique):
        """Perform a depth first search for a clique.

        Args:
          person: A Person object
          clique: a set of Person objects, the return.
        """
        if not type(person) is Person:
            raise TypeError('Can only clique a person')
        if person.number in self.seen:
            return
        self.seen.add(person.number)
        clique.add(person)
        for other_number in person.marked_numbers:
            try:
                other = self.everyone[other_number]
            except KeyError:
                continue
            if person.number in other.marked_numbers:
                self._clique_search(other, clique)
