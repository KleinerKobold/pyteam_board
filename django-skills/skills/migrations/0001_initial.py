# Generated by Django 4.0.6 on 2022-07-25 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('beginner', models.CharField(blank=True, max_length=1024, null=True)),
                ('intermediate', models.CharField(blank=True, max_length=1024, null=True)),
                ('expert', models.CharField(blank=True, max_length=1024, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.skill')),
            ],
        ),
    ]
