# Generated by Django 2.1.3 on 2018-11-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0002_auto_20181110_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='fact_type',
            field=models.CharField(choices=[('new_old', 'new_old'), ('one_point', 'one_point')], default='one_point', max_length=10),
        ),
    ]