# Generated by Django 4.2.2 on 2023-07-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WinSearch',
            fields=[
                ('search_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=30)),
                ('search_word', models.CharField(max_length=200)),
                ('search_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'win_search',
                'managed': False,
            },
        ),
    ]
