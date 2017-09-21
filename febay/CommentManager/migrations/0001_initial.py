# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-21 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManager', '0001_initial'),
        ('ItemManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ItemManager.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManager.customer')),
            ],
        ),
    ]