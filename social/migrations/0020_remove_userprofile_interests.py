# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0019_interests_user_interests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='interests',
        ),
    ]
