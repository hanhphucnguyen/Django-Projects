# Generated by Django 2.2.7 on 2019-12-11 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataForGalery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='hinh/', verbose_name='data image')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('desciption', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='ima',
            field=models.ImageField(default='', upload_to='hinh/'),
        ),
    ]
