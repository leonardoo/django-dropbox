# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_dropbox.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestDropbox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_test', models.FileField(storage=django_dropbox.storage.DropboxStorage(location=b'/test/djangodropbox'), null=True, upload_to=b'.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
