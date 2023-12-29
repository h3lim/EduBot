# Generated by Django 5.0 on 2023-12-28 06:54

import config.asset_storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_auto_20231223_1352"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lecture",
            old_name="grade",
            new_name="rating",
        ),
        migrations.RenameField(
            model_name="lecture",
            old_name="reamin_time",
            new_name="remain_time",
        ),
        migrations.RenameField(
            model_name="lecture",
            old_name="visited",
            new_name="student_count",
        ),
        migrations.RenameField(
            model_name="lecture",
            old_name="chapter",
            new_name="subject",
        ),
        migrations.AddField(
            model_name="lecture",
            name="teacher",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="lecture",
            name="thumbnail",
            field=models.ImageField(
                default="default_thumbnail.jpg",
                storage=config.asset_storage.MediaStorage(),
                upload_to="images/",
            ),
        ),
    ]