# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20151029_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='expected_salary',
            field=models.CharField(max_length=2, choices=[(b'0', b'\xe9\x9d\xa2\xe8\xae\xae'), (b'1', b'2000-2999'), (b'2', b'3000-4499'), (b'3', b'4500-5999'), (b'4', b'6000-7999'), (b'5', b'8000-9999'), (b'6', b'10000-14999'), (b'7', b'15000-19999'), (b'8', b'20000-24999'), (b'9', b'25000-29999'), (b'10', b'30000-39999'), (b'11', b'40000-49999'), (b'12', b'50000-69999'), (b'13', b'70000-99999'), (b'14', b'100000\xe4\xbb\xa5\xe4\xb8\x8a')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'0', b'\xe9\x9d\xa2\xe8\xae\xae'), (b'1', b'2000-2999'), (b'2', b'3000-4499'), (b'3', b'4500-5999'), (b'4', b'6000-7999'), (b'5', b'8000-9999'), (b'6', b'10000-14999'), (b'7', b'15000-19999'), (b'8', b'20000-24999'), (b'9', b'25000-29999'), (b'10', b'30000-39999'), (b'11', b'40000-49999'), (b'12', b'50000-69999'), (b'13', b'70000-99999'), (b'14', b'100000\xe4\xbb\xa5\xe4\xb8\x8a')]),
        ),
    ]
