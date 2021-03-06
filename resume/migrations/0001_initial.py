# Generated by Django 3.1.1 on 2020-10-03 14:34

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20201003_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='published_resumes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('attachment', models.FileField(upload_to='papers')),
                ('publish_date', models.DateField(auto_now=True)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.journal')),
                ('legacy_users', models.ManyToManyField(related_name='papers', to='user.LegacyUser')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='papers', to='resume.resume')),
                ('users', models.ManyToManyField(related_name='papers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('science', models.CharField(choices=[('MT', 'Mathematics'), ('PH', 'Sophomore'), ('PY', 'Physics'), ('CH', 'Chemistry'), ('BI', 'Biology'), ('GR', 'GENERAL')], default='GR', max_length=2)),
                ('legacy_users', models.ManyToManyField(related_name='fields', to='user.LegacyUser')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resumes', to='resume.resume')),
                ('users', models.ManyToManyField(related_name='fields', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
