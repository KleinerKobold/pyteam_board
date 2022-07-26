# Generated by Django 4.0.6 on 2022-08-02 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team_member', '0009_experience_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='observed on')),
            ],
        ),
        migrations.CreateModel(
            name='Observed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team_member.observation')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team_member.person')),
            ],
        ),
        migrations.AddField(
            model_name='observation',
            name='persons',
            field=models.ManyToManyField(through='team_member.Observed', to='team_member.person'),
        ),
    ]
