# Generated by Django 4.1.5 on 2023-01-10 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pass", "0003_access_delete_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="access",
            name="site",
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name="access",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="passwords",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]