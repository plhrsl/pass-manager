# Generated by Django 4.1.5 on 2023-01-10 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pass", "0002_rename_pass_password_rename_pw_password_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="Access",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=60)),
                ("password", models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name="Password",
        ),
    ]
