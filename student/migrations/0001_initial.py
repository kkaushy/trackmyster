# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('tag_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('bus_no', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('class_num', models.IntegerField()),
                ('school', models.CharField(max_length=200)),
                ('mobile_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=5)),
                ('time', models.IntegerField()),
                ('student', models.ForeignKey(to='student.Student')),
            ],
        ),
    ]
