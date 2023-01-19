# Generated by Django 4.1.3 on 2022-11-10 15:39

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=timezone.now, help_text='fecha de publicación'),
        ),
    ]
