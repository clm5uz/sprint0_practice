# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formtest', '0002_auto_20160326_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='public_key',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
