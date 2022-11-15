# Generated by Django 4.1.3 on 2022-11-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('timer', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Contagem Regressiva',
            },
        ),
    ]
