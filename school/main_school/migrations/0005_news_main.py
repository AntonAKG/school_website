# Generated by Django 4.2.1 on 2023-05-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_school', '0004_сall_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images_news')),
                ('date_public', models.DateTimeField()),
                ('text_news', models.TextField()),
            ],
        ),
    ]