# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 13:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamber_of_deputies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalreimbursement',
            name='history_user',
        ),
        migrations.AlterModelTable(
            name='reimbursement',
            table=None,
        ),
        migrations.AlterModelTable(
            name='tweet',
            table=None,
        ),
        migrations.DeleteModel(
            name='HistoricalReimbursement',
        ),
    ]
