# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20151029_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_progress',
            name='progress',
            field=models.CharField(default=b'ap', max_length=2, choices=[(b'ap', b'Applicated'), (b'sc', b'Scanned'), (b'in', b'Interview'), (b'of', b'Offer')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='collection',
            field=models.ManyToManyField(related_name='+', to='mainapp.Job'),
        ),
    ]
