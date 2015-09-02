# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20150831_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bus_no', models.CharField(max_length=10)),
                ('device_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='travel',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='bus_no',
        ),
        migrations.DeleteModel(
            name='Travel',
        ),
        migrations.AddField(
            model_name='student',
            name='bus',
            field=models.ForeignKey(default=0, to='student.Bus'),
            preserve_default=False,
        ),
    ]
