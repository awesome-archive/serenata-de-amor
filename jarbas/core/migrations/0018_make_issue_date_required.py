# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_make_some_fields_optional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reimbursement',
            name='issue_date',
            field=models.DateField(verbose_name='Issue date'),
        ),
    ]
