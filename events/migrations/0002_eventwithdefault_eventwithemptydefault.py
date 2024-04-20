# Generated by Django 5.0.3 on 2024-04-20 12:52

import bit_enum_list_field.bit_enum_list_field
import events.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventWithDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('days', bit_enum_list_field.bit_enum_list_field.BitEnumListField(
                    events.enums.Weekdays,
                    default=[events.enums.Weekdays['Monday'], events.enums.Weekdays['Tuesday']]
                )),
            ],
        ),
        migrations.CreateModel(
            name='EventWithEmptyDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('days', bit_enum_list_field.bit_enum_list_field.BitEnumListField(events.enums.Weekdays, default=[])),
            ],
        ),
    ]