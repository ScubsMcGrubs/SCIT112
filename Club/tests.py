from django.test import TestCase
from .models import Meeting, Meeting_Minutes, Resource, Event
from django.contrib.auth.models import User
from .forms import ResourceForm, MeetingForm
from django.urls import reverse_lazy, reverse

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


class NewMeetingForm(TestCase):
    def test_meetingform(self):
        data = {'meetName' : 'Important Meeting', 'date' : '02/17/21', 'time' : '15:00:00', 
       'location' : 'Python Clubhouse', 'agenda' : 'We will discuss stuff'}
        form = MeetingForm(data)
        self.assertTrue(form.is_valid)

    def test_meetingform_invalid(self):
        # FAILED
        data = {'meetName' : 'Important Meeting', 'date' : 'February 16 2021', 'time' : '3:00pm', 
       'location' : 'Python Clubhouse', 'agenda' : 'We will discuss stuff'}
        form = MeetingForm(data)
        self.assertFalse(form.is_valid)



class NewResourceForm(TestCase):
    def test_resourceform(self):
        data = {'resname' : 'Google', 'restype' : 'Search Engine', 'URL' : 'https://www.google.com', 
       'date_entered' : '02/16/21', 'userID' : 'Simon'}
        form = ResourceForm(data)
        self.assertTrue(form.is_valid)

    def test_resourceform_invalid(self):
        # FAILED
        data = {'resname' : 'Google', 'restype' : 'Search Engine', 'URL' : 'https://www.google.com', 
       'date_entered' : 'Februaryy 16 2021', 'userID' : 'Simon'}
        form = ResourceForm(data)
        self.assertFalse(form.is_valid)


class NewMeetingAuthenticationsTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password = 'P@ssw0rd')
        self.meeting = Meeting('Urgent Meeting', '03/01/21', '15:00:00', 'Python Club HQ', 'We will discuss stuff')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, 'accounts/login/?next=/club/newmeeting/')

        
# Create your tests here.
