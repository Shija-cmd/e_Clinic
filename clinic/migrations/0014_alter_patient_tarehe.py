# Generated by Django 5.0 on 2024-08-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinic", "0013_patient_tarehe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="tarehe",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
