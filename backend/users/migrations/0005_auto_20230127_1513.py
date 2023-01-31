# Generated by Django 3.2 on 2023-01-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook_url',
            field=models.URLField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter_url',
            field=models.URLField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vk_url',
            field=models.URLField(blank=True, max_length=256, null=True),
        ),
    ]