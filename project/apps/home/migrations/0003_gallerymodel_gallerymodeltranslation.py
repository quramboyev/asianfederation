# Generated by Django 5.0 on 2025-02-08 22:20

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_aboutusmodel_goalmodel_calendarmodel_country_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
                'db_table': 'galleries',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GalleryModelTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('description', models.TextField(verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='home.gallerymodel')),
            ],
            options={
                'verbose_name': 'Gallery Translation',
                'db_table': 'galleries_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
