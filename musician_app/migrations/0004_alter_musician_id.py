# Generated by Django 5.1 on 2024-08-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician_app', '0003_alter_musician_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
