# Generated by Django 4.2.6 on 2024-08-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=5841984166, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]