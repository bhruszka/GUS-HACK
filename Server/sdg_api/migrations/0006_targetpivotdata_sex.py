# Generated by Django 2.1.3 on 2018-11-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdg_api', '0005_targetpivotdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetpivotdata',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
