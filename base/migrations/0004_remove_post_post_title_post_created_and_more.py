# Generated by Django 4.1 on 2022-09-18 21:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_post"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="post_title",),
        migrations.AddField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="post_caption",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="post",
            name="post_image",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
