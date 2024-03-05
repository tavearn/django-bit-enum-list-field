from django.db.models import Model, TextField

from events.enums import Weekdays
from lib.bit_enum_list_field import BitEnumListField


class Event(Model):
    name = TextField()
    days = BitEnumListField(Weekdays)
