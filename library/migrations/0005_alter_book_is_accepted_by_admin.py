# Generated by Django 4.2.3 on 2023-07-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_is_accepted_by_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_accepted_by_admin',
            field=models.BooleanField(default=False),
        ),
    ]
