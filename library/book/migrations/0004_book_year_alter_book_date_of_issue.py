# Generated by Django 4.1 on 2023-02-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('book', '0003_book_date_of_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, default=2000),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_of_issue',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]