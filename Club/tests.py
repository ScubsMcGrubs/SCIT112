from django.test import TestCase
from .models import Meeting, Meeting_Minutes, Resource, Event

class MeetingTest(TestCase):
    def setUp(self):
        self.name = Meeting(meetName = 'First Meeting')

    def test_meetstring(self):
        self.assertEqual(str(self.name), 'First Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')


class MeetingMinutesTest(TestCase):
    def setUp(self):
        # meetID is a ForeignKey and requires an instance of 'Meeting' so I had to create one
        self.name = Meeting(meetName = 'Second Meeting')
        self.mins = Meeting_Minutes(meetID = self.name)

    def test_minsstring(self):
        self.assertEqual(str(self.mins), 'Second Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting_Minutes._meta.db_table), 'Meeting Minutes')


class ResourceTest(TestCase):
    def setUp(self):
        self.name = Resource(resname = 'Microsoft Teams')

    def test_meetstring(self):
        self.assertEqual(str(self.name), 'Microsoft Teams')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')


class EventTest(TestCase):
    def setUp(self):
        self.name = Event(eventName = 'Python Club Barbeque')

    def test_eventstring(self):
        self.assertEqual(str(self.name), 'Python Club Barbeque')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')

# Create your tests here.
