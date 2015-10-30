# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App_progress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('progress', models.CharField(max_length=2, choices=[(b'ap', b'Applicated'), (b'sc', b'Scanned'), (b'in', b'Interview'), (b'of', b'Offer')])),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('scale', models.CharField(max_length=1, choices=[(b'0', b'\xe5\xb0\x91\xe4\xba\x8e50\xe4\xba\xba'), (b'1', b'50-150\xe4\xba\xba'), (b'2', b'150-500\xe4\xba\xba'), (b'3', b'500-1000\xe4\xba\xba'), (b'4', b'1000-5000\xe4\xba\xba'), (b'5', b'5000-10000\xe4\xba\xba'), (b'6', b'10000\xe4\xba\xba\xe4\xbb\xa5\xe4\xb8\x8a')])),
                ('city', models.CharField(max_length=2, choices=[(b'bj', b'\xe5\x8c\x97\xe4\xba\xac'), (b'sh', b'\xe4\xb8\x8a\xe6\xb5\xb7'), (b'gz', b'\xe5\xb9\xbf\xe5\xb7\x9e'), (b'sz', b'\xe6\xb7\xb1\xe5\x9c\xb3'), (b'wh', b'\xe6\xad\xa6\xe6\xb1\x89'), (b'xa', b'\xe8\xa5\xbf\xe5\xae\x89'), (b'hz', b'\xe6\x9d\xad\xe5\xb7\x9e'), (b'nj', b'\xe5\x8d\x97\xe4\xba\xac'), (b'cd', b'\xe6\x88\x90\xe9\x83\xbd'), (b'cq', b'\xe9\x87\x8d\xe5\xba\x86'), (b'dw', b'\xe4\xb8\x9c\xe8\x8e\x9e'), (b'dl', b'\xe5\xa4\xa7\xe8\xbf\x9e'), (b'sy', b'\xe6\xb2\x88\xe9\x98\xb3'), (b'sz', b'\xe8\x8b\x8f\xe5\xb7\x9e'), (b'km', b'\xe6\x98\x86\xe6\x98\x8e'), (b'cs', b'\xe9\x95\xbf\xe6\xb2\x99'), (b'hf', b'\xe5\x90\x88\xe8\x82\xa5'), (b'lb', b'\xe5\xae\x81\xe6\xb3\xa2'), (b'zz', b'\xe9\x83\x91\xe5\xb7\x9e'), (b'tj', b'\xe5\xa4\xa9\xe6\xb4\xa5'), (b'qd', b'\xe9\x9d\x92\xe5\xb2\x9b'), (b'jn', b'\xe6\xb5\x8e\xe5\x8d\x97'), (b'heb', b'\xe5\x93\x88\xe5\xb0\x94\xe6\xbb\xa8'), (b'cc', b'\xe9\x95\xbf\xe6\x98\xa5'), (b'fz', b'\xe7\xa6\x8f\xe5\xb7\x9e')])),
                ('address', models.CharField(max_length=100)),
                ('summary', models.TextField()),
            ],
            options={
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('expected_salary', models.CharField(max_length=30)),
                ('job_objective', models.CharField(max_length=100)),
                ('technique', models.TextField()),
                ('experience', models.TextField()),
                ('evaluation', models.TextField()),
            ],
            options={
                'ordering': ['person'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('years', models.CharField(max_length=1, choices=[(b'0', b'\xe5\xba\x94\xe5\xb1\x8a\xe6\xaf\x95\xe4\xb8\x9a\xe7\x94\x9f'), (b'1', b'1~2\xe5\xb9\xb4'), (b'2', b'3~4\xe5\xb9\xb4'), (b'3', b'5\xe5\xb9\xb4\xe4\xbb\xa5\xe4\xb8\x8a')])),
                ('salary', models.CharField(max_length=1, choices=[(b'0', b'2000\xe4\xbb\xa5\xe4\xb8\x8b'), (b'1', b'2000-2999'), (b'2', b'3000-4499'), (b'3', b'4500-5999'), (b'4', b'6000-7999'), (b'5', b'8000-9999'), (b'6', b'10000-14999'), (b'7', b'15000-19999'), (b'8', b'20000-24999'), (b'9', b'25000-29999'), (b'10', b'30000-39999'), (b'11', b'40000-49999'), (b'12', b'50000-69999'), (b'13', b'70000-99999'), (b'14', b'100000\xe4\xbb\xa5\xe4\xb8\x8a')])),
                ('count', models.IntegerField(default=1)),
                ('technique', models.TextField()),
                ('duty', models.TextField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(to='mainapp.Company')),
            ],
            options={
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('true_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('avatar', models.ImageField(default=b'u33569400553641067398fm23gp0.jpg', height_field=80, width_field=60, upload_to=b'upload/avatar')),
                ('city', models.CharField(max_length=3, choices=[(b'bj', b'\xe5\x8c\x97\xe4\xba\xac'), (b'sh', b'\xe4\xb8\x8a\xe6\xb5\xb7'), (b'gz', b'\xe5\xb9\xbf\xe5\xb7\x9e'), (b'sz', b'\xe6\xb7\xb1\xe5\x9c\xb3'), (b'wh', b'\xe6\xad\xa6\xe6\xb1\x89'), (b'xa', b'\xe8\xa5\xbf\xe5\xae\x89'), (b'hz', b'\xe6\x9d\xad\xe5\xb7\x9e'), (b'nj', b'\xe5\x8d\x97\xe4\xba\xac'), (b'cd', b'\xe6\x88\x90\xe9\x83\xbd'), (b'cq', b'\xe9\x87\x8d\xe5\xba\x86'), (b'dw', b'\xe4\xb8\x9c\xe8\x8e\x9e'), (b'dl', b'\xe5\xa4\xa7\xe8\xbf\x9e'), (b'sy', b'\xe6\xb2\x88\xe9\x98\xb3'), (b'sz', b'\xe8\x8b\x8f\xe5\xb7\x9e'), (b'km', b'\xe6\x98\x86\xe6\x98\x8e'), (b'cs', b'\xe9\x95\xbf\xe6\xb2\x99'), (b'hf', b'\xe5\x90\x88\xe8\x82\xa5'), (b'lb', b'\xe5\xae\x81\xe6\xb3\xa2'), (b'zz', b'\xe9\x83\x91\xe5\xb7\x9e'), (b'tj', b'\xe5\xa4\xa9\xe6\xb4\xa5'), (b'qd', b'\xe9\x9d\x92\xe5\xb2\x9b'), (b'jn', b'\xe6\xb5\x8e\xe5\x8d\x97'), (b'heb', b'\xe5\x93\x88\xe5\xb0\x94\xe6\xbb\xa8'), (b'cc', b'\xe9\x95\xbf\xe6\x98\xa5'), (b'fz', b'\xe7\xa6\x8f\xe5\xb7\x9e')])),
                ('school', models.CharField(max_length=40)),
                ('app_record', models.ManyToManyField(to='mainapp.Job', through='mainapp.App_progress')),
                ('collection', models.ManyToManyField(related_name='+', to='mainapp.Job')),
            ],
            options={
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Welfare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('attach', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='tags',
            field=models.ManyToManyField(to='mainapp.Tag'),
        ),
        migrations.AddField(
            model_name='job',
            name='welfares',
            field=models.ManyToManyField(to='mainapp.Welfare'),
        ),
        migrations.AddField(
            model_name='cv',
            name='person',
            field=models.ForeignKey(to='mainapp.Person'),
        ),
        migrations.AddField(
            model_name='app_progress',
            name='job',
            field=models.ForeignKey(to='mainapp.Job'),
        ),
        migrations.AddField(
            model_name='app_progress',
            name='person',
            field=models.ForeignKey(to='mainapp.Person'),
        ),
    ]
