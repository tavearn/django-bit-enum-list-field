from django.test import TransactionTestCase

from events.enums import Weekdays
from events.models import EventWithEmptyDefault, EventWithDefault, Event


class TestDefaultValues(TransactionTestCase):
    def test_empty_default_value(self):
        my_event = EventWithEmptyDefault(name="MyEvent")
        try:
            my_event.save()
        except Exception as ex:
            self.fail(f"Exception raised: {ex}")

        assert len(my_event.days) == 0, "Default value for `EventWithEmptyDefault` should be an empty list"

        db_event = EventWithEmptyDefault.objects.first()

        assert db_event is not None, "`EventWithEmptyDefault` is not persisted on the database"
        assert db_event.days == my_event.days, ("Persisted default value for `EventWithEmptyDefault` "
                                                "must be equal to the model value")

    def test_default_value(self):
        my_event = EventWithDefault(name="MyEvent")
        try:
            my_event.save()
        except Exception as ex:
            self.fail(f"Exception raised: {ex}")

        assert len(my_event.days) == 2, "Default value for `EventWithDefault` should contain 2 elements"
        for day in Weekdays:
            if day in EventWithDefault.default_days:
                assert day in my_event.days, f"Default value for `EventWithDefault` should contain `{day}`"
            else:
                assert day not in my_event.days, f"Default value for `EventWithDefault` should NOT contain `{day}`"

        db_event = EventWithDefault.objects.first()

        assert db_event is not None, "`EventWithDefault` is not persisted on the database"
        assert db_event.days == my_event.days, ("Persisted default value for `EventWithDefault` "
                                                "must be equal to the model value")

    def test_implicit_default(self):
        my_event = Event(name="MyEvent")
        try:
            my_event.save()
        except Exception as ex:
            self.fail(f"Exception raised: {ex}")

        assert len(my_event.days) == 0, "Default value for `Event` should be an empty list"

        db_event = Event.objects.first()

        assert db_event is not None, "`Event` is not persisted on the database"
        assert db_event.days == my_event.days, ("Persisted default value for `Event` "
                                                "must be equal to the model value")
