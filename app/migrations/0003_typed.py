# Generated by Django 4.1.3 on 2022-11-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_timer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typed',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fixo', models.CharField(max_length=50)),
                ('txt_01', models.CharField(max_length=50)),
                ('txt_02', models.CharField(max_length=50)),
                ('txt_03', models.CharField(max_length=50)),
                ('txt_04', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Efeito de digitação',
            },
        ),
    ]
