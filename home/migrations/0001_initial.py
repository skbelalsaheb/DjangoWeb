# Generated by Django 3.0.7 on 2020-12-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=200)),
                ('authorName', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('path', models.ImageField(upload_to='media/')),
                ('descr', models.CharField(max_length=500)),
            ],
        ),
    ]
