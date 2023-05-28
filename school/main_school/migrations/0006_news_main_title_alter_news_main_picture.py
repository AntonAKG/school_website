# Generated by Django 4.2.1 on 2023-05-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_school', '0005_news_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_main',
            name='title',
            field=models.CharField(default=2, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news_main',
            name='picture',
            field=models.ImageField(null=True, upload_to='images_news'),
        ),
    ]