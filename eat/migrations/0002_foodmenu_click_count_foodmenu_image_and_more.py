# Generated by Django 4.1.4 on 2023-01-31 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("eat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="foodmenu",
            name="click_count",
            field=models.PositiveIntegerField(default=0, verbose_name="뭐먹지 클릭수"),
        ),
        migrations.AddField(
            model_name="foodmenu",
            name="image",
            field=models.ImageField(
                default="eatmenu/pizza.png",
                upload_to="eatmenu/",
                verbose_name="뭐먹지 이미지",
            ),
        ),
        migrations.AlterField(
            model_name="foodcategory",
            name="category",
            field=models.CharField(max_length=50, verbose_name="뭐먹지 카테고리"),
        ),
        migrations.AlterField(
            model_name="foodmenu",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="eat.foodcategory",
                verbose_name="뭐먹지 카테고리",
            ),
        ),
        migrations.AlterField(
            model_name="foodmenu",
            name="menu",
            field=models.CharField(max_length=50, verbose_name="뭐먹지 메뉴"),
        ),
    ]
