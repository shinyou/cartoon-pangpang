# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=10)),
                ('password', models.IntegerField(max_length=15)),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
    ]
