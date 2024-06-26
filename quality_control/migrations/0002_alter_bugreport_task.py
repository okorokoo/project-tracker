# Generated by Django 5.0.4 on 2024-04-29 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quality_control", "0001_initial"),
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bugreport",
            name="task",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bug_reports",
                to="tasks.task",
            ),
        ),
    ]
