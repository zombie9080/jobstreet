# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20151029_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=40),
        ),
    ]
