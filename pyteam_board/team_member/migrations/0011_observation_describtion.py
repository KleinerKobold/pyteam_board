# Generated by Django 4.0.6 on 2022-08-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_member', '0010_observation_observed_observation_persons'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='describtion',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
