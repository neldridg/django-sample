# Generated by Django 3.1 on 2020-08-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cats')),
                ('uploaded_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
