from django.test import TransactionTestCase

from events.enums import Weekdays
from events.models import Event


class TestModelCrud(TransactionTestCase):
    def setUp(self):
        Event(
            name="Test Event",
            days=[Weekdays.Tuesday, Weekdays.Friday]
        ).save()

    def test_create_model(self):
        assert Event.objects.count() == 1, "Event object has not been created"

    def test_read_model(self):
        event = Event.objects.all().first()
        assert event.days == [Weekdays.Tuesday, Weekdays.Friday], "Incorrect days value"

    def test_update_model(self):
        event = Event.objects.all().first()
        event.days = [Weekdays.Monday, Weekdays.Tuesday]
        event.save()

        assert Event.objects.count() == 1, "Another object has been created instead of updating the existing one"

        reloaded_event = Event.objects.all().first()
        assert reloaded_event.days == [Weekdays.Monday, Weekdays.Tuesday], "Incorrect days value after update"

    def test_model_delete(self):
        event = Event.objects.all().first()
        event.delete()

        assert Event.objects.count() == 0, "Event has not been deleted"
