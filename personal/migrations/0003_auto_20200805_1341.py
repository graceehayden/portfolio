# Generated by Django 2.2.12 on 2020-08-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20200805_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
