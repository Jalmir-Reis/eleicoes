# Generated by Django 4.1.3 on 2022-11-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('img_01', models.ImageField(blank=True, upload_to='')),
                ('img_02', models.ImageField(blank=True, upload_to='')),
                ('img_03', models.ImageField(blank=True, upload_to='')),
                ('img_04', models.ImageField(blank=True, upload_to='')),
                ('img_05', models.ImageField(blank=True, upload_to='')),
                ('img_06', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Slide de Imagens',
            },
        ),
    ]
