# Generated by Django 3.2.5 on 2022-05-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]