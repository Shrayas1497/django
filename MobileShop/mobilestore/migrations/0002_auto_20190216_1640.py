# Generated by Django 2.1.5 on 2019-02-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilestore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobile',
            name='Face_recognition',
        ),
        migrations.AddField(
            model_name='mobile',
            name='Descrption',
            field=models.CharField(default='face recognition,13 mp cammera ', max_length=150),
        ),
    ]
