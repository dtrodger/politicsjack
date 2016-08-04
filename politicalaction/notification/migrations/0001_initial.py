# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cause', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=1)),
                ('image', models.ImageField(null=True, upload_to=b'')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('expiration_date', models.DateTimeField()),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('cause', models.ManyToManyField(to='cause.Cause')),
            ],
        ),
    ]
