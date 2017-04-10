# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_order', '0003_orderinfo_oaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='odate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
