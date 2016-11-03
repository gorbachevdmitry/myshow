# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttranslation',
            old_name='description',
            new_name='anecdot',
        ),
        migrations.AddField(
            model_name='product',
            name='alt_image',
            field=models.CharField(max_length=250, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='alt_image_dog',
            field=models.CharField(max_length=250, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_dog',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttranslation',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='producttranslation',
            name='citata',
            field=models.TextField(blank=True),
        ),
    ]
