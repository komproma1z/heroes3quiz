# Generated by Django 2.1.5 on 2019-02-11 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
