# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 01:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20161225_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='number_of_books',
        ),
    ]
