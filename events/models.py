from django.db.models import Model, TextField

from events.enums import Weekdays
from bit_enum_list_field.bit_enum_list_field import BitEnumListField


class Event(Model):
    name = TextField()
    days = BitEnumListField(Weekdays)
