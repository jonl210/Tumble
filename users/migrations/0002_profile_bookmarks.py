# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-16 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_bookmark_date'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bookmarks',
            field=models.ManyToManyField(to='bookmarks.Bookmark'),
        ),
    ]
