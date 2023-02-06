# Generated by Django 4.1.4 on 2023-02-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("review", "0002_alter_review_content_alter_review_grade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="photo",
            field=models.ImageField(blank=True, upload_to="review_upload/"),
        ),
        migrations.AlterField(
            model_name="store",
            name="photo",
            field=models.ImageField(
                blank=True, default="store/drink_default.png", upload_to="store/"
            ),
        ),
    ]
