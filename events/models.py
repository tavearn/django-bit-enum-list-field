from django.db.models import Model, TextField

from events.enums import Weekdays
from bit_enum_list_field.bit_enum_list_field import BitEnumListField


class Event(Model):
    name = TextField()
    days = BitEnumListField(Weekdays)


class EventWithEmptyDefault(Model):
    name = TextField()
    days = BitEnumListField(Weekdays, default=[])


class EventWithDefault(Model):
    default_days = [Weekdays.Monday, Weekdays.Tuesday]
    name = TextField()
    days = BitEnumListField(Weekdays, default=default_days)
