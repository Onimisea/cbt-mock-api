# Generated by Django 4.1.5 on 2023-02-03 14:06

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="question",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                verbose_name="Question"
            ),
        ),
    ]
