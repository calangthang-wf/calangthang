# Generated by Django 4.2.4 on 2023-10-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_newarticle_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newarticle',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, unique=True),
        ),
    ]
