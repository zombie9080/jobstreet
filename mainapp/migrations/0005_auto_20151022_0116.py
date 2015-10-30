# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_company_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='account_name',
            new_name='account',
        ),
    ]
