# Generated by Django 4.2.4 on 2023-09-23 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blogposts_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='communityList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('introduce', models.CharField(max_length=250)),
                ('avatar', models.ImageField(default='https://static.vecteezy.com/system/resources/thumbnails/005/545/335/small/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg', upload_to='images/%y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='blogposts',
            name='images',
            field=models.ImageField(default='https://static.vecteezy.com/system/resources/thumbnails/005/545/335/small/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg', upload_to='images/%y/%m/%d'),
        ),
    ]
