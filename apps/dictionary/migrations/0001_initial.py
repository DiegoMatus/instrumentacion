# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.dictionary.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumentation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=200, verbose_name='Nombre')),
                ('definition', models.TextField(verbose_name='Definición')),
                ('image', models.FileField(upload_to=apps.dictionary.models.get_path_instrumentation)),
            ],
            options={
                'verbose_name_plural': 'Instrumentos',
                'verbose_name': 'Instrumento',
            },
        ),
    ]
