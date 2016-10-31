# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('joined', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('members', models.ManyToManyField(related_name='alarm_members', to='customer.Customer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]