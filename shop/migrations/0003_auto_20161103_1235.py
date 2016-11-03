# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20161103_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='slug',
            field=models.SlugField(unique_for_date='publish', max_length=200),
        ),
    ]
