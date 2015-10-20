# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumentation',
            name='tags',
            field=models.CharField(default='tags', verbose_name='Tags', max_length=200),
            preserve_default=False,
        ),
    ]
