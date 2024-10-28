# Generated by Django 5.1.1 on 2024-10-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0008_student_hostel_assigned"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="status",
            field=models.CharField(
                choices=[
                    ("Active", "Active"),
                    ("Inactive", "Inactive"),
                    ("Graduated", "Graduated"),
                    ("Dropped", "Dropped"),
                    ("Suspended", "Suspended"),
                    ("Pending Check-In", "Pending Check-In"),
                ],
                max_length=255,
            ),
        ),
    ]
