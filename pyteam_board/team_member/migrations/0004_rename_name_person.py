# Generated by Django 4.0.6 on 2022-07-24 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_member', '0003_rename_exprience_experience'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Name',
            new_name='Person',
        ),
    ]
