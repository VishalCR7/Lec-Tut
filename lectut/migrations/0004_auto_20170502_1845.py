# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-02 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectut', '0003_post_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.FileField(blank=True, null=True, upload_to=b'documents/%Y/%m/%d'),
        ),
    ]
