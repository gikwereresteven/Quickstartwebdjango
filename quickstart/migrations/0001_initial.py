# Generated by Django 2.2.1 on 2019-05-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('talkid', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('borndate', models.DateField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]