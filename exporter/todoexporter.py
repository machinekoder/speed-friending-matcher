from .exporter import Exporter


TEXT_TEMPLATE = '''
============================
Send to %(name)s, %(email)s, %(phone)s the following message:

Hi %(name)s, here are your contacts with people you can reach out to
(people that marked you with an "x" and you marked them with an "x"):

You marked:
%(marked)s

You got marked by:
%(got_marked)s

Your matches:
%(matches)s

You can also find all other contacts here: http://goo.gl/123xyz
or on meetup here: https://www.meetup.com/speed-friending-events/members/
'''


class TodoExporter(Exporter):
    def __init__(self, filename):
        Exporter.__init__(self)
        self._filename = filename

    def export_data(self, data):
        with open(self._filename, 'wt') as todo_file:
            for person in data:
                self._export_person(person, todo_file)

    def _export_person(self, person, todo_file):
        todo_file.write(self._create_person_todo_string(person))

    def _create_person_todo_string(self, person):
        def sort(results):
            return sorted(results, key=lambda x: x.number)
        marked_by_me = []
        for p in sort(person.results.marked_by_me):
            marked_by_me.append(self._create_person_simple_string(p))
        marked_me = []
        for p in sort(person.results.marked_me):
            marked_me.append(self._create_person_simple_string(p))
        matches = []
        for p in sort(person.results.matches):
            matches.append(self._create_person_simple_string(p))
        return TEXT_TEMPLATE % {'name': person.name, 'email': person.email, 'phone': person.phone,
                                'marked': '\n'.join(marked_by_me), 'got_marked': '\n'.join(marked_me),
                                'matches': '\n'.join(matches)}

    @staticmethod
    def _create_person_simple_string(person):
        data = [str(person.number), person.name]
        if person.email is not '':
            data.append(person.email)
        if person.phone is not '':
            data.append(person.phone)
        return ', '.join(data)


exporter = TodoExporter
