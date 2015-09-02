# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20150902_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='bus_no',
            field=models.CharField(max_length=20),
        ),
    ]
