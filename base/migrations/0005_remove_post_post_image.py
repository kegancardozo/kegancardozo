# Generated by Django 4.1 on 2022-09-19 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_remove_post_post_title_post_created_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="post_image",),
    ]