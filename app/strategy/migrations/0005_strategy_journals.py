# Generated by Django 4.1.4 on 2022-12-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0004_remove_strategylogicoperation_first_variable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='journals',
            field=models.JSONField(blank=True, null=True),
        ),
    ]