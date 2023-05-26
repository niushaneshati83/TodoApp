# Generated by Django 4.2 on 2023-04-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('done', models.BooleanField(verbose_name='انجام شده')),
            ],
            options={
                'verbose_name': 'تسک',
                'verbose_name_plural': 'تسک ها',
            },
        ),
    ]