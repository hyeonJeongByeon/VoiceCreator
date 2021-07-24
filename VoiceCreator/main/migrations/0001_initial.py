# Generated by Django 3.2.5 on 2021-07-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=20, verbose_name='성별')),
                ('age_group', models.CharField(max_length=20, verbose_name='나이 그룹')),
                ('preference', models.CharField(max_length=20, verbose_name='선호도')),
                ('voice_code', models.CharField(max_length=20)),
                ('audio_url', models.URLField(verbose_name='S3_URL')),
            ],
        ),
    ]
