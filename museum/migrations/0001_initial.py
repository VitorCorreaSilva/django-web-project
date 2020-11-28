# Generated by Django 3.1.2 on 2020-11-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField()),
            ],
        ),
    ]