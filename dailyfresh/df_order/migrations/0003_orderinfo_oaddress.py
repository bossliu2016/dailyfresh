# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_order', '0002_orderinfo_ototal'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='oaddress',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
