# Generated by Django 2.2.17 on 2021-02-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SNS', '0005_auto_20210209_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reposts',
            field=models.ManyToManyField(related_name='reposts', to='SNS.Post'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='SNS.Post'),
        ),
    ]
