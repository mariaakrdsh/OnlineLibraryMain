# Generated by Django 4.1 on 2023-02-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('book', '0004_book_year_alter_book_date_of_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_of_issue',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
