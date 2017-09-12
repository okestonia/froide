# -*- coding: utf-8 -*-
# Generated by Django 1.11.5.dev20170903160518 on 2017-09-12 08:36
from __future__ import unicode_literals

from django.db import migrations


def set_email_null(apps, schema_editor):
    User = apps.get_model('account', 'User')
    User.objects.filter(email__exact='').update(email=None)


def set_email_empty(apps, schema_editor):
    User = apps.get_model('account', 'User')
    User.objects.filter(email__isnull=True).update(email='')


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20170912_1032'),
    ]

    operations = [
        migrations.RunPython(set_email_null, set_email_empty),
    ]
