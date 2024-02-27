# Generated by Django 5.0.1 on 2024-02-27 12:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=150)),
                ('series', models.IntegerField()),
                ('repetitions', models.IntegerField()),
                ('charge', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=150)),
                ('days', models.IntegerField()),
                ('week_series', models.IntegerField()),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cover', models.ImageField(upload_to='trainsheet/covers/%Y/%m/%d/')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('exercises', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainingsheet.exercise')),
            ],
        ),
    ]