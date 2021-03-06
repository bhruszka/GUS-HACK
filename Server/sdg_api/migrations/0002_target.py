# Generated by Django 2.1.3 on 2018-11-09 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdg_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('goal', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('uri', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
