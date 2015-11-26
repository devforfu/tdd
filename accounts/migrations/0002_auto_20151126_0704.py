# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listuser',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user'),
        ),
        migrations.AddField(
            model_name='listuser',
            name='is_superuser',
            field=models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.'),
        ),
        migrations.AddField(
            model_name='listuser',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user'),
        ),
    ]
