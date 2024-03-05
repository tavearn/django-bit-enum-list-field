from django.test import TransactionTestCase

from events.enums import Weekdays
from events.models import Event
from lib.bit_enum_list_field import BitEnumListField


class TestDbQuery(TransactionTestCase):
    def setUp(self):
        combos = [
            [Weekdays.Tuesday, Weekdays.Friday],
            [Weekdays.Monday, Weekdays.Tuesday],
            [Weekdays.Friday, Weekdays.Saturday, Weekdays.Sunday],
            [],
            [Weekdays.Saturday]
        ]
        for i, combo in enumerate(combos):
            Event(
                name=f"Test Event {i}",
                days=combo
            ).save()

    def test_get_all_single_day_one(self):
        assert Event.objects.filter(days__all=[Weekdays.Monday]).count() == 1, \
            "Unable to fetch single event with a 1-day match"

    def test_get_all_single_day_many(self):
        assert Event.objects.filter(days__all=[Weekdays.Tuesday, Weekdays.Friday]).count() == 1, \
            "Unable to fetch single event with a many-day match"

    def test_get_all_multiple_days_one(self):
        assert Event.objects.filter(days__all=[Weekdays.Tuesday]).count() == 2, \
            "Unable to fetch multiple events with a 1-day match"

    def test_get_any(self):
        assert Event.objects.filter(days__any=[Weekdays.Monday, Weekdays.Friday]).count() == 3, \
            "Unable to fetch events with any of the specified days"

    def test_get_none(self):
        assert Event.objects.filter(days__none=[Weekdays.Tuesday, Weekdays.Friday]).count() == 2, \
            "Unable to fetch events without any of the specified days"

    def test_get_single_day_mask(self):
        query = BitEnumListField.to_bit_value(Weekdays.Saturday) | BitEnumListField.to_bit_value(Weekdays.Sunday)
        assert Event.objects.filter(days__all=query).count() == 1, \
            "Unable to fetch single event with bitwise mask"
