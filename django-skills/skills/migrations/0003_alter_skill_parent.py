# Generated by Django 4.0.6 on 2022-07-25 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_alter_skill_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='skills.skill'),
        ),
    ]