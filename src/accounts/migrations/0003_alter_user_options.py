# Generated by Django 5.0.6 on 2024-06-19 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ["id"]},
        ),
    ]