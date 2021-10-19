# Generated by Django 3.2.7 on 2021-09-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('courseCode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=100)),
                ('courseTeacher', models.CharField(max_length=50)),
                ('corseSeason', models.CharField(max_length=10)),
                ('courseKey', models.CharField(max_length=10)),
            ],
        ),
    ]