# Generated by Django 4.2.11 on 2024-03-31 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, help_text='Designates whether the user can log into company admin dashboard.', verbose_name='Company Admin status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='username'),
        ),
    ]