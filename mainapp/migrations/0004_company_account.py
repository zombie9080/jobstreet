# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_company_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='account',
            field=models.CharField(default='account', max_length=50),
            preserve_default=False,
        ),
    ]
