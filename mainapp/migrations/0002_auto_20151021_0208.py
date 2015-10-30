# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='welfare',
            name='attach',
        ),
        migrations.AddField(
            model_name='job',
            name='attach_welfare',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=2, choices=[(b'bj', b'\xe5\x8c\x97\xe4\xba\xac'), (b'sh', b'\xe4\xb8\x8a\xe6\xb5\xb7'), (b'gz', b'\xe5\xb9\xbf\xe5\xb7\x9e'), (b'SZ', b'\xe6\xb7\xb1\xe5\x9c\xb3'), (b'wh', b'\xe6\xad\xa6\xe6\xb1\x89'), (b'xa', b'\xe8\xa5\xbf\xe5\xae\x89'), (b'hz', b'\xe6\x9d\xad\xe5\xb7\x9e'), (b'nj', b'\xe5\x8d\x97\xe4\xba\xac'), (b'cd', b'\xe6\x88\x90\xe9\x83\xbd'), (b'cq', b'\xe9\x87\x8d\xe5\xba\x86'), (b'dw', b'\xe4\xb8\x9c\xe8\x8e\x9e'), (b'dl', b'\xe5\xa4\xa7\xe8\xbf\x9e'), (b'sy', b'\xe6\xb2\x88\xe9\x98\xb3'), (b'sz', b'\xe8\x8b\x8f\xe5\xb7\x9e'), (b'km', b'\xe6\x98\x86\xe6\x98\x8e'), (b'cs', b'\xe9\x95\xbf\xe6\xb2\x99'), (b'hf', b'\xe5\x90\x88\xe8\x82\xa5'), (b'lb', b'\xe5\xae\x81\xe6\xb3\xa2'), (b'zz', b'\xe9\x83\x91\xe5\xb7\x9e'), (b'tj', b'\xe5\xa4\xa9\xe6\xb4\xa5'), (b'qd', b'\xe9\x9d\x92\xe5\xb2\x9b'), (b'jn', b'\xe6\xb5\x8e\xe5\x8d\x97'), (b'heb', b'\xe5\x93\x88\xe5\xb0\x94\xe6\xbb\xa8'), (b'cc', b'\xe9\x95\xbf\xe6\x98\xa5'), (b'fz', b'\xe7\xa6\x8f\xe5\xb7\x9e')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(default=b'u33569400553641067398fm23gp0.jpg', upload_to=b'upload/avatar'),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=3, choices=[(b'bj', b'\xe5\x8c\x97\xe4\xba\xac'), (b'sh', b'\xe4\xb8\x8a\xe6\xb5\xb7'), (b'gz', b'\xe5\xb9\xbf\xe5\xb7\x9e'), (b'SZ', b'\xe6\xb7\xb1\xe5\x9c\xb3'), (b'wh', b'\xe6\xad\xa6\xe6\xb1\x89'), (b'xa', b'\xe8\xa5\xbf\xe5\xae\x89'), (b'hz', b'\xe6\x9d\xad\xe5\xb7\x9e'), (b'nj', b'\xe5\x8d\x97\xe4\xba\xac'), (b'cd', b'\xe6\x88\x90\xe9\x83\xbd'), (b'cq', b'\xe9\x87\x8d\xe5\xba\x86'), (b'dw', b'\xe4\xb8\x9c\xe8\x8e\x9e'), (b'dl', b'\xe5\xa4\xa7\xe8\xbf\x9e'), (b'sy', b'\xe6\xb2\x88\xe9\x98\xb3'), (b'sz', b'\xe8\x8b\x8f\xe5\xb7\x9e'), (b'km', b'\xe6\x98\x86\xe6\x98\x8e'), (b'cs', b'\xe9\x95\xbf\xe6\xb2\x99'), (b'hf', b'\xe5\x90\x88\xe8\x82\xa5'), (b'lb', b'\xe5\xae\x81\xe6\xb3\xa2'), (b'zz', b'\xe9\x83\x91\xe5\xb7\x9e'), (b'tj', b'\xe5\xa4\xa9\xe6\xb4\xa5'), (b'qd', b'\xe9\x9d\x92\xe5\xb2\x9b'), (b'jn', b'\xe6\xb5\x8e\xe5\x8d\x97'), (b'heb', b'\xe5\x93\x88\xe5\xb0\x94\xe6\xbb\xa8'), (b'cc', b'\xe9\x95\xbf\xe6\x98\xa5'), (b'fz', b'\xe7\xa6\x8f\xe5\xb7\x9e')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='collection',
            field=models.ManyToManyField(related_name='+', null=True, to='mainapp.Job', blank=True),
        ),
    ]
