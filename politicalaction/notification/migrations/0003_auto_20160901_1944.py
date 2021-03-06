# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20160901_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='notification',
            name='expiration_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='notification',
            name='modified',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
