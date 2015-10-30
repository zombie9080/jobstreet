# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20151022_0400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-create_date']},
        ),
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(default=b'u33569400553641067398fm23gp0.jpg', upload_to=b'static/upload/avatar'),
        ),
    ]
