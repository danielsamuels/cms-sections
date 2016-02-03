# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import cms.models.fields
import cms.apps.media.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20151002_1655'),
        ('media', '0002_auto_20150713_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('page', models.OneToOneField(related_name='+', primary_key=True, serialize=False, editable=False, to='pages.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, choices=[(b'homepage-hero', b'Homepage hero'), (b'landing-hero', b'Landing hero'), (b'dual-column', b'Dual column'), (b'form', b'Form'), (b'keyline', b'Keyline')])),
                ('title', models.CharField(max_length=140, null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('content', cms.models.fields.HtmlField(null=True, blank=True)),
                ('button_text', models.CharField(max_length=100, null=True, blank=True)),
                ('button_url', models.CharField(max_length=200, null=True, verbose_name=b'button URL', blank=True)),
                ('order', models.PositiveIntegerField(default=0, help_text=b'Order which the section will be displayed')),
                ('image', cms.apps.media.models.ImageRefField(related_name='+', on_delete=django.db.models.deletion.PROTECT, blank=True, to='media.File', null=True)),
                ('page', models.ForeignKey(to='pages.Page')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
