# Generated by Django 4.2.1 on 2023-05-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_school', '0011_remove_teacher_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]