# Generated by Django 2.1.5 on 2019-02-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_quizsessions'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsessions',
            name='current_question',
            field=models.IntegerField(default=0),
        ),
    ]
