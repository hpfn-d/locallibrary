# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170316_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
    ]
