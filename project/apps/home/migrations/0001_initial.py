# Generated by Django 5.0 on 2024-12-08 21:00

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', models.DateField()),
                ('to', models.DateField()),
            ],
            options={
                'verbose_name': 'Calendar',
                'verbose_name_plural': 'Calendars',
                'db_table': 'calendars',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DocumentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('C', 'Calendar'), ('A', 'Anti Doping'), ('R', 'Rule')])),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'db_table': 'documents',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('file', models.FileField(upload_to='images/')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('for_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='CalendarModelTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=256)),
                ('organizer', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='home.calendarmodel')),
            ],
            options={
                'verbose_name': 'Calendar Translation',
                'db_table': 'calendars_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DocumentModelTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=64)),
                ('file', models.FileField(upload_to='documents/')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='home.documentmodel')),
            ],
            options={
                'verbose_name': 'Document Translation',
                'db_table': 'documents_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
