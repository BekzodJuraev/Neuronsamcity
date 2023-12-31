# Generated by Django 3.2.4 on 2021-08-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Обпубликовано')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'отзывы',
                'ordering': ['created_at'],
            },
        ),
    ]
