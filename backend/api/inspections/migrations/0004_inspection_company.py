# Generated by Django 4.0.4 on 2022-05-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0003_rename_items_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='Company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
