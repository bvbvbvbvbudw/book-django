# Generated by Django 5.0.3 on 2024-03-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='preview',
            field=models.FileField(blank=True, null=True, upload_to='static/uploads'),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(upload_to='static/uploads/books/'),
        ),
    ]