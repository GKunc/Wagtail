# Generated by Django 4.2.13 on 2024-06-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_remove_contactpage_page_title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactpage",
            name="page_title",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
