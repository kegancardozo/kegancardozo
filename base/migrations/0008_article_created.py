# Generated by Django 4.1 on 2022-09-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_article_body_alter_article_title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
