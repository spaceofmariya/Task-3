# Generated by Django 4.2.1 on 2023-05-20 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registered", "0003_alter_form_date_of_birth_alter_form_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="date_of_birth",
            field=models.DateField(default=datetime.date(2023, 5, 20)),
        ),
    ]