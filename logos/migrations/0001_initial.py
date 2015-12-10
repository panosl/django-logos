# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField(verbose_name='body text', blank=True)),
                ('allow_comments', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=True, help_text='Determines if it will be displayed at the website.', verbose_name='it is published')),
                ('is_pinned', models.BooleanField(default=False, help_text='Determines if it will remain on top even if newer posts are made.', verbose_name='is it pinned?')),
            ],
            options={
                'ordering': ('-pub_date',),
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('taggit.tag',),
        ),
        migrations.CreateModel(
            name='TaggedPost',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('taggit.taggeditem',),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='logos.TaggedPost', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
