# Generated by Django 2.2 on 2019-04-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("authentication", "0004_auto_20190415_2029")]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="cipher",
            field=models.CharField(blank=True, default="", max_length=15, unique=True),
            preserve_default=False,
        )
    ]
