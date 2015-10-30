# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20151028_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
