# Generated by Django 5.0.3 on 2024-04-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_delete_item_delete_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='termin',
            field=models.DateField(null=True),
        ),
    ]
