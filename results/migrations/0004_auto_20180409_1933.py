# Generated by Django 2.0.2 on 2018-04-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20180409_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.TextField(null=True),
        ),
    ]