# Generated by Django 3.1.2 on 2021-01-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top100', '0003_auto_20210118_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image_url',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='rank',
            field=models.IntegerField(default=None, null=True),
        ),
    ]